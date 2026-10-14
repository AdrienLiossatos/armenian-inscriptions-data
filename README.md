# Armenian inscriptions — data

Structured inscription notices extracted from the *Corpus Inscriptionum
Armenicarum* by a vision-language model, together with the corrections
researchers have made to them.

## What is here

| | |
|---|---|
| `notices.jsonl` | the machine extraction, one notice per line |
| `corrections/<id>.json` | human corrections, one file per notice |
| `corrections.json` | all corrections in one file, for the site |

**The extraction is never overwritten.** A correction shadows it, so
*what did the model produce* stays answerable for every field, forever.
`notices.jsonl` is rebuilt wholesale from the extraction pipeline; nothing in it
is hand-edited.

## Correcting a notice

Use the site, [epigraphy.calfa.fr](https://epigraphy.calfa.fr/) — it shows the
catalogue page beside the transcription and writes the correction in the form
this repository expects. Open a notice, press **Edit**, then **Send to GitHub**:
it opens a pre-filled issue. You need a GitHub account; the site will prompt you
to sign in or register.

A workflow then validates the issue. It refuses rather than guesses: an unknown
notice, a field that is not correctable, a crop box outside the page, or a
transcription whose diplomatic brackets do not balance is rejected with an
explanation.

- **Members of the team** (write access to this repository) have their
  correction committed straight away, crediting them as co-author.
- **Everyone else** gets a pull request from `correction/<issue>`. An editor
  checks it against the scan; merging publishes it and records the editor as
  `approved_by`, closing declines it. Editing the issue updates the pull request
  while it is open. One contributor can have at most 50 corrections awaiting
  review; beyond that, new ones are put on hold.

`corrections.json`, the file the site reads, is rebuilt from `corrections/`
whenever a correction is published. To rebuild it by hand, run the
*publish reviewed correction* workflow from the Actions tab.

## Diplomatic notation

Transcriptions are diplomatic. These marks are data, not formatting, and are
preserved exactly:

| mark | meaning |
|---|---|
| `⎡ ⎤` | letters restored by the editor |
| `⎣ ⎦` | an error or omission on the stone |
| `[ ]` | extraneous characters |
| `...` | letters destroyed, count unknown |
| `/` | a line boundary on the stone |

Do not modernise the Armenian, normalise the characters, or replace these
brackets with ordinary parentheses.

## Images

Page scans are not in this repository — they are served separately; see the project notes.
