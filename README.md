
# HW 1: Housing Priority Calculator

> [!CAUTION]
> Make sure the name of this repository / directory has your GitHub username in it. Otherwise, you will not be able to submit any work. You can find the repository with your GitHub username through Pawtograder.

## Due Wednesday, January 21 at 6pm Pacific / 9pm Eastern

## Learning Outcomes
- [Submitting code to GitHub](https://neu-pdi.github.io/cs2100-public-resources/lecture-notes/next/l1-intro-python1#vscode-pawtograder-and-github)
- [Practice designing functions with type annotations, documentation, and tests](https://neu-pdi.github.io/cs2100-public-resources/lecture-notes/next/l1-intro-python1#functions-including-documentation-and-tests)
- [Testing functions that print and take user input](https://neu-pdi.github.io/cs2100-public-resources/lecture-notes/next/l2-python2#read-and-write-data-from-user-input-and-text-files)
- [Using dictionaries](https://neu-pdi.github.io/cs2100-public-resources/lecture-notes/next/l3-python3#data-structures-list-set-and-dict)

## Overview
Welcome to your first programming assignment of the semester! In this assignment you will be building a housing "priority score" engine in Python that decides who gets the first pick of campus housing. You'll dive into human-centered design—chatting with users, uncovering their needs, and iterating on your plan—while mastering Python basics: grabbing input, crafting if/elif/else logic, performing arithmetic, and tallying up points.

This assignment is based on this [Nifty Assignment](http://nifty.stanford.edu/2020/peck-decision-makers/).

## NOTE: Open the entire folder in VSCode, not individual files
In VSCode, open this assignment through `File` > `Open Folder...` > open the entire repo. Do not open individual files. Opening the entire folder makes it so that:
- the `import` statements can find the pages
- Python runs the code "from" the right location
- the `.vscode` settings automatically get applied
- the terminal opens at the right location

In general, open the entire folder for all assignments in this course, rather than individual files.


### files in `src`:
1. **`question_asker.py`**
   * `ask_class_year()`
   * `ask_graduation_status()`
   * `ask_credits_earned()`
   * `ask_additional_questions()`

2. **`priority_calculator.py`**
   * `points_for_class_year(year)`
   * `points_for_graduation(is_graduating)`
   * `points_for_credits(credits)`
   * `points_for_additional_questions(responses)`
   * `calculate_total_score(year, is_graduating, credits, additional_responses)`

3. **`main.py`**
   * `main()`

## Your Tasks:

### Part 1: Understand the purpose of each function.
Read through the files in the `src` directory and understand how they are expected to work together.

Do not implement these functions yet, but think about how the different functions interact with each other.

Note: In the handout files, if you have pylint setup correctly, vscode will show you some errors/informational comments about unused imports or unused variables or unnecessary pass statements. You may ignore these for now as they will go away once you start completing the assigment. Do not get rid of the imports or any starter code assuming it is unused--you will need it later! 


### Part 2: Design Your Scoring System

Based on their inputs to the questions asked, students receive a score that is used in the system to provide housing. A higher scores means their housing needs are more prioritized. Your tasks are to 

**Decide** on your priority-based scoring system for each component:
 - How many points for each class year (1-4)?
 - How many points for graduating vs. not graduating?
 - How many points per credit hour?
 - What additional questions will you ask and how many points each?
   - Our autograder is set to allow up to five additional questions. If you have a compelling reason to ask more than five additional questions, please reach out to an instructor.

Additional questions must all be yes/no questions.

You are free to choose your own scoring system, but you will need to be able to explain why you made those choices. 

### Part 3: Complete the `test` files in the `tests` directory
 
**Before implementing any functions**, complete all the TODO items in the test files:

Before implementing the functions, write tests that specify how they are expected to behave. This is a good practice to follow in general, not just for this assignment, because it forces you to think about different inputs and edge cases independently from how *your* particular implementation might handle them. 

You will notice that some test file names begin with `impl_`. This is because the tests in these files are specific to how you choose to implement this assignment (other valid implementations may fail these tests, and that's okay). 

The tests in file names starting with `test_`, on the other hand, are interface tests (ie. they should pass for any valid implementation). The tests in these files should not be specific to your implementation.

#### 3a. Complete `test_question_asker.py`
- **Write tests** for input validation and error handling
- **Test** invalid input followed by valid input scenarios
- **Use `patch('builtins.input')`** to mock user input

#### 3b. Complete `impl_priority_calculator.py`
- **Write specific test cases** based on your particular scoring system that you previously documented
- **Fill in expected values** for each test method
- **Test edge cases** (invalid years, negative credits, etc.)

#### 3c. Complete `impl_main.py`
- **Test** that graduation questions are only asked for seniors
- **Test** different scenarios (freshman, non-graduating senior, etc.)

#### 3d. Commit test files

- Submit your code to GitHub. These commands should help:
  - `git add .`
  - `git commit -m "Wrote tests for question asker, priority calculator, and main"`
  - `git push`
- Check Pawtograder to make sure the submission went through. If not, please ask for help during office hours.
- You may try to run your tests now. Your tests will fail; this is expected: we haven't gotten to implementing the functionality yet.

### Part 4: Implement functions according to your test specification

Now, implement the functions in `question_asker.py`, `priority_calculator.py`, and `main.py`.

Your tests should start to pass as you implement.

### Part 5: Extending Additional Questions
* **Add exactly two new yes/no prompts** (e.g., older than 23?, honors student?)
* **Update your tests first** to include these new questions, if you haven't done so already
* **Then implement** the functionality to make tests pass
* **Return** a dictionary where each key corresponds to a question and the value is a boolean

### Part 6: Final Testing and Integration
* Run all tests to ensure everything passes
* Execute your program

## Downloading required libraries
Run the following command to install dependencies:

```pip install -r requirements.txt```

To run `test_runner.py` and `generate_coverage_reports.sh`, you need to download the required Python libraries that are specified in `requirements.txt` using the command above. You don't need to know about these libraries; they are **only** there for our scripts to run properly. You may take a look at our files if you're interested in seeing how they work. 


## Running Tests
To run your tests, use the `test_runner.py` file we have provided. Run `python3 test_runner.py` to run all tests in the `tests/` directory. 

If you try to run the test files directly, you will face an import error due to the way the assignment is structured (to work for the autograder). DO NOT try to fix this import error, and leave the imports as they are provided in the handout. Othwerwise, the autograder may not be able to run your tests properly. 

While you are completing the test files, you may want to run individual test files at a time, instead of running them all at once. To do this, you can run `test_runner.py` with the `-t` option in your terminal to only run tests in the files you specify. Note: the test file names you provide must be in the `tests/` directory, or they won't run. 

Example command to only run tests in `test_question_asker.py`:
```python3 test_runner.py -t test_question_asker.py```

You can also run multiple test files by listing the file names after the `-t` option. 
Example command to run multiple test files: 
```python3 test_runner.py -t test_question_asker.py test_priority_calculator.py```

If you just want to run all tests in the `tests/` directory, you can run `python3 test_runner.py` omitting the `-t` flag at the end. This will run all test files with the pattern `test_*.py` or `impl_*.py` inside of the `tests/` directory. Make sure all your test file names start with either `test_` or `impl_`, or else they will not run.

## Generating Coverage reports

Run the following command in your terminal to generate coverage reports:

```./generate_coverage_reports```

A link to the a html page containing the coverage reports will be produced in the output of the command. You can click on it to view detailed coverage reports. 

These reports indicate how much of your code is being executed by your tests. This is a purely syntactic check, and having full coverage does not necessarily mean your tests are sufficient, but it's a good starting point. You should aim to have full coverage (i.e., every line of your code gets exercised by your tests).


Good luck!
