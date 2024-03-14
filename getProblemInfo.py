import html2text
import re
import requests

from bs4 import BeautifulSoup

CODEFORCES_URL = "https://codeforces.com/problemset/problem/{}/{}"

def get_info():
    """Retrieve problem information from Codeforces."""
    problem_code = get_problem_code()
    if problem_code:
        link = CODEFORCES_URL.format(problem_code[:-1], problem_code[-1])
        title, difficulty, statement = extract_problem_info(link)
        if title and difficulty and statement:
            return problem_code, format_problem_data(title, difficulty, statement)
        else:
            print("Error retrieving problem information.")
    else:
        print("Invalid problem code.")

def get_problem_code():
    """Get the problem code from the user."""
    problem_code = input("Enter the problem's code (e.g., 996A): ")
    if validate_problem_code(problem_code):
        return problem_code
    else:
        print("Invalid problem code.")
        return None

def validate_problem_code(problem_code):
    """Validate the problem code format."""
    return re.match(r'^[0-9]{1,4}[A-Z]$', problem_code)

def format_problem_data(title, difficulty, statement):
    """Format the extracted problem data."""
    title = title.text.strip()
    difficulty = re.sub(r'[^0-9]', '', difficulty.text.strip())

    statement_text = html2text.html2text(str(statement)).replace('$$$', '$')
    lines = statement_text.split('\n')
    del lines[1:18]
    lines[0] = '# ' + lines[0]
    statement = '\n'.join(lines)

    return title, difficulty, statement

def extract_problem_info(link):
    """Extract information about a Codeforces problem from a given link."""
    try:
        response = requests.get(link)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.find('div', class_='title')
        difficulty = soup.find('span', {'title': 'Difficulty'})
        statement = soup.find('div', class_='problem-statement')

        return title, difficulty, statement

    except requests.exceptions.RequestException as e:
        print(f"Error fetching problem information: {e}")
        return None, None, None
