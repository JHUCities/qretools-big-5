# Big Five personality markers

A QREtools workspace holding the 50 items of the **IPIP Big-Five Factor Markers**, and
one instrument that asks all 50 and computes the five factor scores.

- 50 questions, ten for each factor, in five folders by factor.
- One shared scale, `agreement5`, which every item uses.
- Five shared concepts, one per factor, which the questions and their variables refer to.
- `instruments/big5.yaml`: the items in IPIP's published order, then the five scores.

## Where the items come from

The items are Lewis R. Goldberg's, published by the **International Personality Item
Pool** at <https://ipip.ori.org/New_IPIP-50-item-scale.htm>. IPIP puts its items and
scales in the public domain: anyone may copy, edit, translate or use them for any
purpose, without asking permission and without paying a fee. They are reproduced here
word for word, because with a measure the wording is the instrument.

The measure itself: Goldberg, L. R. (1992). The development of markers for the Big-Five
factor structure. *Psychological Assessment*, 4, 26–42.

## The response options are not IPIP's, and that is deliberate

IPIP publishes these items with an accuracy scale (*Very Inaccurate* to *Very
Accurate*). This workspace uses an agreement scale instead — *Disagree*, *Slightly
disagree*, *Neutral*, *Slightly agree*, *Agree* — because that is how the Open-Source
Psychometrics Project fields the same 50 items, and its public response set of about a
million answers is the human comparison this workspace is meant to serve. Answers
collected on one scale are not answers collected on the other, so the workspace names
one and only one.

Two consequences, both on purpose:

- **The preamble is ours, not IPIP's.** IPIP's instruction names its own response
  options, so it could not be used unchanged. The instrument's first line keeps IPIP's
  own sentence — "Describe yourself as you generally are now, not as you wish to be in
  the future" — and says the rest in terms of agreeing and disagreeing.
- **Changing the wording is not an edit to these files.** If the accuracy scale is ever
  wanted, it belongs here as a second scale with 50 sibling questions that declare
  `variant_of` against these, so that the two sets of answers can never be mistaken for
  each other. Editing `scales/agreement5.yaml` would silently change what every answer
  already collected means.

## The scores

Each item becomes its own value first — `points_life_of_party` is the answer as a number,
`points_talks_little` is 6 minus it, because that item is keyed the other way — and each
factor's score is the plain sum of its ten. 6 is the lowest code plus the highest, so a
score runs from 10 to 50. 24 of the 50 items are reverse-keyed. Factor IV is scored as
**emotional stability**, as IPIP keys it, not as neuroticism.

The scoring lives in the instrument and nowhere else: one line says how an item is keyed,
and the question itself says only what it asks. Two reasons to keep that shape rather than
folding the reversals back into the five sums:

- One line per item can be checked against IPIP's own keying. A sum of ten terms with
  minus signs in it cannot, not quickly.
- It is what Qualtrics can run. A survey platform has to be told "every one of these
  answers was given" before it computes anything, and for a question with options that
  means one test per option; ten items at once is far past what Qualtrics accepts, while
  one item at a time is five tests, and the sum then asks only whether ten values are
  there.

An item left unanswered, or refused, leaves that whole score empty. Nothing is imputed.
The missing-value codes are words (`REF`, `DK`) rather than numbers so that this holds by
construction: a score reads each answer as a number, and a code that is not a number
reads as empty. A numeric refusal code such as `99` would be added to the score instead.

## It is generated

`scales/`, `universes/`, `concepts/`, `questions/` and `instruments/` are written by
`tools/generate.py` from the tables at the top of that file. Don't edit them by hand:

```sh
python -I tools/generate.py                      # rewrite them
python -I tools/generate.py && git diff --exit-code   # has anything drifted?
```

`workspace.yaml`, `missing.yaml`, this file and `AGENTS.md` are written by hand.

## Releases

A draft instrument on a branch may read this workspace as `../`, the questions as they are
on that branch. On `main`, which is what a release includes, it reads them at a release
tag: `bank: JHUCities/qretools-big-5@v1`. The generator writes that line from `RELEASE`,
at the top of `tools/generate.py`, and writes no instrument while `RELEASE` is `None`.

So questions are released before the instrument uses them. To change them:

1. Change the tables, run the generator, and merge. If an item is added or renamed, set
   `RELEASE` to `None` first: the released questions don't have it yet, so the
   generator takes the instrument off `main` until step 3. Removing an item needs no
   such step, as the released questions still have it.
2. Release the questions: on GitHub, Actions, then Release, then "Run workflow", with the
   next tag (`v2`, `v3`).
3. Set `RELEASE` to that tag and run the generator. Then run `git fetch --tags` and
   `qretools instrument export instruments/big5.yaml -o dist/big5.json`, which records the
   tag's commit under `locked:` in `workspace.yaml`. Merge.
4. Release again. This release includes the instrument.

Each push to `main`, and each release, publishes the DDI on GitHub Pages: `main` at
<https://jhucities.github.io/qretools-big-5/ddi.json>, and each release in a folder named
for its tag, where it stays: for example
<https://jhucities.github.io/qretools-big-5/v2/instruments/big5.json>. Each release is
built with the qretools that it pins (`.github/workflows/ddi.yml`).

Never make, move or delete a tag by hand. The check on every pull request also builds the
workspace as a release would, and fails if the instrument isn't ready to release. A
ruleset on `main` requires it to pass before a pull request can be merged.

## Open it

- **In the app:** sign in at <https://qretools.com> and enter this repository.
- **From a terminal:** `mise install` gives the pinned tools, then:

  ```sh
  qretools check .                                  # findings, one per line
  qretools instrument check instruments/big5.yaml
  qretools instrument export instruments/big5.yaml -o big5.json   # DDI-Lifecycle 4.0
  ```

## Qualtrics

```sh
qretools instrument export instruments/big5.yaml --qsf -o big5.qsf
```

Then, in Qualtrics: Projects, Create project, Survey, Import a QSF file. The 50 items
become questions; each item's points and each factor's score become embedded data, set as
the respondent goes, so the five scores come out in the response export beside the
answers.

One note is expected and is not a problem: a respondent doesn't see the missing-value
codes as options. Refusing in Qualtrics is leaving the question blank, and a blank item
leaves its own points and its factor's score empty, which is what the codes mean here.
