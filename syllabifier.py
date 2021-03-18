# Program that syllabifies a greek word
# Author: Eirini Valkana


# create lists
#TODO add uppercase
vowels = ["α", "ε", "η", "ι", "ο", "ω", "υ", "ά", "έ", "ή", "ί", "ό", "ώ", "ύ", "αί", "οί", "εί", "ού", "αι", "οι", "ει", "υι", "ου"]
diphthogs = ["αί", "οί", "εί", "ού","αι", "οι", "ει", "υι", "ου"]
consonants = ["β", "γ", "δ", "ζ", "θ", "κ", "λ", "μ", "ν", "ξ", "π", "ρ", "σ", "τ", "φ", "χ", "ψ", "ς", "μπ", "ντ", "γκ", "τσ", "τζ"]
double_consonants = ["μπ", "ντ", "γκ", "τσ", "τζ"]
double_pron= ["αυ", "ευ"]
semivowel = "ι"

cons_tuples_start_greek = ["βγ", "βδ", "βλ", "βρ", "γδ", "γκ", "γλ", "γν", "γρ", "δρ", "θλ", "θν", "θρ", "κβ", "κλ",
                           "κν", "κρ", "κτ", "μν", "μπ", "ντ", "πλ", "πν", "πρ", "πτ", "σβ", "σγ", "σθ", "σκ",  "σλ",
                           "σμ", "σν", "σπ", "στ",  "σφ", "σχ", "τζ", "τμ", "τρ", "τσ", "φθ", "φκ", "φλ", "φρ", "φτ",
                           "φχ","χθ", "χλ", "χν", "χρ", "χτ"]

cons_triples_start_greek= ["γκλ", "γκρ", "μπλ", "μπρ", "ντρ", "σκλ", "σμπ", "σπλ", "σπρ", "στρ", "σφρ"]


def is_syllable(syllable:str) -> None:
    # consonant + vowel
    if syllable[0] in consonants and syllable[1] in vowels:
        print(True)
    # consonant + dipthog
    elif syllable[0] in consonants and syllable[1:3] in diphthogs:
        print(True)
    # double consonant + vowel
    elif syllable[0:2] in double_consonants and syllable[2] in vowels:
        print(True)
    # double consonant + diphthog
    elif syllable[0:2] in double_consonants and syllable[2:4] in diphthogs:
        print(True)
    # vowel or diphthog
    elif syllable in vowels or syllable in diphthogs:
        print(True)
    # double pron
    elif syllable in double_pron:
        print(True)
    else:
        print(False)


def seperate_vowels_consonants(word:str) -> str:
    pass


def syllabify_token_while(string: str) -> None:
    index_char = 0

    while index_char <= len(string)-1:
        #print(index_char)
        # take index of this character
        char = string[index_char]
        # Consonants
        if char in consonants:
            # if consonant is not in the beginning or ending of the string
            if index_char > 0 and index_char < (len(string) - 1):
                # 1) look before and after the consonants to see if it is surrounded by vowels φτά/νω
                if string[index_char - 1] in vowels and string[index_char + 1] in vowels:
                    # seperate before consonant and renew string
                    string = string[: index_char] + " " + string[index_char:]
                    index_char += 1
                # 2) look if before it there is a vowel and after it there is another consonant
                elif string[index_char - 1] in vowels and string[index_char + 1] in consonants:
                    # if μ+π in the beginning of greek word don't seperate them
                    if string[index_char]+string[index_char+1] in cons_tuples_start_greek:
                        string = string[: index_char] + " " + string[index_char:]
                    else:
                    # if λ+τ or σ+σ not in the beginning of greek word seperate them
                        string = string[: index_char+1] + " " + string[index_char+1:]
                    index_char += 1
                # TODO do I need it?
                else:
                    index_char += 1
            # we need it for our first letter in order to move to the next one
            else:
                index_char += 1
        # Vowels
        else:
            index_char += 1
    print(string)

syllabify_token_while("αεροπλάνο")
syllabify_token_while("άστρο")
syllabify_token_while("φτάνω")
syllabify_token_while("αστρονομία")
syllabify_token_while("οχιά")
syllabify_token_while("ευτυχία")
syllabify_token_while("λάσπη")
syllabify_token_while("αμπούλα")
syllabify_token_while("βοήθα")
syllabify_token_while("βόηθα")
syllabify_token_while("φίλτατος")
syllabify_token_while("λολάκι")
syllabify_token_while("εκπτώσεις")
syllabify_token_while("στάτους")
syllabify_token_while("θάλασσα")
syllabify_token_while("ματς")
syllabify_token_while("κουτιού")
syllabify_token_while("ματιών")
syllabify_token_while("στράτα")
syllabify_token_while("εχθρός")
syllabify_token_while("αργαλειού")

