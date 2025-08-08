import os

class Question:
    def __init__(self,question_text,options,correct_option) :
        self.question_text = question_text
        self.options = options
        self.correct_option = correct_option
    def is_correct(self,user_answer) :
        return user_answer == self.correct_option

class Quiz :
    def __init__(self,categories) :
        self.categories = categories
        self.questions = []
        self.score = 0 
    def load_questions(self,file_path) :
        try :
            with open(file_path, "r") as f :
                lines = f.read().strip().split("\n")
        except FileNotFoundError :
            print(f"Error: File {file_path} not Found")
            return
        
        i = 0 
        while i < len(lines) :
            if lines[i].startswith("Q:") :
                question_text = lines[i][3:].strip()
                options = [lines[i+1][2:].strip(),lines[i+2][2:].strip(),lines[i+3][2:].strip(),lines[i+4][2:].strip() ]
                correct_option = lines[i+5].split(":")[1].strip()
                question = Question(question_text,options,correct_option)
                self.questions.append(question)
                i += 6
            else :
                i += 1
    def start_quiz(self)         :
        print(f"\n📘 Starting quiz in category: {self.categories}\n")
        for idx,question in enumerate(self.questions,start = 1) :
            print(f"Q{idx}: {question.question_text}")
            for opt_label, opt in zip(["A","B","C","D"],question.options) :
                print(f"  {opt_label}. {opt}")
            answer = input("Your answer (A/B/C/D): ").strip().upper()
            while answer not in ["A","B","C","D"] :
                print("Please Enter Valid Answer")
                answer = input("Your answer (A/B/C/D): ").strip().upper()
            if question.is_correct(answer) :
                self.score += 1
            print()
    def show_result(self) :
        total = len(self.questions)
        percent = (self.score / total) * 100
        print(f"\n🎯 Quiz Finished!")
        print(f"✅ Score: {self.score}/{total}")
        print(f"📊 Percentage: {percent:.2f}%")
        if percent == 100 :
            feedback = "🌟 Excellent!"
        elif percent >= 70 :
            feedback = "👍 Good Job!"
        elif percent >= 50 :
            feedback = "🙂 Fair Attempt"
        else :
            feedback = "❗ Try Again"
        print(f"💬 Feedback: {feedback}\n")
class QuizManager :
    def __init__(self,quiz_dir="quizzes") :
        self.quiz_dir = quiz_dir
    def list_categories(self) :
        files = os.listdir(self.quiz_dir)
        return [f.replace(".txt","") for f in files if f.endswith(".txt")]
    def choose_category(self) :
        categories = self.list_categories()
        if not categories :
            print("No quiz categories founs.")
            return None
        print("📚 Available Categories:")
        for i,cat in enumerate(categories,1) :
            print(f"{i}. {cat.capitalize()}")
        choice = input("Choose a category (number): ")
        try :
            return categories[int(choice) -1]
        except(IndexError,valueError) :
            print("❌ Invalid choice.")
            return None
    def run(self) :
        print("🎉 Welcome to QuizMaster 🎉")
        category = self.choose_category()
        if not category :
            return
        quiz = Quiz(category)
        quiz.load_questions(os.path.join(self.quiz_dir,category + ".txt"))
        if not quiz.questions :
            print("No qusetions found in thin category")
            return
        quiz.start_quiz()
        quiz.show_result()

if __name__ == "__main__" :
    manager = QuizManager()
    manager.run()





