import argparse
from audio import Audio

__all__ = ['main']


def main():
    parser = argparse.ArgumentParser(description='Pronounce the given word')
    parser.add_argument('word', help='word to be pronounced', type=str)
    args = parser.parse_args()
    Audio(args.word).play()
