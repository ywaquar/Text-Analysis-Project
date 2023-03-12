##Text Analysis Project
#Introduction
Welcome to the Text Analysis Project, developed by BlackOffer. This project performs text analysis on articles to compute variables such as sentiment scores, readability, word count, and personal pronouns. The project is divided into two parts: data extraction and data analysis. To understand the project, please refer to the objective.docx and Text Analysis.docx files. For instructions on how to use the code, check the Instruction.docx file.

#Dependencies
To run the project, you will need the following dependencies:
1) PyCharm or VSCode
2) Python Programming language
3) All the required libraries are included in the requirements.txt file, with version numbers specified.

#Contents
The repository includes the following files:

1) README.md: This file provides an introduction to the project and instructions for using the repository.
2) input.xlsx: This file contains a list of URLs to extract data from.
3) output Data Structure.xlsx: This file specifies the output format for the data analysis.
4) PythonFile: This folder contains the Python code for performing text analysis.
5) StopWords: This folder contains a list of stop words used for cleaning the text.
6) MasterDictionary: This folder contains a master dictionary of positive and negative words.
7) Obective.docx: The objective of this assignment is to extract textual data articles from the given URL and perform text analysis to compute variables that are       explained below.
8)Text Analysis.docx: Objective of this document is to explain methodology adopted to perform text analysis to drive sentimental opinion, sentiment scores,         readability, passive words, personal pronouns and etc.
9)Instruction.docx: This is an instruction file which explains how to use the code.

#How to Use
To analyze articles using this project, please follow these steps:
1) Download the all the files and folder.
2) Create a sperate 'PythonFile' folder where all the .py file will be present. This will be current working directory.
3) Ensure that the "input.xlsx" and "Output Data Structure.xlsx" should be in located in parent working directory, and the current working directory should be named "PythonFile where .py file are presents."
4) Create a Python environment with the required dependencies, including BeautifulSoup, nltk, Pandas, and Requests.
5) Open the terminal or command prompt and navigate to the project directory.
6) Run the "main.py" Python script to extract article text from URLs and save it in the text files with the URL_ID as their filename. Also, this script will perform
textual analysis on the extracted article text and compute the required variables.
7) The output will be saved in an Excel file named "output.xlsx" in the same directory as the input file.
8) Verify that the output file format matches the "Output Data Structure.xlsx" file provided.
9) A "textfile" folder will be created after the run of "main.py" python script to store all the extracted text content with the URL_ID as the base name.
10) A separate "LogfileFolder" will be created to store all the log files for each module.
11) Console handler and file handle is set to ERROR level. It can be changed from the logger module.

#Contact
If you have any questions or issues with the project, please contact us at:
LinkedIn: https://www.linkedin.com/in/pwaquar/
Gmail: ywaquar@gmail.com
