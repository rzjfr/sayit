#!/usr/bin python
# encoding: utf-8

from sys import argv

#http://www.oxfordlearnersdictionaries.com/definition/english/extraordinary
#http://www.oxfordlearnersdictionaries.com/media/english/uk_pron/c/cus/custo/customize__gb_1.mp3
#http://dictionary.cambridge.org/media/english/uk_pron/u/uke/ukext/ukextra014.mp3

#TODO: these have us and ogg versions as well

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

if __name__ == '__main__':
    print(create_uri(argv[1]))
