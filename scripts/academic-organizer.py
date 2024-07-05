# 1. Project: Student Academic Organizer for XYZ University
# Client: XYZ University

# Project Overview: XYZ University wants to develop an Academic Organizer to help students manage their academic activities. The solution should include functionalities for managing assignments, tracking study hours, recording grades, and keeping a study journal. Each function should be simple to use and integrate seamlessly into the overall system.

# Scenario and Tasks
# 1. Assignment Management

# Scenario: Students often have multiple assignments with various due dates.
# They need a system to keep track of these assignments efficiently.
# Task: Develop a function that allows students to add assignments with a description, due date, and subject.
# 2. Study Hours Tracking

# Scenario: Students need to monitor the amount of time they spend studying to ensure they are dedicating enough time to each subject.
# Task: Create a function to log study sessions by capturing the subject, duration, and date.
# 3. Grade Recording

# Scenario: Keeping track of grades helps students monitor their academic progress and identify areas for improvement.
# Task: Implement a function to record grades by specifying the subject, type of assessment (e.g., exam, quiz), and the grade received.
# 4. Study Journal Keeping

# Scenario: Reflecting on study habits and strategies can help students improve their learning techniques and manage stress.
# Task: Design a function that allows students to add journal entries by specifying the date and content.

# 1. Assignement Manager Function
def assignement_manager():
    """
    Description:

    Args: None

    Return: 
    """
    # Define Data Structure - dictionary
    assignments = {}

    # Loop to prompt user to enter assignement description, subject and due date 
    while True:
        subject = input("Enter the subject or 'Done' to exit: ").strip()
        if subject.lower() == 'done':
            break
        try:
            description = input(f"Enter {subject} description: ")
            due_date = input(f"Enter {subject} due date: ")
            assignments[subject] = [description, due_date]
            print(f"Assignments: {assignments}")
        except ValueError as e:
            print(f"Error: {e}")

    return assignments


assignement_manager()
    #{'subject:' ['description', 'due date']}
  
        # prompt student to add assignments subject string
        # prompt student to add assignments description string
        # prompt student to add assignments due date date
    

# 2. Study Hours Tracker Function
def study_hours_tracker():
    """
    Description:

    Args: 

    Return:
    """

# 3. Grade Recorder Function
def grade_recorder():
    """
    Description:

    Args: 

    Return:
    """

# 1. Study Jorunal Keeper Function
def study_journal_keeper():
    """
    Description:

    Args: 

    Return:
    """

def main():
    assignement_manager()