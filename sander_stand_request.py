# Екатерина Анисимова, 23-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests


def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)

def get(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + str(track))