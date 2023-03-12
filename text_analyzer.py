
"""This module contains two classes to analyze the text data: TextAnalyzer and ReadabilityAnalyzer.

TextAnalyzer class contains four methods to analyze the sentiment of text data. These methods are:

positive_score: Calculates the number of positive words in the text.
negative_score: Calculates the number of negative words in the text.
polarity_score: Calculates the polarity score of the text.
subjectivity_score: Calculates the subjectivity score of the text.
ReadabilityAnalyzer class contains three methods to analyze the readability of text data. These methods are:

average_sentence_length: Calculates the average number of words per sentence in the text.
per_complex_words: Calculates the percentage of complex words in the text.
fog_index: Calculates the fog index of the text using the Gunning Fog Index formula.
This module depends on several external libraries: re, nltk.corpus, logger, dictionary, and tokenizer.
Before using this module, these dependencies must be installed."""

import re
from nltk.corpus import stopwords
from logger import Logger
from dictionary import DictionaryCreator


class TextAnalyzer:
    """
    SENTIMENTAL ANALYSIS:
    A class for analyzing the text data.
    """

    def __init__(self, tokenizer):
        """
        Initializes the TextAnalyzer object with the given text.

        Args:
        - text (str): The text to be analyzed.
        """
        self.tokenizer = tokenizer
        self.dictionary_creator = DictionaryCreator()
        self.logger = Logger(__name__, 'textanalyzer.log', log_to_console=True).logger
        self.positive_dict = self.dictionary_creator.positive_dict()
        self.negative_dict = self.dictionary_creator.negative_dict()

    """ 1) POSITIVE SCORE """
    def positive_score(self):
        """
        Positive Score:
        This score is calculated by assigning the value of +1 for each word,
        if found in the Positive Dictionary and then adding up all the values.

        Returns:
            positive_score (int): The number of positive words in the text.
        """
        words = self.tokenizer.tokenize_words()
        positive_score = sum([1 for word in words if word in self.positive_dict])
        self.logger.info("Positive score calculated")
        return positive_score

    """ 2) NEGATIVE SCORE """

    def negative_score(self):
        """
        Negative Score:
        This score is calculated by assigning the value of -1 for each word,
        if found in the Negative Dictionary and then adding up all the values.
        We multiply the score with -1 so that the score is a positive number.

        Returns:
            negative_score (int): The number of negative words in the text.
        """
        words = self.tokenizer.tokenize_words()
        negative_score = sum([1 for word in words if word in self.negative_dict])
        self.logger.info("Negative score calculated")
        return negative_score

    """ 3) POLARITY SCORE """

    def polarity_score(self):
        """
        Polarity Score:
        This is the score that determines,
        if a given text is positive or negative in nature.

        It is calculated by using the formula:
        Polarity Score = (Positive Score – Negative Score)/
                        ((Positive Score + Negative Score) + 0.000001)
        Returns:
            polarity_score (float): The polarity score of the text.
        """
        positive_score = self.positive_score()
        negative_score = self.negative_score()

        polarity_score = round((positive_score - negative_score) / (positive_score + negative_score + 0.000001), 2)
        return polarity_score

    """ 4) SUBJECTIVITY SCORE """

    def subjectivity_score(self):
        """
        Subjectivty Score:
        Calculates the subjectivity score of the text.
        This is the score that determines if a given text is objective or subjective.

        It is calculated by using the formula:
        Subjectivity Score = (Positive Score + Negative Score)/
        ((Total Words after cleaning) + 0.000001)

        Returns:
        - subjectivity_score (float): The subjectivity score of the text.
        """
        words = self.tokenizer.tokenize_words()
        positive_score = self.positive_score()
        negative_score = self.negative_score()
        subjectivity_score = round((positive_score + negative_score) / len(words), 2)
        return subjectivity_score


class ReadabilityAnalyzer:
    """
    ANALYSIS OF READABILITY:
    A class to analyze the readability of a given text.
    """

    def __init__(self, tokenizer):
        """
        INITIALIZER:
        Initializes an instance of ReadabilityAnalyzer with the given text.
        Args:
        text (str): The text to analyze.
        """
        self.tokenizer = tokenizer
        self.logger = Logger(__name__, 'textanalyzer.log', log_to_console=True).logger

    """ 5) AVERAGE SENTENCE LENGTH """

    def average_sentence_length(self):
        """
        Average Sentence Length:
        Calculates the average number of words per sentence in the text.
        Average Sentence Length = the number of words / the number of sentences

        Returns:
            float: The average number of words per sentence in the text.
        """

        words = self.tokenizer.tokenize_words()
        num_words = len(words)
        sentences = self.tokenizer.tokenize_sentences()
        num_sentences = len(sentences)
        avg_sentence_length = round(num_words / num_sentences, 2)
        return avg_sentence_length

    """ 6) PERCENTAGE OF COMPLEX WORD """

    def per_complex_words(self):
        """
        Percentage of Complex Word:

        Calculates the number of complex words in the text.
        Percentage of Complex words = the number of complex words / the number of words
        Returns:
            float: The number of complex words in the text.
        """
        """Extracting Complex Word Count from the method complex_word_count"""

        words = self.tokenizer.tokenize_words()
        complex_word_count = self.complex_word_count()
        per_complex_words = round(complex_word_count / len(words), 2)
        return per_complex_words

    """ 7) FOG INDEX """

    def fog_index(self):
        """
        Fog Index
        Calculates the fog index using the gunning fog index formula given below.
        Fog Index = 0.4 * (Average Sentence Length + Percentage of Complex words)

        Returns:
            float: Fog Index
        """
        avg_sentence_length = self.average_sentence_length()
        per_complex_words = self.per_complex_words()

        fog_index = 0.4 * (avg_sentence_length + per_complex_words)
        return fog_index

    """ 8) AVERAGE NUMBER OF WORDS PER SENTENCE """

    def average_words_per_sentence(self):
        """
        AVERAGE NUMBER OF WORDS PER SENTENCE:
        The formula for calculating is:
        Average Number of Words Per Sentence = the total number of words / the total number of sentences
        """
        words = self.tokenizer.tokenize_words()
        num_words = len(words)

        sentences = self.tokenizer.tokenize_sentences()
        num_sentences = len(sentences)

        avg_words_per_sentence = round(num_words / num_sentences, 2)
        return avg_words_per_sentence

    """ 9) COMPLEX WORD COUNT """

    def complex_word_count(self):

        """
        Complex Word Count:
        Complex words are words in the text that contain more than two syllables.

        Returns:
            float: The number of complex words in the text.
        """

        """Complex Word Count"""
        words = self.tokenizer.tokenize_words()
        complex_word_count = 0
        for word in words:
            syllables = len(re.findall('[aeiou]+', word.lower()))
            if len(word) >= 3 and syllables > 2:
                complex_word_count += 1
        return complex_word_count

    """ 10) WORD COUNT """

    def word_count(self):
        """
        Word Count:
        We count the total cleaned words present in the text by
        1.	removing the stop words (using stopwords class of nltk package).
        2.	removing any punctuations like ? ! , . from the word before counting.

        Returns:
            int: The number of words in the text, excluding stop words.
        """
        words = self.tokenizer.tokenize_words()

        # Extracting stop words of english from nltk package

        stop_words = set(stopwords.words('english'))
        words_filtered = [word for word in words if word.lower() not in stop_words]

        word_count = len(words_filtered)
        return word_count

    """ 11) SYLLABLE PER WORD """

    def syllable_per_word(self):

        """
        SYLLABLES COUNT PER WORD:
        We count the number of Syllables in each word of the text by counting the vowels present in each word.
        We also handle some exceptions like words ending with "es","ed" by not counting them as a syllable.

        Returns:
        syllables_word (int): The total number of syllables in the text.
        """

        words = self.tokenizer.tokenize_words()
        syllables_word = 0
        for word in words:
            pattern = re.compile(r'\b\w+(?:es|ed|e|[^aeiouy]le|[^aeiouy][aeiouy](?!$))+(?!\S)')
            syllables_word += len(pattern.findall(word.lower()))
        return syllables_word

    """ 12) PERSONAL PRONOUNS """

    def personal_pronoun(self):
        """
        PERSONAL PRONOUNS:
        To calculate Personal Pronouns mentioned in the text, we use regex to find
        the counts of the words - “I,” “we,” “my,” “ours,” and “us”. Special care is
        taken so that the country name US is not included in the list.
        Counts the number of Personal Pronouns I, we, my, our, ours and us, exculding the words US.

        Returns:
        Personal_pronouns (int): The total number of personal pronouns in the text.
        """
        """ Writing Pattern for pronouns using re module"""

        words = self.tokenizer.tokenize_words()
        text = ' '.join(words)
        pattern_pronouns = re.compile(r'\b(?:I|we|my|our|ours|us)\b', re.IGNORECASE)

        """Writing Patterns for US word """
        pattern_us = re.compile(r'\b(?:US)\b')

        """ Matching pronouns for the text data """
        matches_pronouns = pattern_pronouns.findall(text)

        """ Matching US words for the text data """
        matches_us = pattern_us.findall(text)

        """ Calculating personal pronouns """

        personal_pronoun = len(matches_pronouns) - len(matches_us)
        return personal_pronoun

    """ 13) AVERAGE WORD LENGTH """

    def avg_word_length(self):
        """
        Average Word Length :
        Average Word Length is calculated by the formula:
        Sum of the total number of characters in each word/Total number of words

        Return:
            avg_word_length (int): The average word length in the text.
        """

        words = self.tokenizer.tokenize_words()
        num_words = len(words)
        count_char = 0
        for word in words:
            count_char += len(word)

        avg_word_length = round(count_char / num_words, 2)
        return avg_word_length
