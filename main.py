import metre_detector as met
import syllabifier as syl
import argparse
from collections import Counter


def create_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser('aa',
                                     description='A commandline tool for syllabification and metre analysis of Modern '
                                                 'Greek verses.')
    parser.add_argument('poem_file',
                        help='a txt file containing a Modern Greek poem')
    parser.add_argument('--print', '-p',
                        help='if present, it prints the verses',
                        action='store_true')
    parser.add_argument('--poem_metre',
                        help='if present, it prints the metre detected for the poem',
                        action='store_true')
    parser.add_argument('--verse_metre',
                        help='if present, it prints the metre detected for each verse',
                        action='store_true')
    parser.add_argument('--verse_score',
                        help='if present, it prints the metre scores for each verse',
                        action='store_true')
    parser.add_argument('--syllables',
                        help='if present, it prints each verse in syllables',
                        action='store_true')
    return parser


def main():
    parser = create_argument_parser()
    args = parser.parse_args()
    metre_verse_list = []
    for elem in list(met.analyze_poem(args.poem_file)):
        verse_metre = elem[3]
        metre_verse_list.append(verse_metre)
        if args.syllables:
            print(syl.syllabify_verse(elem[0]))
        if args.print:
            print(elem[0])
        if args.verse_metre:
            print(f"The metre of verse {elem[1]} is: {verse_metre}")
        if args.verse_score:
            print(f"Metre scores of verse {elem[1]}:")
            for key, value in elem[2].items():
                print(key, ":", value)
    poem_metre = Counter(metre_verse_list).most_common(1)[0][0]
    if args.poem_metre:
        print(f"The poem's metre is: {poem_metre}")


if __name__ == '__main__':
    main()
