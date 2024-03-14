import os
from getProblemInfo import get_info

def create_info_file(problem_code, problem_info, folder_path):
    """
    Create an info file with problem details.

    Args:
        problem_code (str): Code of the problem.
        problem_data (tuple): Tuple containing problem information.
        folder_path (str): Path where the info file should be created.

    """

    title, difficulty, statement = problem_info
    info_path = os.path.join(folder_path, "info.md")

    statement_lines = statement.split("\n")
    statement_lines.pop(0)
    updated_statement = '\n'.join(statement_lines) 

    with open(info_path, "w", encoding="utf-8") as f:
        f.write(f"# {title} \n")
        f.write(f"**Difficulty**: {difficulty} \n")
        f.write(f"**Link**: https://codeforces.com/problemset/problem/{problem_code[:-1]}/{problem_code[-1]}\n\n")
        f.write(updated_statement)
    
    print("\nInfo file successfully created!")

def create_problem_folders(problem_code, problem_info):
    """
    Create folders for the problem.

    Args:
        problem_id (str): ID of the problem.
        problem_index (str): Index of the problem.
        folder_title (str): Title of the problem folder.
        difficulty (str): Difficulty level of the problem.

    """
    difficulty = problem_info[1]
    difficulty_folder_path = os.path.join(difficulty)
    problem_folder_path = os.path.join(difficulty_folder_path, problem_code) 

    if not os.path.exists(problem_folder_path):
        os.makedirs(problem_folder_path)
        
        # Create main.py file
        main_path = os.path.join(problem_folder_path, "main.py")
        with open(main_path, "w") as f:
            f.write("def main():\n\nif __name__ == '__main__':\n\tmain()\n")
        
        # Create info.txt file
        create_info_file(problem_code, problem_info, os.path.join(difficulty_folder_path, problem_code))

        print("\nFolder and files successfully created!")

def create_problem():
    """Create problem folder and files."""
    
    problem_code, problem_info = get_info()

    if not problem_info:
        print("Failed to retrieve problem information.")
        return

    folder_title = f"{problem_code[:-1]}{problem_code[-1]}_{problem_info[0]}"
    create_problem_folders(problem_code, problem_info)

if __name__ == "__main__":
    create_problem()
