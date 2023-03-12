"""
Module to extract the content of web pages from a list of URLs provided in an Excel file.
The module uses asyncio to concurrently fetch and extract the content of the web pages,
and stores the extracted content in individual text files in a specified folder.

Dependencies:
- pandas
- os
- re
- bs4 (BeautifulSoup)
- urllib.request
- logger

Usage:
1. Place the URLs to extract in an Excel file with the following columns:
   - URL_ID: unique identifier for each URL
   - URL: the URL to extract content from
2. Specify the path to the Excel file in the import_excel_file function.
3. Run the script.

Output:
The module will create a folder named 'textfile' in the current working directory, and store
the extracted content of each URL in a separate text file named after the URL_ID in the 'textfile' folder.

Example:
    from web_content_extractor import WebContentExtractor

    # Create an instance of the WebContentExtractor class
    wce = WebContentExtractor()

    # Import the URLs from an Excel file
    url = wce.import_excel_file("input.xlsx")

    # Extract the content of the web pages
    wce.extract_page_content(url["URL_ID"], url["URL"])

"""
import pandas as pd
import re
from bs4 import BeautifulSoup as bs
import asyncio
import os
import aiohttp
from logger import Logger


class WebContentExtractor:
    """
    A class for extracting the content of web pages from a list of URLs provided in an Excel file.

    """

    def __init__(self):
        """
        Initialize the WebContentExtractor class by setting up a logger, importing the input file,
        and creating a folder to store the extracted text files.
        """
        self.logger = Logger(__name__, 'web_content_extractor.log', log_to_console=True).logger
        # self.create_folder()

    def import_excel_file(self, filepath):
        """
        Import an Excel file containing the URLs to extract.

        :param filepath: the path to the Excel file containing the URLs,
            i.e. the location of Input.xlsx

        :return: a pandas DataFrame object containing the URL_ID and URL columns
        """
        try:
            input_file = pd.read_excel(filepath)
            self.logger.info(f"{filepath} imported successfully")
            return input_file
        except Exception as e:
            self.logger.error(f"Error reading {filepath}: {e}")
            return None

    async def fetch_url(self, url_link):
        async with aiohttp.ClientSession() as session:
            async with session.get(url_link) as response:
                response_text = await response.text()
                return response_text

    async def extract_page_content(self, url_id, url_link):
        """
        Extract the content of a web page.

        :param url_id: the unique identifier for the URL
        :param url_link: the URL to extract content from

        :return: None
        """
        page_html = await self.fetch_url(url_link)
        page_soup = bs(page_html, 'html.parser')
        self.logger.info(f'page content of URL_ID {url_id} is souped successfully ')

        try:
            page_title = page_soup.title.string.split('-')[0].strip()
            page_content = page_soup.find("div", {"class": "td-post-content"}).get_text()
            page_content = re.sub(r'^\s+|\s+$', '', page_content)
            page_content = re.sub(r'(?s)^(.*\n)(Blackcoffer.*)$', r'\1', page_content)
            self.create_text_file(url_id, f"{page_title}\n\n{page_content}")
            self.logger.info(f"URL_ID {url_id} content saved successfully ")

        except Exception as e:
            page_title = page_soup.title.string.split('-')[0].strip()
            page_sub_title = page_soup.find('div', {'class': 'td-404-sub-title'}).text.strip()
            page_sub_sub_title = page_soup.find('div', {'class': 'td-404-sub-sub-title'}).get_text().strip()
            self.create_text_file(url_id, f"{page_title}\n{page_sub_title}\n{page_sub_sub_title}")
            self.logger.error(
                f"URL_ID {url_id} url page is not found but Error text is saved in the text file {url_id}.txt {e}")

    async def extract_all_pages(self, filepath):
        """
        Extract the content of all web pages listed in the input Excel file concurrently.

        :param filepath: the path to the Excel file containing the URLs

        :return: None
        """
        try:
            input_file = self.import_excel_file(filepath)
            url_id_list = input_file["URL_ID"]
            url_link_list = input_file["URL"]
            tasks = [asyncio.create_task(self.extract_page_content(url_id, url_link))
                     for url_id, url_link in zip(url_id_list, url_link_list)]
            self.logger.info('All task extracted successfully')
            await asyncio.gather(*tasks)

        except Exception as e:
            self.logger.error(f"Error in extracting all pages: {e}")

    def create_folder(self):

        """
        Create a folder to store the extracted text files. the folder is created in parent directory.
        :return: None
        """
        textfile_folder = os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'textfile'))
        # textfile_folder = os.path.join(os.getcwd(), "textfile")

        try:
            if not os.path.exists(textfile_folder):
                os.makedirs(textfile_folder)
                self.logger.info(f"{textfile_folder} folder created successfully")
            return textfile_folder
        except:
            self.logger.exception(f"{textfile_folder} did not created")

    def create_text_file(self, url_id, content):
        """
        Create a text file containing the extracted content.

        :param url_id: the unique identifier for the URL
        :param content: the extracted content to store in the text file

        :return: None
        """

        textfile_folder = self.create_folder()

        try:
            with open(os.path.join(textfile_folder, f"{url_id}"), "w", encoding="utf-8") as file:
                file.write(content)
            self.logger.info(f"URL_ID {url_id} Page content stored in {url_id}.txt file successfully")
        except Exception as e:
            self.logger.error(f"URL_ID {url_id} Error in encoding the file", e)


if __name__ == '__main__':
    # file_path = "Input.xlsx"
    filepath = os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'Input.xlsx'))
    web_extractor = WebContentExtractor()
    asyncio.run(web_extractor.extract_all_pages(filepath))
