# Portal probe: can curl read blocked DSAR portals?

Date: 2026-10-27. Scope: the `(blocked)` rows in `pool/dsar-us.md` and `pool/dsar-eu-uk.md`. The real count is **49**, not 50: 32 US and 17 EU/UK. The 50th grep hit is the EU/UK "Routes:" note line. Tools: curl, python3 and the Wayback CDX only. No browser was used.

**Answer: yes for OneTrust and Transcend, which together cover 26 of the 49 rows. TrustArc also works, but none of the 49 rows uses it.** Each of these vendors publishes the whole form definition as JSON. That JSON includes request types, subject types, fields with their required flags, ID-verification settings, and all notice text through the translation tables. `<noscript>` blocks never helped: OneTrust's only holds a stylesheet link, and the other vendors' blocks just say "enable JavaScript".

## Recipes

### OneTrust: works (24/24 rows recovered; 1 needed a redirect hop)
- URL patterns in the pool: `privacyportal[-uk|-eu|-de].onetrust.com/webform/{orgId}/{formId}`, `{tenant}.my.onetrust.com/webform/...`, `.../webform/{orgId}/draft/{formId}`, and a custom domain (`www.sars.natwestgroup.com/webform/...`). All of them behave the same way.
- Recipe: run a plain `curl -L` on the row URL. The page is Angular SSR. The full config sits inline in `<script id="dsar-components-state" type="application/json">`. Decode the entities `&q;`→`"`, `&a;`→`&`, `&s;`→`'`, `&l;`→`<`, `&g;`→`>`, then parse the JSON. Read the entry whose key contains `/webform/{formId}/publish`. Its `body` has these parts:
  - `requestTypes`, `subjectTypes`: field keys only. Labels come from `formFields[fieldKey=requestTypes|subjectTypes].options[].value`, plus `tooltipValue`.
  - `formFields[]`: `fieldKey`, `inputType`, `isRequired`, `isSelected`, `isHidden`, `options`. Keep rows with `isSelected` true. Some forms have more than 100 selected fields, because visibility rules in `formSettingInputs` make many of them conditional.
  - `formTranslations['en-us']`: labels (key = `fieldKey`) and notice text (`WelcomeText`, `*HelpTextDisplayText`, acknowledgement text). `globalTranslations` has the shared strings.
  - `idVerification`: for example `EmailVerification`, `IdVerificationEnabled`, `EnablePhoneNumberVerification`, `OpenIdEnabled`.
- The form id is the last UUID in the path (it is also in `<meta name="webformId">`). The URL alone is enough; nothing else needs to be fetched.
- Edge case: GEICO returned `isDisabled: true`, all fields `null`, and a `reDirectUrl` that points to a new webform. Fetching that URL with the same recipe worked.
- The documented API (`DSAR_API/webform/{id}/publish`) uses an internal hostname (`datasubject-access:8080`), so it cannot be reached. The SSR blob is the only route.

### Transcend: works (2 rows: Taco Bell live, OpenAI through Wayback)
- How to detect it: `api.transcend.io` or `transcend-cdn.com` appears in the HTML, or the inline script fetches `/static/{host}/privacyCenter.json`.
- Recipe: fetch these static files from `https://{host}/static/{host}/`:
  - `privacyCenterSubjects.json`: subjects → `actions[]` (`type`, `title`, `description`, `secondaryDescription`, `formItems[]` with `label`, `isRequired`, `type`), plus `loginInstructions` per subject, which is the verification step.
  - `privacyCenterMessages-en.json`: `[{id,value}]` overrides for the `DefinedMessage` ids. Use `defaultMessage` when there is no override.
  - `privacyCenter.json`: org-level settings. Also available: `privacyCenterPolicies-en.json`, `privacyCenterPurposes.json`, `privacyCenterWorkflowConfigs.json`.
- OpenAI (`privacy.openai.com`) returns a Cloudflare 403 to curl. Wayback has the same files: `web.archive.org/web/{ts}id_/https://privacy.openai.com/static/privacy.openai.com/privacyCenterSubjects.json`. The latest capture is 2026-06-04. The response is gzipped, so run `gunzip` on it.
- The public GraphQL endpoint (`api.transcend.io/privacy/graphql`) blocks introspection, and it is not needed.

### TrustArc: works (0 rows in the blocked set; tested on 3 outside forms: Appen, Cloud Software Group, TCL)
- URL pattern: `submit-irm.trustarc.com/services/validation/{formId}[?brandId=...]`. The HTML is an empty shell and `const intakeFormId = "..."` appears in the inline script.
- Recipe: `GET https://submit-irm.trustarc.com/services/validation/api/v1/forms/{formId}/render?locale=en[&brandId=...]` returns JSON with no auth:
  - `content.formFields[]`: `type.id` (for example `data-subject-select`, `request-type-select`, `Email`, `Country`, `StaticText`, `Checkbox`, `FileAttachment`), `label` (a translation key), `settings.required.value`, `extras.optionList` / `extras.optionLabels` (request types) / `extras.message` (notice and attestation text).
  - `localeTranslations[key].value`: resolves every UUID key, including the title, labels and notices.
  - `content.verifyEmail`, `content.verifyIdentity`, `captchaTypes`: the verification steps.
- Minor gap: plain `Select` options keep their labels under a key shape I did not map, so they came out as `None`. This is a parser detail, not a blocker.

### Others (not recovered; DataGrail was the only one probed past fingerprinting)
- DataGrail (`/api/v2/privacy_rights` and similar return 401 without the page's session/CSRF) and SixFifty RequestEasy (Vite SPA, API not located) failed within the time I gave them. The rest were only fingerprinted.

## Vendor count across the 49 blocked rows

| Vendor | Rows | curl recipe |
|---|---|---|
| OneTrust (incl. NatWest custom domain) | 24 | works |
| Transcend (Taco Bell, OpenAI) | 2 | works (OpenAI only through Wayback) |
| TrustArc | 0 | works (tested outside the pool) |
| SixFifty RequestEasy (Dutch Bros, Ace Parking) | 2 | not found |
| Zendesk help-centre forms (McDonald's UK, Home Store + More) | 2 | 403 to curl; not tried |
| DataGrail (MyFitnessPal) | 1 | API needs session; no |
| Relyance (Opendoor) | 1 | not tried |
| Typeform (Perplexity), Termly (Blossom), Pipedrive webforms, Salesforce Experience Cloud (eBay) | 1 each, 4 total | not tried |
| In-house SPA (Capital One, Experian, Wells Fargo, Sainsbury's Bank, WeChat, Instacart, Klarna) | 7 | not tried; each would need its own recipe |
| Bot wall / WAF, vendor unknown (Walmart, Ledger, At Home, Santander Consumer, Severn Trent, Jet2) | 6 | curl blocked (403, block page or timeout) |
| **Total** | **49** | |
