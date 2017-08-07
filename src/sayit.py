import enchant
import argparse
from sys import exit
from stats import Stats
from audio import Audio
from dictionary import Dictionary

__all__ = ['main']


def spell_suggestion(word):
    dictionary = enchant.Dict("en_GB")
    if not dictionary.check(word):
        print("{} seems to be not a correct word.".format(word))
        print("Is it possible that you meant any of these:")
        print(' • '.join(dictionary.suggest(word)))
        exit(2)


def main():
    parser = argparse.ArgumentParser(description='Pronounce the given word')
    parser.add_argument('word', help='word to be pronounced', type=str)
    args = parser.parse_args()
    spell_suggestion(args.word)   # Stop the app if spell is incorrect
    Audio(args.word).play()       # Play the audio
    Dictionary(args.word).show()  # Show the definition
    Stats(args.word).add()        # Add the stats and show


if __name__ == '__main__':
    main()
