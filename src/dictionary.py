import os
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class Dictionary:
    """audio related parts"""

    def __init__(self, word, files_path='~/.sayit'):
        self.word = word
        self.user_agent = UserAgent().random  # Random user_agent for http calls
        self.files_path = os.path.expanduser(files_path)
        if not os.path.isdir(files_path):
            os.makedirs(files_path, exist_ok=True)

    def show(self):
        """ who the definition part of the word """
        file_path = self._get_file(self.word)
        if not os.path.exists(file_path):
            raise Exception("File cannot be found for {}.".format(self.word))
        with open(file_path, 'r') as html:
            soup = BeautifulSoup(html, 'html.parser')
            # Phonetics
            phonetics = soup.find('div', class_="phons_br")
            if phonetics:
                print(phonetics.get_text())
            # Origin
            origin = soup.find('span', unbox="wordorigin")
            if origin:
                print(origin.get_text(" "))
            # Definitions
            senses = soup.find('ol', class_='senses_multiple')
            if senses:
                self._print_definitions(senses)
            # Idioms
            idioms = soup.find_all('span', class_='idm-g')
            if idioms:
                self._print_idioms(idioms)

    def _get_file(self, word):
        """ download if not already downloaded """
        word_audio = word + "__gb"  # to save the file in audio sharded format
        word_path = "{}/oxford/uk/{}/{}/{}".format(self.files_path,
                                                   word_audio[0],
                                                   word_audio[0: 3],
                                                   word_audio[0: 5])
        file_path = "{}/{}.html".format(word_path, word)
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
        with open('{}/{}.html'.format(path, word), 'wb') as f:
            for chunk in request:
                f.write(chunk)
        return uri

    def _create_uri(self, word):
        """create oxford learner dictionary mp3 uri"""
        base = "https://www.oxfordlearnersdictionaries.com/definition/english/"
        return base + word

    def _print_definitions(self, html):
        """prints definitions"""
        for i, sense in enumerate(html):
            if str(sense) != " ":
                meaning = sense.find('span', class_='def')
                if meaning:
                    meaning = meaning.text
                    title = sense.find('span', class_='cf')
                    label = sense.find('span', class_='dtxt')
                    labels = sense.find('span', class_='labels')
                    if label:
                        meaning = "({}) {}".format(label.text, meaning)
                    if labels:
                        meaning = "{} {}".format(labels.text, meaning)
                    if title:
                        meaning = "{}: {}".format(title.text, meaning)
                    print("{}. {}".format(i+1, meaning))
                examples = [item.text for item in sense.find_all('li', class_="") if item]
                for example in examples:
                    if example:
                        print("  • {}".format(example))

    def _print_idioms(self, html):
        """prints idioms"""
        print("\nIdioms:")
        for idiom in html:
            if idiom:
                print("  ⦾ {}".format(idiom.find('div').get_text(" ", strip=True)))
                label = idiom.find('span', class_='labels')
                description = idiom.find('span', class_='def').get_text(" ", strip=True)
                if label:
                    description = "{} {}".format(label.text, description)
                print("    {}".format(description))
                for example in idiom.find_all('span', class_='x'):
                    print("    . {}".format(example.text))
