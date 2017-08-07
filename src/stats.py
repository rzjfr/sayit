import os
import pickle


class Stats:
    """ stats of usage """

    def __init__(self, word, files_path='~/.sayit'):
        self.word = word
        self.files_path = os.path.expanduser(files_path)
        self.file_path = self.files_path + '/stats'
        if not os.path.isdir(files_path):
            os.makedirs(files_path, exist_ok=True)
        try:
            with open(self.file_path, 'rb') as stats_file:
                self.stats = pickle.load(stats_file)
        except FileNotFoundError:
            self.stats = {}

    def show(self):
        print("\nTimes {} has been looked: {}".format(self.word,
                                                      self.stats.get(self.word, 0)))

    def add(self, show=True):
        self.stats[self.word] = self.stats.get(self.word, 0) + 1
        with open(self.file_path, 'wb') as stats_file:
            pickle.dump(self.stats, stats_file)
        if show:
            self.show()
