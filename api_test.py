import sender_stand_request

# Анастасия Стешенко, 24-я когорта — Финальный проект. Инженер по тестированию плюс


# Функция для проверки статуса кода:
def test_post_order_status_code():
    get_response = sender_stand_request.get_orders_track()
    assert get_response.status_code == 200


