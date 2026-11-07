# Grilling

How you get anything from the user: where their users are, what the product is, which
documents it needs, and every fact the code does not show. Adapted from the grilling skill.

- **Look first.** Finding facts is your job. Only what the code, the store metadata and the
  existing documents cannot show reaches the user, and a `missing` entry's *Hint* becomes the
  recommendation.
- **Fact tree.** Questions hang off each other: `facts.users.regions` decides which region
  questions exist, and a key in an *Applies when* condition decides whether its section's keys
  are needed at all. The **frontier** is every question whose prerequisites are settled. Ask the
  whole frontier each round; a question that depends on one still open waits for the next round.
  A key whose sections are all switched off is never asked.
- **Ask tool.** Ask through your harness's tool for asking the user multiple-choice questions, as
  many per call as it allows. If you have no such tool, ask the frontier in plain text as a
  numbered list, recommended answer first, and end your turn.
- **Recommend.** Each question lists the recommended answer first, marked as recommended in the
  user's language, picked by the key's *Ask* line and the legal minimum. One click accepts it.
  Word each question so that "yes" accepts the recommended answer; agreeing must never mean
  answering "no".
- **One sentence of why.** When an answer has legal weight, say in one plain sentence what it
  changes in the documents ("If you sell to people in Turkey, you also need a distance sales
  contract.").
- **Record.** Write each answer to `legal/facts.md` as `answered` as soon as it comes; "none" and
  "declined" are answers. Record only answers the user gave.

Done when the frontier is empty.
