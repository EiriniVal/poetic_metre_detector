import re
unstressed_vowels = ("α", "ε", "η", "ι", "ο", "ω", "υ")
from syllabifier import syllabify_verse


def adjust_syllables_for_metre_detection(syllables_list: list) -> list:
    # prepare syllables for metre detection
    # handle synizesis if it exists in the verse
    for index, token in enumerate(syllables_list):
        if token.endswith(unstressed_vowels) and index != len(syllables_list)-1:
            if syllables_list[index + 1].startswith(unstressed_vowels):
                syllables_list[index: index+2] = ["".join(syllables_list[index: index+2])]

    # handle cases were there is no vowel in syllable/token due to idioms/dialects
    for index, token in enumerate(syllables_list):
        if re.search(r"[αεηιοωυάέήίόώύϊϋΐΰ]", token) is None:
            syllables_list[index: index+2] = ["".join(syllables_list[index: index+2])]
        else:
            continue
    return syllables_list



