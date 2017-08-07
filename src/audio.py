import os
import requests
from playsound import playsound
from fake_useragent import UserAgent


class Audio:
    """audio related parts"""

    def __init__(self, word, files_path='~/.sayit'):
        self.word = word
        self.user_agent = UserAgent().random  # Random user_agent for http calls
        self.files_path = os.path.expanduser(files_path)
        if not os.path.isdir(files_path):
            os.makedirs(files_path, exist_ok=True)

    def play(self):
        """ play the mp3 file of the word """
        file_path = self.get_file(self.word)
        if not os.path.exists(file_path):
            raise Exception("File cannot be found for {}.".format(self.word))
        playsound(file_path)

    def get_file(self, word):
        """ download if not already downloaded """
        word_path = "{}/oxford/uk/{}/{}/{}".format(self.files_path, word[0],
                                                   self.trim_word(word, 3),
                                                   self.trim_word(word, 5))
        file_path = "{}/{}.mp3".format(word_path, word)
        if not os.path.exists(file_path):
            os.makedirs(word_path, exist_ok=True)
            self.save_word(word, word_path)
        return file_path

    def save_word(self, word, path):
        """ download and save the binary file to the given path """
        uri = self.create_uri(word)
        headers = {'User-Agent': self.user_agent}
        request = requests.get(uri, headers=headers)
        if request.status_code != 200:
            raise Exception("{} cannot be found on the server.".format(word))
        with open('{}/{}.mp3'.format(path, word), 'wb') as f:
            for chunk in request:
                f.write(chunk)
        return uri

    def trim_word(self, word, trim_chars=3):
        """ trim word to character number for sharding """
        word_chars = len(word)
        remaining_chars = trim_chars - word_chars
        if remaining_chars > 0:
            return word + ''.join(["_" for i in range(0, remaining_chars)])
        return word[0:trim_chars]

    def create_uri(self, word):
        """create oxford learner dictionary mp3 uri"""
        base = "http://www.oxfordlearnersdictionaries.com/media/english/uk_pron/"
        word_part = "{}/{}/{}/{}".format(word[0], self.trim_word(word, 3),
                                         self.trim_word(word, 5), word)
        end = "__gb_1.mp3"
        return base + word_part + end
