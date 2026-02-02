#STEP 2
#A logger in Python is an object from the `logging` module that records messages (info, warnings, errors, etc.) to help track and debug program execution.
import logging 
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok = True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s -%(levelname)s - %(message)s",
    level = logging.INFO
)

'''if __name__ == "__main__":
    logging.info("Logging has started")##this is the lineno in the line 16

this was only to check if the code was running properly or not
    '''

'''
1. Imports
- logging: Python’s built-in logging library.
- os: For file path handling.
- datetime: To generate timestamped filenames.
2. LOG_FILE
- Creates a unique log filename based on the current date and time.
- Example: 02_02_2026_23_20_45.log.
3. logs_path
- Builds a path like .../logs/<timestamp>.log.
- ⚠️ Issue: This includes the file name, not just the folder.
4. os.makedirs(logs_path, exist_ok=True)
- Tries to create a directory named after the log file (e.g., .../logs/02_02_2026_23_20_45.log/).
- That’s incorrect—os.makedirs() should be called on the folder (logs), not the file path.
5. LOG_FILE_PATH
- Joins logs_path and LOG_FILE again, but since logs_path already includes the file name, this doubles it (e.g., .../logs/<timestamp>.log/<timestamp>.log).
- This will break logging.
6. logging.basicConfig(...)
- Configures logging to write messages into the file at LOG_FILE_PATH.
- Format includes timestamp, line number, logger name, log level, and message.
- Logging level is set to INFO, so it records info, warnings, errors, and critical messages.

 In short: the code is meant to set up logging into a timestamped file, but it mistakenly treats the file path 
 as a directory. Fixing the os.makedirs() call ensures logs are stored correctly.

'''