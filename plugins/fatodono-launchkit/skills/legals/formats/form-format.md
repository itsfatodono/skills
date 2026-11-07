# Form format

A form skeleton describes one console questionnaire (App Store privacy label, Play data
safety, age rating, and so on). The build branch writes it per `build/build-form.md`; `doc-writer`
fills it; `doc-checker` checks the answers against it.

Header: `doc_id`, `title`, `kind: form`, `platform` (apple | google), `source`
(sampled | official), `sample_count` (sampled only), `scanned`, `format_version`.

## Form
- **Purpose:** one sentence.
- **Lives in:** console path (App Store Connect › App Privacy).
- **Output:** the file the writer produces (fastlane JSON, Play CSV, plist, plain text).
- **Upload:** the command or console step that submits it.

## Questions
In the form's own order:

### <q-id>: <question as the form asks it>
- **Answers:** the allowed values.
- **Facts:** keys from `helpers/facts-schema.md`.
- **Rule:** how the facts decide the answer, from the platform's documentation.
- **Common answers:** sampled only; counts by app kind.
- **Pitfalls:** answers that commonly get rejected or contradict the privacy policy.

Valid when every question in the live form is listed and each has a rule.
