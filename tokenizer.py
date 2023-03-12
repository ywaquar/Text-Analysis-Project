from typing import List
from nltk.tokenize import word_tokenize, sent_tokenize
from logger import Logger


class Tokenizer:
    """
    A class that can be used to tokenize text into words and sentences.
    Methods:
    - tokenize_words(text: str) -> List[str]
    - tokenize_sentences(text: str) -> List[str]
    """

    def __init__(self, text):
        """
        Initializes the Tokenizer object.
        """
        self.text = text
        self.logger = Logger(__name__, 'tokenizer.log', log_to_console=True).logger

    def tokenize_words(self) -> List[str]:
        """
        Tokenizes the input text into a list of words.

        Args:
        - text (str): the text to be tokenized

        Returns:
        - List[str]: a list of tokenized words
        """
        try:
            # Use word_tokenize() to split the text into individual words
            words = word_tokenize(self.text)
            # Remove any words that are not alphabetical
            words = [word for word in words if word.isalpha()]
            self.logger.info("Successfully tokenized words from the text")
            return words
        except Exception as e:
            self.logger.error("Error occurred while tokenizing words: {}".format(e))
            raise Exception("Error occurred while tokenizing words: {}".format(e))

    def tokenize_sentences(self) -> List[str]:
        """
        Tokenizes the input text into a list of sentences.

        Args:
        - text (str): the text to be tokenized

        Returns:
        - List[str]: a list of tokenized sentences
        """
        try:
            # Use sent_tokenize() to split the text into individual sentences
            sentences = sent_tokenize(self.text)
            # Remove any leading/trailing whitespace from each sentence
            sentences = [sentence.strip() for sentence in sentences]
            self.logger.info("Successfully tokenized sentences from the text")
            return sentences
        except Exception as e:
            self.logger.error("Error occurred while tokenizing sentences: {}".format(e))
            raise Exception("Error occurred while tokenizing sentences: {}".format(e))
