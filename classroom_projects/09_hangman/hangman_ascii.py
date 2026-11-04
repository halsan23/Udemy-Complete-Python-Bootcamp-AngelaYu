words = [
    "aardvark",
    "baboon",
    "battery",
    "blanket",
    "brother",
    "camel",
    "captain",
    "century",
    "chicken",
    "diamond",
    "display",
    "dolphin",
    "elephant",
    "evening",
    "fifteen",
    "freedom",
    "glacier",
    "gravity",
    "harvest",
    "helpful",
    "inspect",
    "journey",
    "justice",
    "kingdom",
    "kitchen",
    "machine",
    "nothing",
    "painted",
    "quickly",
    "rainbow",
    "shelter",
    "teacher",
    "uniform",
    "village",
    "welcome",
]


hangman_text = """
 _   _
| | | |  - can you save me from the gallows -
| |_| | __ _ _ __   __ _ __ ___ _   __ _ _ __
| '_  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/
"""


# hangman_art = """
# ****************************************
# *       - -   H A N G M A N   - -      *
# * ------------------------------------ *
# *   can you save me from the gallows   *
# ****************************************\n
# """"


stages = [
    r"""
 +---+
 |   |
 |   O
 |  /|\
 |   |
 |  / \
 |
=========
""",
    r"""
 +---+
 |   |
 |   O
 |  /|\
 |   |
 |  /
 |
=========
""",
    r"""
 +---+
 |   |
 |   O
 |  /|\
 |   |
 |
 |
=========
""",
    """
 +---+
 |   |
 |   O
 |  /|\\
 |
 |
 |
=========
""",
    """
 +---+
 |   |
 |   O
 |  /|
 |
 |
 |
=========
""",
    """
 +---+
 |   |
 |   O
 |   |
 |
 |
 |
=========
""",
    """
 +---+
 |   |
 |   O
 |
 |
 |
 |
=========
""",
    """
 +---+
 |   |
 |
 |
 |
 |
 |
=========
""",
]
