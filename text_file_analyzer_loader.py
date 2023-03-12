"""
This module contains the TextFileAnalyzerLoader class, which is used to load and analyze text files
and output the final data structure. It uses the MyLogger and TextFileAnalyzer classes from the logger and
text_file_analyzer modules, respectively. The module also imports pandas for DataFrame operations.

Class:
TextFileAnalyzerLoader:
A class to load and analyze text files and output the final data structure.

Methods:
init():
Initializes the TextFileAnalyzerLoader object.

load_files() -> pd.DataFrame:
Loads and analyzes text files, returning a pandas DataFrame.

load_data_structure() -> pd.DataFrame:
Loads the output data structure file and returns a pandas DataFrame.

merge_data(output_path: str) -> None:
Merges the output data structure DataFrame with the analyzed text files DataFrame and saves the final
data value file.

Parameters:
output_path : str
The path to save the final output file.

Returns:
None
"""

from logger import Logger
from text_file_analyzer import TextFileAnalyzer
import pandas as pd
import os


class TextFileAnalyzerLoader:
    """
    A class to load and analyze text files and output the final data structure.
    """

    def __init__(self):
        """
        Initializes the TextFileAnalyzerLoader object.
        """
        try:
            self.logger = Logger(__name__, 'text_file_analyzer_loader.log', log_to_console=True).logger
            self.text_file_analyzer = TextFileAnalyzer()
        except Exception as e:
            self.logger.error(f"An error occurred during initialization: {str(e)}")

    def load_files(self) -> pd.DataFrame:
        """
        Loads and analyzes text files, returning a pandas DataFrame.
        """
        try:
            text_file_data = self.text_file_analyzer.analyze_all_files()

            # importing text_file_data as DataFrame
            text_file_df = pd.DataFrame(text_file_data).T
            text_file_df = text_file_df.reset_index().rename(columns={"index": "URL_ID"})
            text_file_df["URL_ID"] = text_file_df["URL_ID"].astype("int64")
            return text_file_df

        except Exception as e:
            self.logger.error(f"An error occurred while loading and analyzing text files: {str(e)}")

    def load_data_structure(self) -> pd.DataFrame:
        """
        Loads the output data structure file and returns a pandas DataFrame.
        """
        filepath = os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'Output Data Structure.xlsx'))

        try:
            # Importing the Out Data Structure File
            output_data_df = pd.read_excel(filepath)

            # Taking only URL_ID and URL Column
            output_data_df = output_data_df.iloc[:, : 2]

            return output_data_df

        except Exception as e:
            self.logger.error(f"An error occurred while loading output data structure file: {str(e)}")

    def merge_data(self, output_path: str) -> None:
        """
        Merges the output data structure DataFrame with the analyzed text files DataFrame
        and saves the final data value file.

        Parameters
        ----------
        output_path : str
            The path to save the final output file.

        Returns
        -------
        None
        """
        try:
            output_data_df = self.load_data_structure()
            text_file_df = self.load_files()

            # Merging output_df and text_file_df
            final_df = pd.merge(output_data_df, text_file_df, on="URL_ID")

            # Saving the final data value file.
            final_df.to_excel(output_path, index=False)
            self.logger.info("Final output file saved successfully in the specified directory")
        except Exception as e:
            self.logger.error(f"An error occurred while merging data frames and saving the final output file: {str(e)}")


if __name__ == '__main__':
    output_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'output.xlsx'))
    df = TextFileAnalyzerLoader()
    df.merge_data(output_path)