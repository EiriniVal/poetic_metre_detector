import re
import operator
from itertools import islice
from syllabifier import syllabify_verse, vowels

unstressed_vowels = ("α", "ε", "η", "ι", "ο", "ω", "υ")


def adjust_syllables_for_metre_detection(syllables_list: list) -> list:
    """
    Function that takes as input a list of syllables and processes them to detect and handle cases of:
    i) synizesis (note: only for the case when a syllable ends with an unstressed vowel and the following syllable
    starts with an unstressed vowel. Synizesis with stressed vowels is not that common and is excluded in the current
    implementation. The metre detection is strictly based on the stress, and including synizesis with stressed vowels
    would frequently create less accurate metric patterns.)
    ii) cases where a monosyllable word is in the list and does not consist of a vowel (due to idioms/dialect forms)
    e.g. "τσ" instead of "της". In this case, the monosyllable word "τσ" is merged with the following syllable, which
    starts with a vowel, because in the verse they are pronounced as one. For example, if the function takes as input
    the list ["τσ","αυ","γής], it will return the list ["τσαυ","γής"].
    :param syllables_list: a list consisting of the syllables of a verse
    :return: a list where syllables are changed if any of the cases mentioned above is present in the verse
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
    """
    Function that separates an iterable into tuples of given size
    :param it: iterable
    :param size: size of tuples
    :return: callable iterator
    """
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
    metre_detected = max(metre_scores_dict.items(), key=operator.itemgetter(1))[0]
    return metre_scores_dict, metre_detected


def analyze_poem(poem_filename: str):
    """
    Function that takes as input a (Modern) Greek poem in text file and yields:
    i) each verse
    ii) the number of the verse
    iii) the metre scores for each verse
    iv) each verse's metre
    :param poem_filename: the text file containing a single poem
    """
    counter = 1
    with open(poem_filename, "r", encoding="utf8") as f:
        for line in f:
            stress_list = detect_stress(adjust_syllables_for_metre_detection(syllabify_verse(line)))
            d = detect_verse_metre(stress_list)[0]
            metre_detected_verse = max(d.items(), key=operator.itemgetter(1))[0]
            yield line, counter, d, metre_detected_verse
            counter += 1
