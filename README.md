[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# MODERN GREEK SYLLABIFICATION AND METRE DETECTION

## Author
- [Eirini Valkana](https://github.com/EiriniVal) 


The aim of this program is to syllabify sentences in Modern Greek based on the corresponding rules of 
syllabification and to detect the correct metre of a given poem written in Modern Greek (monotonic system).

## 1. Introduction

Syllabification is a complex process in Modern Greek since many rules apply at once. The rules for syllabification are the following:

- A consonant between two vowels is paired with the second vowel, e.g. ά-νω, πα-ρα-κα-λώ.
- Single or double consonants at the beginning or at the end of the word do not consist seperate syllables, e.g. σπά-ω.
- Identical consonants following one another are split, e.g. θά-λασ-σα.
- Two or more consonants between two vowels are syllabified with the second vowel, if there is a Greek word that starts with 
this combination of consonants, e.g. λά-σπη (because in Greek there are words that start with "σπ" like "σπάω").
- Two or more consonants between two vowels are split after the first consonant if there is no Greek word that starts with this combination. 
The first consonant is syllabified with the previous vowel and the remaining ones are syllabified with the following vowel, e.g. άν-θρω-πος 
(because in Greek there are no words that start with "νθρ").
- All dipthongs are treated as a single vowel, e.g. αί-μα, ιε-ρά.


Syllabification is critical for metre detection in Modern Greek. This is why, based on syllabification, the program searches for sequences 
of stressed and unstressed syllables in each verse of a poem and assigns to each verse the metre with the highest score between the five types mentioned below. 
The score for each metre is defined as the ratio of the number of occurences of the corresponding metric pattern (e.g. unstressed + stressed for Iambic) to the 
total number of groups in the verse. After the program has parsed all the verses and has assigned to them a specific metre, the most frequent metre, verse-wise, 
is chosen as the poem's metre.

At this point, it should be noted that a perfect grammatical syllabification is not always sufficient for detecting the correct metre. There are cases where 
a poem is read with a rhythm which does not follow the written stress. Similarly, there are also instances of synizesis in the verse. 
Thus, it is expected that the program will not deduce the correct metre of every verse, as it is based exclusively on the grammatical stress. 

The metres in Modern Greek are defined by the following patterns:

Iambic: unstressed + stressed 
Trochaic: stressed + unstressed 
Anapaest: unstressed + unstressed + stressed
Dactyl: stressed + unstressed + unstressed 
Messotonos: unstressed + stressed + unstressed 


## 2. Usage

The program can be used through the terminal. A poem file of type ".txt" can be used as infile.
To run the program you can use as input files the poems that exist in the "poems/" folder. 

There are different flags for different processing types:

**'--print', '-p': if present, it prints the verses**

**'--poem_metre': if present, it prints the metre detected for the poem**

**'--verse_metre': if present, it prints the metre detected for each verse**

**'--verse_score': if present, it prints the metre scores for each verse**

**'--syllables': if present, it prints each verse in syllables**


Input:

```
 python main.py poems\anapaest\anapaest_poem_1 --syllables 
```
*Note: poems\anapaest\anapaest_poem_1 is the path to the poem that will be processed.*

Output: 

```
['του', 'μα', 'γιού', 'βρο', 'χε', 'ρή', 'κυ', 'ρια', 'κή']

['και', 'οι', 'νύμ', 'φες', 'α', 'ντά', 'μα', 'χο', 'ρεύ', 'ουν']

['σαν', 'ιέ', 'ρειες', 'μια', 'χα', 'ραυ', 'γή']

['με', 'σπον', 'δές', 'τη', 'θε', 'ά', 'τους', 'λα', 'τρεύ', 'ουν.']

['χρω', 'μα', 'τί', 'ζο', 'ντας', 'τό', 'ξα', 'ου', 'ρά', 'νια']

['στη', 'θε', 'ά', 'τους', 'ω', 'δές', 'α', 'πευ', 'θύ', 'νουν']

['δι', 'ψα', 'σμέ', 'νες', 'την', 'ά', 'νοι', 'ξη', 'γεύ', 'ο', 'νται']

['και', 'το', 'νέ', 'κταρ', 'του', 'έ', 'ρω', 'τα', 'πί', 'νουν.']
```



## 3. Data

The data used for this project are modern Greek poems (monotonic system) for all different types of metres.
The directory "verses_test_metre/" and the text file "verses_test_syllabification.txt" are used automatically in the unittests. 


## 4. References

- https://www.arisgiavris.gr/glossa.php
- https://eclass.uoa.gr/modules/document/file.php/FRL253/%CE%9A%CE%95%CE%99%CE%9C%CE%95%CE%9D%CE%91%20%CE%98%CE%95%CE%A9%CE%A1%CE%99%CE%91%CE%A3%20%CE%9A%CE%91%CE%99%20%CE%9C%CE%95%CE%98%CE%9F%CE%94%CE%9F%CE%A5/%CE%A3%CE%91%CE%A1%CE%91%CE%9B%CE%97%CE%A3%20%CE%9D%CE%B5%CE%BF%CE%B5%CE%BB%CE%BB%CE%B7%CE%BD%CE%B9%CE%BA%CE%B7%20%CE%BC%CE%B5%CF%84%CF%81%CE%B9%CE%BA%CE%AE.pdf
- https://www.tug.org/TUGboat/tb25-0/filippou.pdf
