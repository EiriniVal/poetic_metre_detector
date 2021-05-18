import re
import operator
from collections import Counter
from itertools import islice

unstressed_vowels = ("α", "ε", "η", "ι", "ο", "ω", "υ")
from syllabifier import syllabify_verse, vowels


def adjust_syllables_for_metre_detection(syllables_list: list) -> list:
    """
    Function that takes as input a list of syllables and processes them to detect and handle cases of;
    i) synizesis (note: only for the case when a syllable ends with an unstressed vowel and the following syllable
    starts with an unstressed vowel. stressed vowels were not included here because the metre detection will be based on
    them. Since, synizesis is not that common on stressed vowels, it was not worth the risk using it and having altered
    results.)
    ii) cases where a monosyllable word is in the list and does not consist of a vowel (due to idioms/dialect forms)
    e.g. "τσ" instead of "της". In this case, the monosyllable word is merged with the following syllable which starts
    with a vowel because in the verse they are pronounced as one. For example, if the function takes as input the list
    ["τσ","αυ","γής], it will return the list ["τσαυ","γής"].
    :param syllables_list: a list consisting of the syllables of a verse
    :return: a list where syllables are changed if any of the cases mentioned above are present in the verse
    """
    # prepare syllables for metre detection
    # handle synizesis if it exists in the verse
    for index, token in enumerate(syllables_list):
        if token.endswith(unstressed_vowels) and index != len(syllables_list) - 1:
            if syllables_list[index + 1].startswith(unstressed_vowels):
                syllables_list[index: index + 2] = ["".join(syllables_list[index: index + 2])]

    # handle cases were there is no vowel in syllable/token due to idioms/dialects
    for index, token in enumerate(syllables_list):
        if re.search(r"[αεηιοωυάέήίόώύϊϋΐΰ]", token) is None:
            if syllables_list[index + 1].startswith(vowels):
                syllables_list[index: index + 2] = ["".join(syllables_list[index: index + 2])]
            else:
                # if next syllable does not start with a vowel, merge it with the previous one
                syllables_list[index: index - 2] = ["".join(syllables_list[index: index - 2])]
        else:
            continue
    return syllables_list


def is_stressed(syllable: str) -> bool:
    """
    Function that returns True if the given string, in this case syllable, is stressed
    :param syllable: the syllable
    :return: True, if syllable is stressed, otherwise False.
    """
    if re.search(r"[άέήίόώύΐΰ]", syllable) is None:
        return False
    else:
        return True


def detect_stress(syllables_list: list) -> list:
    """
    Function that takes as input a list of syllables and identifies them as stressed or unstressed.
    :param syllables_list: list consisting of syllables
    :return: list consisting with the corresponding identification for syllables as stressed (s) or unstressed (u)
    """
    metre_list = []
    for syllable in syllables_list:
        if is_stressed(syllable):
            metre_list.append("s")
        else:
            metre_list.append("u")
    return metre_list


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


def detect_verse_metre(stress_list: list) -> tuple:
    """
    Function that takes as input a list consisting of a sequence of "s" (stressed) and "u" (unstressed) elements, which
    correspond to the syllables of a verse, computes the scores for each metre in Modern Greek, and returns them in a
    dict. The score is counted as follows:
    i) the sequences are separated in groups of two or three (depending on the metre)
    ii) for each metre the function counts the occurrences of the specific pattern e.g the pattern ('u', 's') for the
    iambic)
    iii) the number of occurrences is then divided by the total number of groups. This division is critical in order to
    have normalized and comparable results between the metres whose pattern is disyllabic and those whose pattern is
    trisyllabic.
    :param stress_list: a list consisting of a sequence of "s" and "u"
    :return: tuple consisting of a dict with the names of the metres as keys and the scores as values, and a string
    which is the metre with the highest score
    """
    # create a list with pairs to check for iambic and trochaic
    tuple_list = list(chunk(stress_list, 2))
    # count how many triads our list has in order to normalize the score
    total_tuples = len(tuple_list)
    iambic_counts = tuple_list.count(('u', 's')) / total_tuples
    trochaic_counts = tuple_list.count(('s', 'u')) / total_tuples

    # create a list with triads to check for anapaest, messotonos, dactyl
    triad_list = list(chunk(stress_list, 3))
    # count how many triads our list has in order to normalize the score
    total_triads = len(triad_list)
    anapaest_counts = triad_list.count(('u', 'u', 's')) / total_triads
    dactyl_counts = triad_list.count(('s', 'u', 'u')) / total_triads
    messotonos_counts = triad_list.count(('u', 's', 'u')) / total_triads
    metre_scores_dict = {"iambic": iambic_counts, "trochaic": trochaic_counts, "anapaest": anapaest_counts,
                         "dactyl": dactyl_counts, "messotonos": messotonos_counts}
    # print(f"iambic: {iambic_counts}\ntrochaic: {trochaic_counts}\nanapaest: {anapaest_counts}\ndactyl: {
    # dactyl_counts}\nmessotonos: {messotonos_counts}")
    #print(f"Metre detected for verse: {metre_detected}")
    metre_detected = max(metre_scores_dict.items(), key=operator.itemgetter(1))[0]
    return metre_scores_dict, metre_detected


def detect_poem_metre(poem_filename: str):
    """
    Function that takes as input a (Modern) Greek poem in text file and returns:
    i) the metres scores per verse
    ii) the metre chosen per verse
    iii) the poem's metre
    :param poem_filename: the text file containing a single poem
    """
    metre_verse_list = []
    counter = 1
    with open(poem_filename, "r", encoding="utf8") as f:
        for line in f:
            stress_list = detect_stress(adjust_syllables_for_metre_detection(syllabify_verse(line)))
            #print(line)
            d = detect_verse_metre(stress_list)
            metre_detected = max(d.items(), key=operator.itemgetter(1))[0]
            metre_verse_list.append(metre_detected)
            print(f"Metre scores for verse {counter}: {d} ")
            print(f"Metre detected for verse {counter}: {metre_detected}")
            counter += 1
        poem_metre = Counter(metre_verse_list).most_common(1)[0][0]
        print(f"The poem's metre is: {poem_metre}")
        return poem_metre

