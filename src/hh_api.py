import requests
from abc import ABC, abstractmethod


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


# if __name__ == "__main__":
#     api = HH("слесарь")
#     res = api.get_vacancies()
#     print(res)
