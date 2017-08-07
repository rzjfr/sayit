import os
import requests
from playsound import playsound
from fake_useragent import UserAgent


class Audio:
    """audio related parts"""

    def __init__(self, word, files_path='~/.sayit'):
        self.word = word + "__gb"
        self.user_agent = UserAgent().random  # Random user_agent for http calls
        self.files_path = os.path.expanduser(files_path)
        if not os.path.isdir(files_path):
            os.makedirs(files_path, exist_ok=True)

    def play(self):
        """ play the mp3 file of the word """
        file_path = self._get_file(self.word)
        if not os.path.exists(file_path):
            raise Exception("File cannot be found for {}.".format(self.word))
        playsound(file_path)

    def _get_file(self, word):
        """ download if not already downloaded """
        word_path = "{}/oxford/uk/{}/{}/{}".format(self.files_path, word[0],
                                                   word[0: 3], word[0: 5])
        file_path = "{}/{}.mp3".format(word_path, word)
        if not os.path.exists(file_path):
            os.makedirs(word_path, exist_ok=True)
            self._save_word(word, word_path)
        return file_path

    def _save_word(self, word, path):
        """ download and save the binary file to the given path """
        uri = self._create_uri(word)
        headers = {'User-Agent': self.user_agent}
        request = requests.get(uri, headers=headers)
        if request.status_code != 200:
            raise Exception("{} cannot be found on the server.".format(word))
        with open('{}/{}.mp3'.format(path, word), 'wb') as f:
            for chunk in request:
                f.write(chunk)
        return uri

    def _create_uri(self, word):
        """create oxford learner dictionary mp3 uri"""
        base = "http://www.oxfordlearnersdictionaries.com/media/english/uk_pron/"
        word_part = "{}/{}/{}/{}".format(word[0], word[0: 3], word[0: 5], word)
        end = "_1.mp3"  # this might end with _2 or _\d for other variations
        print(base + word_part + end)
        return base + word_part + end
