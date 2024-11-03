# Екатерина Анисимова, 23-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import sander_stand_request

def test_get_order():
    track = sander_stand_request.create_order(data.order_body).json()['track']
    response = sander_stand_request.get(track)
    assert response.status_code == 200
