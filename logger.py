"""The module provides a Logger class that sets up and returns a logging object.
It has the following methods and attributes:

__init__(self, logger_name, log_file, log_level=logging.INFO, log_to_console=True):
Initializes the Logger object. logger_name is the name of the logger,
log_file is the name of the log file, log_level is the logging level (default is logging.INFO),
and log_to_console is a boolean indicating whether to log to console (default is True).
create_log_folder(self): Creates a folder to store the log files.
setup_logger(self, logger_name): Sets up the logger object and returns it.
logger: The logger object.
The module also includes a check to create a new folder called "LogFileFolder"
in the parent directory of the current working directory to store the log files. If the folder already exists,
it will not create a new one.

If the module is run as the main program,
it will create a Logger object with the name __name__ and the log file name logfile.log."""


import os
import logging


class Logger:
    def __init__(self, logger_name, log_file, log_level=logging.ERROR, log_to_console=True):
        self.log_file = log_file
        self.log_level = log_level
        self.log_to_console = log_to_console
        self.logger = None
        self.setup_logger(logger_name)

    def create_log_folder(self):
        """
        Create a folder to store the log files.

        :return: str: path of the created folder
        """
        logfile_folder = os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'LogFileFolder'))
        try:
            if not os.path.exists(logfile_folder):
                os.makedirs(logfile_folder)
                if self.logger:
                    self.logger.info(f"{logfile_folder} folder created successfully")
            return logfile_folder
        except Exception as e:
            if self.logger:
                self.logger.exception(f"{logfile_folder} did not created due to {str(e)}")

    def setup_logger(self, logger_name):
        """
        Set up a logger object.
        Args:
            logger_name (str): The name of the logger.

        Returns:
            logging.Logger: The logger object.
        """
        try:
            self.logger = logging.getLogger(logger_name)
            self.logger.setLevel(self.log_level)

            formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

            # create file handler
            file_path = os.path.join(self.create_log_folder(), self.log_file)
            file_handler = logging.FileHandler(file_path)
            file_handler.setLevel(self.log_level)
            file_handler.setFormatter(formatter)

            # create console handler if log_to_console is True
            console_handler = None
            if self.log_to_console:
                console_handler = logging.StreamHandler()
                console_handler.setLevel(logging.ERROR)
                console_handler.setFormatter(formatter)

            # add handlers to logger
            self.logger.addHandler(file_handler)
            if console_handler is not None:
                self.logger.addHandler(console_handler)

        except Exception as e:
            if self.logger:
                self.logger.exception(f"Failed to setup logger: {str(e)}")


if __name__ == '__main__':
    my_logger = Logger(__name__, 'logfile.log')
    my_logger.create_log_folder()
