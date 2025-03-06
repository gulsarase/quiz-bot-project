import unittest
from unittest.mock import MagicMock
from webax_bot import handle_message
from webexteamssdk import WebexTeamsAPI

class TestWebaxBot(unittest.TestCase):
    def setUp(self):
        # Мокаем API Webex
        self.api = MagicMock(WebexTeamsAPI)
        self.room = MagicMock()
        self.room.id = "room1"
        self.room.title = "Test Room"
        self.api.rooms.list.return_value = [self.room]
    
    def test_handle_message_start_quiz(self):
        # Мокаем входящее сообщение от пользователя
        event = MagicMock()
        event.personId = "user123"
        event.text = "start quiz"
        event.roomId = "room1"
        
        # Проверяем, что метод create был вызван с правильным сообщением
        handle_message(event)
        self.api.messages.create.assert_called_with(roomId="room1", text="What is the capital of France?")

if __name__ == '__main__':
    unittest.main()
