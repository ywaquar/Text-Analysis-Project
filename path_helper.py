"""
This module provides a Singleton class, 'PathHelper', that provides methods to retrieve file paths.

Classes:
    Singleton: A metaclass that creates a Singleton base class when called.

Methods:
    get_StopWords_path: Retrieves the file paths for all the StopWords files in the 'StopWords' directory.
    get_MasterDictionary_path: Retrieves the file path for a given file name in the 'MasterDictionary' directory.
    get_textfile_paths: Retrieves the file paths for all the files in the 'textfile' directory.
"""

from logger import Logger
import os


class Singleton(type):
    """
    A metaclass that creates a Singleton base class when called.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class PathHelper(metaclass=Singleton):
    """
    A class that provides methods to retrieve file paths.
    """

    def __init__(self):
        try:
            self.logger = Logger(__name__, 'path_helper.log', log_to_console=True).logger
            self.logger.info("PathHelper initialized successfully")
        except Exception as e:
            self.logger.error(f"Failed to initialize PathHelper: {str(e)}")

    def get_StopWords_path(self):
        """
        This method retrieves the file paths for all the StopWords files in the 'StopWords' directory.

        Returns:
            list: A list of tuples containing the file paths and filenames.
        """
        try:
            directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'StopWords'))
            StopWords_file_paths = []
            for filename in os.listdir(directory):
                filepath = os.path.join(directory, filename)
                StopWords_file_paths.append((filepath, filename))
            self.logger.info("StopWords file paths retrieved successfully")
            return StopWords_file_paths
        except Exception as e:
            self.logger.error(f"Failed to retrieve StopWords file paths: {str(e)}")
            return []

    def get_MasterDictionary_path(self, file_name):
        """
        This method retrieves the file path for a given file name in the 'MasterDictionary' directory.

        Args:
            file_name (str): The name of the file to retrieve, it can be positive-words or negative-words.

        Returns:
            str: The file path for the given file name in the 'MasterDictionary' directory.
        """
        try:
            file_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'MasterDictionary', file_name))
            self.logger.info(f"File path for {os.path.basename(file_name)} in MasterDictionary is {file_path}")
            return file_path
        except Exception as e:
            self.logger.error(
                f"Failed to retrieve file path for {os.path.basename(file_name)} in MasterDictionary: {str(e)}")
            return ""

    def get_textfile_paths(self):
        """
        This method retrieves the file paths for all the files in the 'textfile' directory.
        This textfile is created from the web_content_extractor.py module and
        contains the extracted text with URL_ID as its base name.

        Returns:
            list: A list of file paths.
        """
        try:
            directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'textfile'))
            textfile_filepath = []
            for filename in os.listdir(directory):
                filepath = os.path.join(directory, filename)
                if os.path.isfile(filepath):
                    textfile_filepath.append(filepath)
            self.logger.info("Text file paths retrieved successfully")
            return textfile_filepath
        except Exception as e:
            self.logger.error(f"Failed to retrieve text file paths: {str(e)}")
            return []


if __name__ == '__main__':
    path_helper = PathHelper()
    path_helper.get_StopWords_path()
