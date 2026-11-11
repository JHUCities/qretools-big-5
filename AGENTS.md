# Working in this workspace

A QREtools workspace holding the 50 IPIP Big-Five Factor Markers and one instrument that
scores them. `README.md` says where the items come from, why the response options are not
IPIP's, and what the scores do. Read both before changing anything.

## The one rule: it's generated

`scales/`, `universes/`, `concepts/`, `questions/` and `instruments/` (once `RELEASE` is
set) are written by `tools/generate.py`. Don't edit those files by hand: change the
tables at the top of the generator and run it again (`python -I tools/generate.py`), so
that the keying, the notes, the concepts and the five scoring expressions can never say
two different things.
`workspace.yaml`, `missing.yaml`, `README.md` and this file are written by hand.

The generator ends in assertions: 50 items, ten per factor, 24 reversed, unique names,
and every item asked exactly once and scored exactly once. If one fails, the tables are
wrong, not the assertion.

## Releases

The instrument on `main` reads this workspace at a release tag, never `../`: the
generator writes `bank: JHUCities/qretools-big-5@<RELEASE>`. Releases are made by the
Release workflow, never by hand, and a question change takes two of them (README,
"Releases"). The pull request check runs `qretools build`, but GitHub can't make it
required here: never merge while it fails.

## Things that look like tidying but aren't

- **Don't reword an item.** The wording is the measure. A different wording is a
  different question, and belongs beside these with `variant_of`, not in place of one.
- **Don't change the response options** (`scales/agreement5.yaml`). README.md says why.
- **Don't shuffle the items or group them into sections by factor.** The interleaved
  order is IPIP's and is the order the comparison response set was collected in.
- **Don't give the missing values numeric codes.** A score reads each answer as a number;
  a numeric refusal code would be added to it.
- **Don't fold the reversals into the five sums.** Each item has its own `points_` value,
  keying included, and a score adds those ten names. README.md says why: one line per item
  can be checked against IPIP's keying, and it is the only shape Qualtrics can run.
