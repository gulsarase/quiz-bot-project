import unittest
from collect_answers import QuizSession, load_questions

class TestQuizSession(unittest.TestCase):
    def setUp(self):
        self.quiz = QuizSession()
        self.user_id = "user123"
        self.questions = load_questions()
        self.quiz.start_session(self.user_id, self.questions)
    
    def test_start_session(self):
        # Проверяем, что сессия началась с правильным вопросом
        first_question = self.quiz.ask_question(self.user_id)
        self.assertIn("What is the capital of France?", first_question)
    
    def test_process_answer(self):
        # Проверяем обработку первого ответа
        self.quiz.process_answer(self.user_id, "Paris")
        second_question = self.quiz.ask_question(self.user_id)
        self.assertIn("What is 2 + 2?", second_question)
    
    def test_end_session(self):
        # Завершаем сессию и проверяем результаты
        self.quiz.process_answer(self.user_id, "Paris")
        self.quiz.process_answer(self.user_id, "4")
        result = self.quiz.end_session(self.user_id)
        self.assertIn("You answered", result)

if __name__ == '__main__':
    unittest.main()
