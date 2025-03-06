import json
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QuizSession:
    def __init__(self):
        self.sessions = {}

    def start_session(self, user_id, questions):
        """Запуск сессии викторины для пользователя."""
        self.sessions[user_id] = {
            "questions": questions,
            "current_question": 0,
            "answers": []
        }
        logging.info(f"Quiz started for user {user_id}")
        return self.ask_question(user_id)

    def ask_question(self, user_id):
        """Отправка вопроса пользователю."""
        session = self.sessions.get(user_id)
        if not session or session["current_question"] >= len(session["questions"]):
            return self.end_session(user_id)
        
        question_data = session["questions"][session["current_question"]]
        question_text = f"{question_data['question']}\nOptions: {', '.join(question_data['options'])}"
        return question_text

    def process_answer(self, user_id, answer):
        """Обрабатывает ответ пользователя и переходит к следующему вопросу."""
        session = self.sessions.get(user_id)
        if not session:
            return "No active quiz session found. Type 'quiz' to start a new one."
        
        session["answers"].append(answer)
        session["current_question"] += 1
        return self.ask_question(user_id)

    def end_session(self, user_id):
        """Завершаем сессию и подводим итог."""
        session = self.sessions.get(user_id)
        if not session:
            return "No session data found."
        
        correct_answers = 0
        for i, answer in enumerate(session["answers"]):
            if answer == session["questions"][i]["answer"]:
                correct_answers += 1
        
        del self.sessions[user_id]  # Удаляем сессию после завершения
        return f"Quiz complete! You answered {correct_answers}/{len(session['questions'])} correctly."

# Пример списка вопросов
def load_questions():
    return [
        {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin"], "answer": "Paris"},
        {"question": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4"}
    ]

# Пример использования
if __name__ == "__main__":
    user_id = "user123"
    questions = load_questions()

    quiz = QuizSession()
    print(quiz.start_session(user_id, questions))  # Запуск сессии
    print(quiz.process_answer(user_id, "Paris"))  # Обработка первого ответа
    print(quiz.process_answer(user_id, "4"))  # Обработка второго ответа
    print(quiz.end_session(user_id))  # Завершение сессии
