"""The module provides a class 'StopWords' that retrieves and cleans stop words. It imports os, re, PathHelper class from 'path_helper' module, and MyLogger class from 'logger' module.

Usage:
- Initialize the StopWords class: stopwords = StopWords()
- Retrieve the cleaned stop words: stopwords.get_StopWords_List()

Methods:
- create_StopWords_list(): retrieves all the stop words from the 'StopWords' folder and returns them as a single string.
    Returns:
        str: A string containing all the stop words.

- get_StopWords_List(): cleans the stop words stored in the create_StopWords_list() method.
    Returns:
        str: A string containing the cleaned stop words.
"""


import os
import re
from path_helper import PathHelper
from logger import Logger


class StopWords:
    """
    A class that provides methods to retrieve and clean StopWords.
    """
    def __init__(self):
        try:
            self.logger = Logger(__name__, 'stop_words_list.log', log_to_console=True).logger
            self.file_path = PathHelper()
        except Exception as e:
            raise Exception(f"Failed to initialize StopWords: {str(e)}")

    def create_StopWords_list(self):
        """
        This method retrieves all the stop words from the 'StopWords' folder and returns them as a single string.

        Returns:
            str: A string containing all the stop words.
        """
        try:
            StopWords_file_path = self.file_path.get_StopWords_path()

            text = ""
            for stopwordfile in StopWords_file_path:
                with open(stopwordfile[0], "r") as f:
                    a = f.read()
                    text += a
                    self.logger.info(f"{stopwordfile[1]} file text content saved successfully")
            self.logger.info('All the words from StopWords folder is saved successfully in a string in text variable')
            return text.lower()
        except Exception as e:
            self.logger.error(f"Failed to create StopWords list: {str(e)}")
            return ""

    def get_StopWords_List(self):
        """
        This method cleans the stop words stored in the create_StopWords_list() method.

        Returns:
            str: A string containing the cleaned stop words.
        """
        try:
            text = self.create_StopWords_list()
            new_text = re.sub(r"Surnames.*\.last", "", text)
            pattern = re.compile(r'http[s]?:(\/)*([a-z.]+)*(\/[a-z]+)*(\/[A-z]+.?)([a-z]+.)([a-z]+)?')
            stop_words_list = re.sub(pattern, '', new_text)
            self.logger.info("StopWordsList created successfully")
            return stop_words_list
        except Exception as e:
            self.logger.error(f"Failed to retrieve cleaned StopWords list: {str(e)}")
            return ""


if __name__ == '__main__':
    stopwords = StopWords()
    print(stopwords.get_StopWords_List())
