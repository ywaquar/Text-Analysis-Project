"""
This module provides a TextFileAnalyzer class that analyzes text files using the TextAnalyzer and ReadabilityAnalyzer
classes from the text_analysis module and the Tokenizer class from the tokenizer module. The class also utilizes the
PathHelper class to obtain the paths of the text files, and the MyLogger class to log analysis results.

Classes:
    - TextFileAnalyzer: Analyzes text files and returns a dictionary of results containing various text and readability
                        analysis measures.

Functions:
    - None

Usage:
    - To analyze a collection of text files, create an instance of TextFileAnalyzer and call the analyze_files method.
      The method returns a dictionary of analysis results containing various text and readability measures.
"""

import os
from text_analyzer import TextAnalyzer, ReadabilityAnalyzer
from path_helper import PathHelper
from logger import Logger
from tokenizer import Tokenizer


class TextFileAnalyzer:
    """
    This class is responsible for analyzing text files using TextAnalyzer and ReadabilityAnalyzer classes
    from the text_analysis module, and Tokenizer class from the tokenizer module. It also uses the PathHelper
    class to get the paths of the text files.
    """

    def __init__(self):
        """
        Initializes a TextFileAnalyzer object and sets up logger and helper objects.
        """
        self.path_helper = PathHelper()
        self.logger = Logger(__name__, 'text_file_analyzer.log', log_to_console=True).logger
        self.t_analyzer = None
        self.r_analyzer = None
        self.tokenizer = Tokenizer('')

    def analyze_text_variables(self):
        """
        Analyzes the given text using the TextAnalyzer.

        Args:
            text (str): The text to analyze.

        Returns:
            A dictionary containing various text analysis measures.
        """
        if not self.t_analyzer:
            self.t_analyzer = TextAnalyzer(self.tokenizer)
        else:
            self.t_analyzer.tokenizer = self.tokenizer
        variables = {
            'POSITIVE SCORE': self.t_analyzer.positive_score(),
            'NEGATIVE SCORE': self.t_analyzer.negative_score(),
            'POLARITY SCORE': self.t_analyzer.polarity_score(),
            'SUBJECTIVITY SCORE': self.t_analyzer.subjectivity_score()
        }

        return variables

    def analyze_readability_variables(self):
        """
        Analyzes the readability of the given text using the ReadabilityAnalyzer.

        Args:
            text (str): The text to analyze.

        Returns:
            A dictionary containing various readability measures.
        """
        if not self.r_analyzer:
            self.r_analyzer = ReadabilityAnalyzer(self.tokenizer)
        else:
            self.r_analyzer.tokenizer = self.tokenizer

        variables = {
            'AVG SENTENCE LENGTH': self.r_analyzer.average_sentence_length(),
            'PERCENTAGE OF COMPLEX WORDS': self.r_analyzer.per_complex_words(),
            'FOG INDEX': self.r_analyzer.fog_index(),
            'AVG NUMBER OF WORDS PER SENTENCE': self.r_analyzer.average_words_per_sentence(),
            'COMPLEX WORD COUNT': self.r_analyzer.complex_word_count(),
            'WORD COUNT': self.r_analyzer.word_count(),
            'SYLLABLE PER WORD': self.r_analyzer.syllable_per_word(),
            'PERSONAL PRONOUNS': self.r_analyzer.personal_pronoun(),
            'AVG WORD LENGTH': self.r_analyzer.avg_word_length()
        }

        return variables

    def analyze_single_file(self, file_path):
        """
        Analyzes text files and returns a dictionary of results containing various text and readability analysis measures.

        Args:
            None

        Returns:
            results (dict): A dictionary containing various text and readability analysis measures for each text file.
        """

        with open(file_path, 'r', encoding="utf-8") as f:
            text = f.read().lower()
            self.tokenizer.text = text

            text_variables = self.analyze_text_variables()
            readability_variables = self.analyze_readability_variables()

            variables = {**text_variables, **readability_variables}
            filename = os.path.splitext(os.path.basename(file_path))[0]
            results = {filename: variables}
            self.logger.info(f"Text file {filename} was analyzed successfully.")
        return results

    def analyze_all_files(self):
        file_paths = self.path_helper.get_textfile_paths()
        results = {}
        for path in file_paths:
            result = self.analyze_single_file(path)
            results.update(result)
        self.logger.info("All text files were analyzed successfully.")
        return results


if __name__ == "__main__":
    analyzer = TextFileAnalyzer()
    print(analyzer.analyze_all_files())
