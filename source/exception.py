#Used for exception handling
#STEP 1
import sys
from source.logger import logging
#error_detail will be present inside sys is shown in the line below
def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()#it will give 3 info, only 3rd is imp - which file, which line number will be stored in exc_tb
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message
    

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message
    

'''if __name__ == "__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e, sys)

it was just to check if our code is working or not
        '''
    


'''
- if __name__ == "__main__":
Ensures this block runs only when the script is executed directly, not when imported as a module.
- a = 1 / 0
Attempts to divide 1 by 0, which raises a ZeroDivisionError.
- except Exception as e:
Catches the error. Using Exception here means it will catch any exception, not just ZeroDivisionError.
- logging.info("Divide by Zero")
Logs an informational message to the configured log file/system, making it easier to trace what went wrong.
- raise CustomException(e, sys)
Re-raises the error as a custom-defined exception (likely a class you wrote elsewhere in your project).
- e is the original exception object.
- sys is passed in, probably to capture system-level details like traceback or environment info.

Purpose
- Demonstrates how to catch an error, log it, and then re-throw it in a controlled way using a custom exception class.
- This pattern is common in production code: you don’t just let raw Python errors bubble up—you wrap them in your own exception type for better debugging and consistency.


'''

'''
How e gets its value
- When Python executes a = 1 / 0, it raises a ZeroDivisionError.
- The except Exception as e: block catches that error.
- The variable e is automatically assigned to the exception object that was raised (ZeroDivisionError('division by zero')).
- So inside the except block, e is not empty — it holds the actual exception instance with details about what went wrong.

'''

'''
why this error is not shown in logging file?

'''