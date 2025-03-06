import requests

def send_results_to_aisulu(user_id, correct_answers, total_questions):
    """Отправка результатов в Aisulu для расчета."""
    
    # Пример структуры данных, которые ты передаешь в Aisulu
    data = {
        "user_id": user_id,
        "correct_answers": correct_answers,
        "total_questions": total_questions
    }

    # URL для отправки данных в Aisulu (предположим, что это HTTP API)
    aisulu_url = "https://aisulu-api.com/calculate_results"  # Заменить на настоящий URL API Aisulu

    try:
        response = requests.post(aisulu_url, json=data)  # Отправляем данные POST-запросом
        response.raise_for_status()  # Проверка на успешный запрос (статус 200)
        print("Results successfully sent to Aisulu!")
        return response.json()  # Возвращаем ответ от Aisulu (если необходимо)
    
    except requests.exceptions.RequestException as e:
        print(f"Error sending results to Aisulu: {e}")
        return None
