import re

vowels = ("α", "ε", "η", "ι", "ο", "ω", "υ", "ά", "έ", "ή", "ί", "ό", "ώ", "ύ", "ϊ", "ϋ", "ΐ", "ΰ")

consonants = ["β", "γ", "δ", "ζ", "θ", "κ", "λ", "μ", "ν", "ξ", "π", "ρ", "σ", "τ", "φ", "χ", "ψ", "ς", "μπ", "ντ",
              "γκ", "τσ", "τζ"]

cons_tuples_start_greek = ["βγ", "βδ", "βλ", "βρ", "γδ", "γκ", "γλ", "γν", "γρ", "δρ", "θλ", "θν", "θρ", "κβ", "κλ",
                           "κν", "κρ", "κτ", "μν", "μπ", "ντ", "πλ", "πν", "πρ", "πτ", "σβ", "σγ", "σθ", "σκ", "σλ",
                           "σμ", "σν", "σπ", "στ", "σφ", "σχ", "τζ", "τμ", "τρ", "τσ", "τς", "φθ", "φκ", "φλ", "φρ",
                           "φτ", "φχ", "χθ", "χλ", "χν", "χρ", "χτ"]

diphthongs = ["αι", "ει", "οι", "ου", "υι", "αυ", "ευ", "ια", "ιε", "ιο", "ιω", "υα", "υο", "υω", "αί", "εί", "οί",
              "ού", "υί", "αύ", "εύ", "ιά", "ιέ", "ιό", "ιώ", "υά", "υό", "υώ", "αη", "όη", "αϊ", "οϊ", "εια", "ειε",
              "ειο", "ειου", "ειώ", "ιου", "οια", "οιε", "οιο", "οιου", "ιοι"]


def is_monosyllable(string: str) -> bool:
    """
    Function that returns True if string is a monosyllable word.
    :param string: string to be checked
    :return: True if string is monosyllable, otherwise False
    """
    counter = 0
    index_char = 0
    while index_char <= len(string) - 1:
        # if char is vowel and is not in the last position of string
        if string[index_char] in vowels and index_char != len(string) - 1:
            # if it forms a diphthong with the following letter and they are not in the end of the string
            if string[index_char] + string[index_char + 1] in diphthongs and index_char != len(string) - 2:
                # check if they form a diphthong together with the 3rd following letter
                if string[index_char] + string[index_char + 1] + string[index_char + 2] in diphthongs:
                    counter += 1
                    # count them as one
                    index_char += 3
                else:
                    counter += 1
                    # increment index by 2 in order not to count the following vowel separately
                    index_char += 2
            # if it forms a diphthong but it is at the end of string
            elif string[index_char] + string[index_char + 1] in diphthongs and index_char == len(string) - 2:
                counter += 1
                break
            # if it does not form a diphthong, just count it as a single vowel
            else:
                counter += 1
                index_char += 1
        # if it is a vowel but it's at the end of the string, only count it
        elif string[index_char] in vowels and index_char == len(string)-1:
            counter += 1
            break
        # if it is a consonant or anything else, move to the next char
        else:
            index_char += 1

    if counter == 1:
        return True
    else:
        return False


def syllabify_token(string: str) -> str:
    """
    Function that does the syllabification token-wise.
    :param string: token to be syllabified
    :return: token with syllables separated by space
    """
    index_char = 0

    while index_char < len(string) - 1:
        char = string[index_char]
        if char in consonants:
            # if consonant is not in the beginning or end of the string
            if index_char > 0:
                # 1) look before and after the consonants to see if it is surrounded by vowels φτά/νω
                if string[index_char - 1] in vowels and string[index_char + 1] in vowels:
                    # separate before consonant and renew string
                    string = string[: index_char] + " " + string[index_char:]
                    index_char += 1
                # 2) look if before it there is a vowel and after it there is another consonant
                elif string[index_char - 1] in vowels and string[index_char + 1] in consonants:
                    # if greek words start with this combination, don't split them
                    if string[index_char] + string[index_char + 1] in cons_tuples_start_greek:
                        string = string[: index_char] + " " + string[index_char:]
                    # if no greek word start with this combination, split them
                    else:
                        string = string[: index_char + 1] + " " + string[index_char + 1:]
                    index_char += 1
                # if index_char-1 is " " or consonant
                else:
                    index_char += 1
            # we need it in order in order to move from char at position 0 to the next one
            else:
                index_char += 1
        else:
            # if vowel is followed by another vowel
            if string[index_char] in vowels and string[index_char + 1] in vowels:
                # and they form a diphthong
                if string[index_char] + string[index_char + 1] in diphthongs:
                    index_char += 1
                # if they do not form a diphthong
                else:
                    # split them
                    string = string[: index_char + 1] + " " + string[index_char + 1:]
                    index_char += 1
            # if vowel is followed by a consonant
            else:
                index_char += 1
    return string


def syllabify_verse(verse: str) -> list:
    """
    Function that does the syllabification verse-wise.
    :param verse: the verse of the poem we want to syllabify
    :return: a list consisting of the syllables of the verse
    """
    syllables_list = []
    for token in verse.lower().split(" "):
        syllables_list.append(syllabify_token(token) if is_monosyllable(token) is False else token)
    string_verse = " ".join(syllables_list)
    syllables_list = re.split(r"\s", string_verse)
    syllables_list = list(filter(None, syllables_list))
    return syllables_list
