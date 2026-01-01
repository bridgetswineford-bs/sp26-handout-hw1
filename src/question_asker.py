"""
Functions to ask the user questions to determine their housing priority.
"""


def ask_class_year() -> int:
    """Ask the student for their class year and return it as int.
    
    Requirements based on tests:
    - Prompt for class year (1=Freshman, 2=Sophomore, 3=Junior, 4=Senior)
    - Only accept integers 1-4
    - Handle invalid input gracefully (keep asking until valid)
    - Return the class year as an integer
    
    Your implementation should:
    1. Display a clear prompt
    2. Get user input
    3. Validate input (must be 1, 2, 3, or 4)
    4. Handle invalid input by asking again
    5. Return the valid integer
    """


def ask_graduation_status() -> bool:
    """Ask if the student is graduating this semester.
    
    Requirements based on tests:
    - Prompt: "Are you graduating this semester? (y/n)"
    - Accept 'y', 'Y', 'n', 'N'
    - Return True for yes, False for no
    - Handle invalid input gracefully (keep asking until valid)
    
    NOTE: When calling this function from main.py, it should ONLY be 
    called for seniors (class year 4)
    
    Your implementation should:
    1. Display a clear prompt
    2. Get user input
    3. Validate input (must be y/Y/n/N)
    4. Handle invalid input by asking again
    5. Return True for y/Y, False for n/N
    """


def ask_credits_earned() -> int:
    """Ask for credits earned and return as int.
    
    Requirements based on tests:
    - Prompt: "How many credits have you earned?"
    - Accept any non-negative integer (0 or higher)
    - Handle invalid input gracefully (non-numbers, negative numbers)
    - Return the valid integer
    
    Your implementation should:
    1. Display a clear prompt
    2. Get user input
    3. Validate input (must be non-negative integer)
    4. Handle invalid input by asking again
    5. Return the valid integer
    """


def ask_additional_questions() -> dict[str, bool]:
    """Ask at least two yes/no questions and return a dict of responses.
    
    Requirements based on tests:
    - Ask exactly 2 additional yes/no questions
    - Accept 'y', 'Y', 'n', 'N' for each question
    - Handle invalid input gracefully for each question
    - Return a dictionary with descriptive keys and boolean values
    
    Example questions you might ask:
    - "Are you older than 23?" (key: 'old23')
    - "Are you in the honors program?" (key: 'honors')
    - "Are you a student athlete?" (key: 'athlete')
    - "Do you have work-study?" (key: 'work_study')
    
    Choose your own questions, but make sure your test keys match!
    
    Your implementation should:
    1. Ask your first question with clear prompt
    2. Validate input (y/Y/n/N)
    3. Ask your second question with clear prompt
    4. Validate input (y/Y/n/N)
    5. Handle invalid input for both questions
    6. Return dict with 2 keys and boolean values
    
    Example structure:
    return {
        'your_first_key': boolean_result_1,
        'your_second_key': boolean_result_2 
        }
    """
