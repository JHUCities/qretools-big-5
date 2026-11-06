"""Writes this workspace from the 50 items of the IPIP Big-Five Factor Markers.

Usage: python -I tools/generate.py [dir]
<dir> is the workspace to write (default: the directory holding this script's parent).

scales/, universes/, concepts/, questions/ and instruments/ are written from the tables
below; workspace.yaml, missing.yaml, README.md and AGENTS.md are written by hand. Edit a
table and run this again: it writes the same bytes every time, so

    python -I tools/generate.py && git diff --exit-code

says whether anything has drifted.

The items are Lewis R. Goldberg's, from the International Personality Item Pool
(https://ipip.ori.org/New_IPIP-50-item-scale.htm), which puts its items and scales in
the public domain. They are copied word for word, because the wording is the instrument.
The response options are not IPIP's: see README.md.
"""

import os
import sys

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

# The response options, as the Open-Source Psychometrics Project fields these items
# (openpsychometrics.org), whose public response set is the human half this workspace is
# meant to be compared with. README.md says why these and not IPIP's own.
SCALE = "agreement5"
SCALE_LABELS = [
    ("1", "Disagree"),
    ("2", "Slightly disagree"),
    ("3", "Neutral"),
    ("4", "Slightly agree"),
    ("5", "Agree"),
]
# A reversed answer counts the other way round: lowest plus highest, less the answer.
REVERSE = int(SCALE_LABELS[0][0]) + int(SCALE_LABELS[-1][0])

UNIVERSE = ("all_respondents", "Everyone who takes the inventory.")

# Said once, before the items. The last sentence is IPIP's own instruction; the rest is
# ours, because IPIP's names its own response options and this workspace uses others.
PREAMBLE = (
    "The next pages describe people's behavior. For each phrase, say how much you agree "
    "or disagree that it describes you. Describe yourself as you generally are now, not "
    "as you wish to be in the future."
)

# One per factor, in the order the items first reach them. The key is the letter the
# table below uses; `score` is the name of the computed score, and of the concept.
FACTORS = {
    "E": ("extraversion", "Extraversion", "How outgoing, talkative and sociable someone says they are."),
    "A": ("agreeableness", "Agreeableness", "How warm, sympathetic and considerate someone says they are toward other people."),
    "C": ("conscientiousness", "Conscientiousness", "How orderly, dependable and diligent someone says they are."),
    "N": ("emotional_stability", "Emotional stability", "How calm and even-tempered someone says they are, rather than easily upset. IPIP keys this factor as stability, not as neuroticism."),
    "O": ("intellect_imagination", "Intellect and imagination", "How curious, imaginative and quick to grasp ideas someone says they are."),
}

# The 50 items in IPIP's published order: number, factor, keying, our name, our title,
# and the item, word for word. "+" counts toward the factor, "-" against it.
ITEMS = [
    (1, "E", "+", "life_of_party", "Life of the party", "Am the life of the party."),
    (2, "A", "-", "little_concern_for_others", "Little concern for others", "Feel little concern for others."),
    (3, "C", "+", "always_prepared", "Always prepared", "Am always prepared."),
    (4, "N", "-", "stressed_easily", "Gets stressed easily", "Get stressed out easily."),
    (5, "O", "+", "rich_vocabulary", "Rich vocabulary", "Have a rich vocabulary."),
    (6, "E", "-", "talks_little", "Doesn't talk a lot", "Don't talk a lot."),
    (7, "A", "+", "interested_in_people", "Interested in people", "Am interested in people."),
    (8, "C", "-", "leaves_belongings_around", "Leaves belongings around", "Leave my belongings around."),
    (9, "N", "+", "relaxed_most_of_the_time", "Relaxed most of the time", "Am relaxed most of the time."),
    (10, "O", "-", "abstract_ideas_hard", "Finds abstract ideas hard", "Have difficulty understanding abstract ideas."),
    (11, "E", "+", "comfortable_around_people", "Comfortable around people", "Feel comfortable around people."),
    (12, "A", "-", "insults_people", "Insults people", "Insult people."),
    (13, "C", "+", "attention_to_details", "Pays attention to details", "Pay attention to details."),
    (14, "N", "-", "worries_about_things", "Worries about things", "Worry about things."),
    (15, "O", "+", "vivid_imagination", "Vivid imagination", "Have a vivid imagination."),
    (16, "E", "-", "keeps_in_the_background", "Keeps in the background", "Keep in the background."),
    (17, "A", "+", "sympathizes_with_feelings", "Sympathizes with others' feelings", "Sympathize with others' feelings."),
    (18, "C", "-", "makes_a_mess_of_things", "Makes a mess of things", "Make a mess of things."),
    (19, "N", "+", "seldom_feels_blue", "Seldom feels blue", "Seldom feel blue."),
    (20, "O", "-", "not_interested_abstract_ideas", "Not interested in abstract ideas", "Am not interested in abstract ideas."),
    (21, "E", "+", "starts_conversations", "Starts conversations", "Start conversations."),
    (22, "A", "-", "not_interested_others_problems", "Not interested in others' problems", "Am not interested in other people's problems."),
    (23, "C", "+", "chores_done_right_away", "Gets chores done right away", "Get chores done right away."),
    (24, "N", "-", "easily_disturbed", "Easily disturbed", "Am easily disturbed."),
    (25, "O", "+", "excellent_ideas", "Excellent ideas", "Have excellent ideas."),
    (26, "E", "-", "little_to_say", "Has little to say", "Have little to say."),
    (27, "A", "+", "soft_heart", "Soft heart", "Have a soft heart."),
    (28, "C", "-", "forgets_to_put_things_back", "Forgets to put things back", "Often forget to put things back in their proper place."),
    (29, "N", "-", "upset_easily", "Gets upset easily", "Get upset easily."),
    (30, "O", "-", "no_good_imagination", "No good imagination", "Do not have a good imagination."),
    (31, "E", "+", "talks_to_many_at_parties", "Talks to many people at parties", "Talk to a lot of different people at parties."),
    (32, "A", "-", "not_really_interested_others", "Not really interested in others", "Am not really interested in others."),
    (33, "C", "+", "likes_order", "Likes order", "Like order."),
    (34, "N", "-", "changes_mood_a_lot", "Changes mood a lot", "Change my mood a lot."),
    (35, "O", "+", "quick_to_understand", "Quick to understand things", "Am quick to understand things."),
    (36, "E", "-", "avoids_attention", "Avoids drawing attention", "Don't like to draw attention to myself."),
    (37, "A", "+", "takes_time_for_others", "Takes time out for others", "Take time out for others."),
    (38, "C", "-", "shirks_duties", "Shirks duties", "Shirk my duties."),
    (39, "N", "-", "frequent_mood_swings", "Frequent mood swings", "Have frequent mood swings."),
    (40, "O", "+", "uses_difficult_words", "Uses difficult words", "Use difficult words."),
    (41, "E", "+", "fine_being_center_of_attention", "Doesn't mind the center of attention", "Don't mind being the center of attention."),
    (42, "A", "+", "feels_others_emotions", "Feels others' emotions", "Feel others' emotions."),
    (43, "C", "+", "follows_a_schedule", "Follows a schedule", "Follow a schedule."),
    (44, "N", "-", "irritated_easily", "Gets irritated easily", "Get irritated easily."),
    (45, "O", "+", "reflects_on_things", "Spends time reflecting", "Spend time reflecting on things."),
    (46, "E", "-", "quiet_around_strangers", "Quiet around strangers", "Am quiet around strangers."),
    (47, "A", "+", "puts_people_at_ease", "Puts people at ease", "Make people feel at ease."),
    (48, "C", "+", "exacting_in_my_work", "Exacting in work", "Am exacting in my work."),
    (49, "N", "-", "often_feels_blue", "Often feels blue", "Often feel blue."),
    (50, "O", "+", "full_of_ideas", "Full of ideas", "Am full of ideas."),
]

SOURCE_URL = "https://ipip.ori.org/New_IPIP-50-item-scale.htm"


def yaml(value):
    """A YAML scalar: quoted only where plain text would be read as something else."""
    text = str(value)
    plain = not text or text[0] in "-?:,[]{}#&*!|>'\"%@`" or ": " in text or " #" in text
    return '"%s"' % text.replace("\\", "\\\\").replace('"', '\\"') if plain else text


def write(path, lines):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write("".join(line + "\n" for line in lines))


def question(n, letter, keying, name, title, text):
    score, label, _ = FACTORS[letter]
    nth = [i[3] for i in ITEMS if i[1] == letter].index(name) + 1
    return [
        "name: " + yaml(name),
        "title: " + yaml(title),
        "text: " + yaml(text),
        "intent: "
        + yaml(
            "Marks %s, as one of the set's ten %s items. The score comes from all ten "
            "together, never from this answer alone." % (label.lower(), label.lower())
        ),
        "concept: " + score,
        "responses: " + SCALE,
        "source: "
        + yaml(
            "IPIP 50-item Big-Five Factor Markers (Goldberg 1992), item %d of 50, %s "
            "item %d. %s" % (n, label.lower(), nth, SOURCE_URL)
        ),
    ]


POINTS = "points_%s"


def points(keying, name):
    """What this item adds to its factor: the answer as a number, reversed if keyed so."""
    read = "cast(bank.%s, integer)" % name
    return read if keying == "+" else "%d - %s" % (REVERSE, read)


def instrument():
    lines = [
        "# The 50 markers of the IPIP Big-Five Factor Markers, asked in the order IPIP",
        "# publishes them, then the five scores.",
        "#",
        "# The order interleaves the five factors on purpose, and it is the order the",
        "# public response set this workspace compares with was fielded in. Don't shuffle",
        "# the items or put them in sections by factor: either would make the answers",
        "# incomparable with it.",
        "#",
        "# Each score adds its ten items, reversing the ones keyed the other way",
        "# (%d - the answer), so every score runs from %d to %d. An item left unanswered"
        % (REVERSE, 10 * int(SCALE_LABELS[0][0]), 10 * int(SCALE_LABELS[-1][0])),
        "# leaves its score empty: nothing is imputed here.",
        "name: big5",
        "title: Big Five personality markers",
        "description: "
        + yaml(
            "The 50 public-domain markers of the five factors, with each factor's score "
            "computed from its ten items."
        ),
        "universe: bank." + UNIVERSE[0],
        "uses:",
        "  bank: ../",
        "flow:",
        "  - say: " + yaml(PREAMBLE),
    ]
    lines += ["  - ask: bank." + i[3] for i in ITEMS]
    for letter, (score, label, _) in FACTORS.items():
        items = [(k, name) for (_, f, k, name, _, _) in ITEMS if f == letter]
        lines.append(
            "  # %s: each item's points, %d of the %d reversed, then the score."
            % (label, sum(1 for k, _ in items if k == "-"), len(items))
        )
        for keying, name in items:
            lines += [
                "  - compute: " + POINTS % name,
                "    value: " + points(keying, name),
            ]
        lines += ["  - compute: " + score, "    value: >-"]
        lines += [
            "      %s%s" % ("" if i == 0 else "+ ", POINTS % name)
            for i, (_, name) in enumerate(items)
        ]
    return lines


def main():
    write("scales/%s.yaml" % SCALE, [
        "# The response options every item uses. See README.md: these are the options the",
        "# public response set was collected with, not IPIP's own.",
        "labels:",
    ] + ['  "%s": %s' % (code, yaml(label)) for code, label in SCALE_LABELS])
    write("universes/%s.yaml" % UNIVERSE[0], ["text: " + yaml(UNIVERSE[1])])
    for score, label, definition in FACTORS.values():
        write("concepts/%s.yaml" % score, [
            "label: " + yaml(label),
            "definition: " + yaml(definition),
        ])
    for n, letter, keying, name, title, text in ITEMS:
        write(
            "questions/%s/%s.yaml" % (FACTORS[letter][0], name),
            question(n, letter, keying, name, title, text),
        )
    write("instruments/big5.yaml", instrument())

    # What the tables must hold for the scores to mean anything.
    names = [i[3] for i in ITEMS]
    assert len(ITEMS) == 50, len(ITEMS)
    assert [i[0] for i in ITEMS] == list(range(1, 51))
    assert len(set(names)) == 50
    assert all(len(n) <= 64 and n.replace("_", "a").isalnum() and n.islower() for n in names)
    assert set(i[1] for i in ITEMS) == set(FACTORS)
    for letter in FACTORS:
        assert sum(1 for i in ITEMS if i[1] == letter) == 10, letter
    assert sum(1 for i in ITEMS if i[2] == "-") == 24
    assert all(i[2] in "+-" for i in ITEMS)
    # Every item is asked once, and scored once.
    flow = instrument()
    for name in names:
        assert flow.count("  - ask: bank." + name) == 1, name
        assert sum(line.count("bank.%s," % name) for line in flow) == 1, name
        assert flow.count("  - compute: " + POINTS % name) == 1, name
        # Read once, by exactly one score, as a whole line of its sum.
        read = [l for l in flow if l.strip().lstrip("+ ") == POINTS % name]
        assert len(read) == 1, name
    print("wrote %d questions, %d concepts, 1 scale, 1 universe and 1 instrument into %s"
          % (len(ITEMS), len(FACTORS), os.path.normpath(OUT)))


main()
