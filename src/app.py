import argparse
from audio import Audio
from dictionary import Dictionary

__all__ = ['main']


def main():
    parser = argparse.ArgumentParser(description='Pronounce the given word')
    parser.add_argument('word', help='word to be pronounced', type=str)
    args = parser.parse_args()
    Audio(args.word).play()
    Dictionary(args.word).show()


if __name__ == '__main__':
    main()
