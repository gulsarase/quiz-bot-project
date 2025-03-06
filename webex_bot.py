from webexteamssdk import WebexTeamsAPI
from collect_answers import QuizSession, load_questions

# Инициализация API Webex с использованием токена доступа
api = WebexTeamsAPI(access_token="ZjNjNDdlODEtMzFhYS00ODZiLTkxNmYtNzgwYTIzODdkZmQ1OWYwN2NhZDEtN2Ix_P0A1_e1616d50-6d5e-4dd6-aa12-b1a5c4b49d92N")

# Создание объекта сессии викторины
quiz = QuizSession()

# Получение всех комнат для того, чтобы слушать сообщения в них
def get_rooms():
    try:
        rooms = api.rooms.list()  # Получаем список всех комнат
        return rooms
    except Exception as e:
        print(f"Error while getting rooms: {e}")
        return []

# Функция для обработки входящих сообщений от пользователей
def handle_message(event):
    try:
        user_id = event.personId  # Используем атрибут personId
        message = event.text  # Используем атрибут text

        # Старт викторины
        if message.lower() == "start quiz":
            questions = load_questions()  # Загружаем вопросы
            response = quiz.start_session(user_id, questions)
            api.messages.create(roomId=event.roomId, text=response)
        
        # Обработка ответа на вопрос
        elif message.lower() in ["paris", "london", "berlin", "4", "3", "5"]:  # Список возможных ответов
            response = quiz.process_answer(user_id, message)
            api.messages.create(roomId=event.roomId, text=response)
        
        # Завершаем викторину по команде пользователя
        elif message.lower() == "end quiz":
            response = quiz.end_session(user_id)
            api.messages.create(roomId=event.roomId, text=response)
    except Exception as e:
        print(f"Error while handling message: {e}")

# Функция для прослушивания сообщений
def listen_for_messages():
    rooms = get_rooms()  # Получаем все комнаты
    if not rooms:
        print("No rooms available or access is denied.")
        return
    
    for room in rooms:
        try:
            print(f"Listening in room: {room.title} (ID: {room.id})")
            messages = api.messages.list(roomId=room.id)  # Получаем все сообщения в комнате
            for message in messages:
                handle_message(message)
        except Exception as e:
            print(f"Error while listening to messages in room {room.title}: {e}")

# Запуск бота
if __name__ == "__main__":
    listen_for_messages()
