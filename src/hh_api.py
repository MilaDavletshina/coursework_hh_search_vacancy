import requests
import json
import os
from abc import ABC, abstractmethod

#выводит все вакансии с найденным запросом


class Parser(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_vacancies(self, keyword):
        """Получение вакансии по ключевому слову"""
        pass


class HH(Parser):
    """Класс для работы с HeadHunter. Класс HeadHunter является родительским от класса Parser"""

    def __init__(self, keyword):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {
            'text': keyword,
            'page': 0,
            'per_page': 10
        }
        self.vacancies = []

    def get_vacancies(self):
        """Получение вакансии по ключевому слову"""
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

        return self.vacancies



# Выводит первую позицию с найденным запросом

#
# class Parser(ABC):
#     """Абстрактный класс для работы с API"""
#
#     @abstractmethod
#     def get_vacancies(self, keyword):
#         """Получение вакансии по ключевому слову"""
#         pass


# class HH(Parser):
#     """Класс для работы с HeadHunter. Класс HeadHunter является родительским от класса Parser"""
#     BASE_URL = "https://api.hh.ru/vacancies"
#
#
#     def get_vacancies(self, keyword):
#         """Получение вакансии по ключевому слову"""
#         response = requests.get(self.BASE_URL, params={'text': keyword})
#         if response.status_code == 200:
#             return response.json().get('items', [])
#         return []


# if __name__ == "__main__":
#     api = HH()
#     res = api.get_vacancies("слесарь")
#     print(res)
