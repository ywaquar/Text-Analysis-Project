import os
import asyncio
import time
from web_content_extractor import WebContentExtractor
from text_file_analyzer_loader import TextFileAnalyzerLoader

if __name__ == '__main__':
    # file_path = "Input.xlsx"
    filepath = os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'Input.xlsx'))
    web_extractor = WebContentExtractor()
    asyncio.run(web_extractor.extract_all_pages(filepath))

    # wait for 5 seconds before running the next module
    time.sleep(10)

    df = TextFileAnalyzerLoader()
    df.merge_data()
