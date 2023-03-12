"""
This module provides a class called DictionaryCreator that creates a
dictionary of positive and negative words by filtering out stop words.

It imports the following modules:
- MyLogger from logger module: A custom logging module that logs messages to a file and/or console.
- StopWords from stop_words_list module: A class that provides a list of stop words.
- word_tokenize from nltk module: A method that tokenizes text into words.
- PathHelper from path_helper module: A class that provides the path of the master dictionary.

This module defines the following:
- DictionaryCreator class: A class that provides methods to create a dictionary of positive and negative words.

Example:
- dict_creator = DictionaryCreator()
positive_dict = dict_creator.positive_dict()
negative_dict = dict_creator.negative_dict()
"""

from logger import Logger
from stop_words_list import StopWords
from nltk import word_tokenize
from path_helper import PathHelper


class DictionaryCreator:
    def __init__(self):
        self.logger = Logger(__name__, 'dictionary.log', log_to_console=True).logger
        self.Stop_Words = StopWords()
        self.Path_Helper = PathHelper()
        self.stop_word_list = self.Stop_Words.get_StopWords_List().lower()

    def positive_dict(self):
        """
        This method will create a dictionary of positive words by filtering out stop words
        """
        try:
            positive_word_path = self.Path_Helper.get_MasterDictionary_path('positive-words.txt')

            with open(positive_word_path) as f:
                positive_words = set(word_tokenize(f.read()))

            positive_dict = [w for w in positive_words if w not in self.stop_word_list]
            self.logger.info('Positive word Dictionary created successfully')
            return positive_dict
        except Exception as e:
            self.logger.exception(f'Error while creating positive word dictionary: {e}')

    def negative_dict(self):
        """
        This method will create a dictionary of negative words by filtering out stop words
        """
        try:
            negative_word_path = self.Path_Helper.get_MasterDictionary_path('negative-words.txt')

            with open(negative_word_path) as f:
                negative_words = set(word_tokenize(f.read()))

            negative_dict = [w for w in negative_words if w not in self.stop_word_list]
            self.logger.info('Negative word Dictionary created successfully')
            return negative_dict
        except Exception as e:
            self.logger.exception(f'Error while creating negative word dictionary: {e}')


if __name__ == '__main__':
    dict_creator = DictionaryCreator()
    positive_dict = dict_creator.positive_dict()
    negative_dict = dict_creator.negative_dict()
