# Python QuizMaster

A command-line quiz game that lets you test your knowledge in various categories such as Backend, Database, Frontend, and Git. The game loads questions from text files and provides instant feedback and scoring.

## Features
- Multiple quiz categories (Backend, Database, Frontend, Git)
- Loads questions and answers from easily editable text files
- Interactive command-line interface
- Instant scoring and feedback
- Easy to add new categories and questions

## Folder Structure
```
python_quizmaster/
  ├── quizGame.py           # Main Python script to run the quiz
  ├── quizzes/              # Folder containing quiz question files
  │     ├── backend.txt
  │     ├── database.txt
  │     ├── frontend.txt
  │     └── git.txt
  └── README.md             # Project documentation
```

## How to Clone This Project
If you want to get a copy of this project from GitHub, use the following command in your terminal:

```
git clone https://github.com/SureshBarika/sprint_pythonProject_quizGame.git
```

## How to Run
1. Make sure you have Python 3 installed.
2. Open a terminal and navigate to the project directory.
3. Run the following command:
   ```
   python quizGame.py
   ```
4. Follow the on-screen instructions to select a category and answer questions.

## How to Add New Quizzes
- To add a new category, create a new `.txt` file in the `quizzes/` folder (e.g., `cloud.txt`).
- Format for each question in the file:
  ```
  Q: Your question text here?
  A. Option 1
  B. Option 2
  C. Option 3
  D. Option 4
  Answer: <A/B/C/D>
  ```
- Separate each question block with a blank line.

## Example Question Format
```
Q: What is Python?
A. A snake
B. A programming language
C. A car
D. A database
Answer: B
```

## Requirements
- Python 3.x
- No external dependencies required

## License
This project is for educational purposes.
