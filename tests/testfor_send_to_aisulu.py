import unittest
from unittest.mock import patch
from send_to_aisulu import send_results_to_aisulu

class TestSendResultsToAisulu(unittest.TestCase):
    
    @patch('send_to_aisulu.requests.post')
    def test_send_results_success(self, mock_post):
        # Мокаем успешный ответ от API Aisulu
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "success", "message": "Results received"}
        mock_post.return_value = mock_response
        
        # Данные для теста
        user_id = "user123"
        correct_answers = 5
        total_questions = 10
        
        # Проверяем, что результат отправлен успешно
        response = send_results_to_aisulu(user_id, correct_answers, total_questions)
        
        self.assertIsNotNone(response)
        self.assertEqual(response['status'], 'success')
        self.assertEqual(response['message'], 'Results received')
        mock_post.assert_called_once()  # Проверяем, что запрос был отправлен один раз

    @patch('send_to_aisulu.requests.post')
    def test_send_results_failure(self, mock_post):
        # Мокаем ошибку при отправке запроса
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 500  # Серверная ошибка
        mock_response.json.return_value = {"status": "error", "message": "Internal server error"}
        mock_post.return_value = mock_response
        
        # Данные для теста
        user_id = "user123"
        correct_answers = 5
        total_questions = 10
        
        # Проверяем, что при ошибке будет возвращено None
        response = send_results_to_aisulu(user_id, correct_answers, total_questions)
        
        self.assertIsNone(response)
        mock_post.assert_called_once()  # Проверяем, что запрос был отправлен один раз

if __name__ == '__main__':
    unittest.main()
