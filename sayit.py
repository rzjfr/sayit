#!/usr/bin/python3
# encoding: utf-8

import os
import requests
import argparse
from playsound import playsound
from fake_useragent import UserAgent

UA = UserAgent().random
DB = os.path.expanduser('~/.sayit')
if not os.path.isdir(DB):
    os.makedirs(DB, exist_ok=True)


def trim(word, char=3):
    """ trim word to character number """
    has_char = len(word)
    deficit = char - has_char
    if deficit > 0:
        return word + ''.join(["_" for i in range(0, deficit)])
    return word[0:char]


def create_uri(word):
    """create oxford learner dictionary mp3 uri"""
    base = "http://www.oxfordlearnersdictionaries.com/media/english/uk_pron/"
    word_part = "{}/{}/{}/{}".format(word[0], trim(word, 3), trim(word, 5), word)
    end = "__gb_1.mp3"
    return base + word_part + end


def save_word(word, path='/tmp'):
    """ download and save the binary file to the given path """
    uri = create_uri(word)

    headers = {'User-Agent': UA}
    request = requests.get(uri, headers=headers)

    if request.status_code != 200:
        raise Exception('Server does not know that!')

    with open('{}/{}.mp3'.format(path, word), 'wb') as f:
        for chunk in request:
            f.write(chunk)
    return uri


def get_word(word):
    """ download if not already downloaded """
    word_path = "{}/oxford/uk/{}/{}/{}".format(DB, word[0], trim(word, 3), trim(word, 5))
    file_path = "{}/{}.mp3".format(word_path, word)
    if not os.path.exists(file_path):
        os.makedirs(word_path, exist_ok=True)
        save_word(word, word_path)
    return file_path


def play_word(word):
    """ play the mp3 file of the word """
    file_path = get_word(word)

    if not os.path.exists(file_path):
        print("{} is not correct!".format(word))
        return None

    playsound(file_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pronounce the given word')
    parser.add_argument('word', help='word to be pronounced', type=str)
    args = parser.parse_args()
    play_word(args.word)
