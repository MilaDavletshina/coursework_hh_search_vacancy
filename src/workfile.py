import json
# import os
from abc import ABC, abstractmethod
from src.vacancies import Vacancy

#
# class AbstractFile(ABC):
#     """Абстрактный класс для работы с файлами"""
#
#     @abstractmethod
#     def get_vacancy(self):
#         """Получение вакансий из файла"""
#         pass
#
#     @abstractmethod
#     def add_vacancy(self, new_vacancy):
#         """Добавление вакансий в файл"""
#         pass
#
#     @abstractmethod
#     def delete_vacancy(self):
#         """Удаление вакансий из файла"""
#         pass
#
#
# class JSONSaver(AbstractFile):
#     """Класс для сохранения информации о вакансиях в JSON формате"""
#
#     def __init__(self, filename):
#         self.filename = filename
#
#     def get_vacancy(self):
#         """Получение вакансий из файла"""
#         if not os.path.exists(self.filename):
#             return []
#
#         with open(self.filename, encoding='utf-8') as file:
#             return json.loads(file.read())
#
#     def add_vacancy(self, new_vacancy):
#         """Добавление вакансий в файл"""
#         existing_vacancies = self.get_vacancy() if os.path.exists(self.filename) else []
#         existing_vacancies.append(new_vacancy)
#         with open(self.filename, 'w', encoding='utf-8') as file:
#             json.dump(existing_vacancies, file, ensure_ascii=False, indent=4)
#         print(f'\nПо вашему запросу найдено вакансий: {len(existing_vacancies)}. Данные сохранены в файл {self.filename}\n\n')
#
#     def delete_vacancy(self):
#         """Удаление вакансий из файла"""
#         pass

class AbstractFile(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def get_vacancy(self):
        """Получение вакансий из файла"""
        pass

    @abstractmethod
    def add_vacancy(self, new_vacancy):
        """Добавление вакансий в файл"""
        pass

    @abstractmethod
    def delete_vacancy(self):
        """Удаление вакансий из файла"""
        pass


class JSONSaver(AbstractFile):
    """Класс для сохранения информации о вакансиях в JSON формате"""

    def __init__(self, filepath: str = 'data/vacancies.json'):
        self.filepath = filepath

    def get_vacancy(self):
        """Получение вакансий из файла"""
        try:
            with open(self.filepath, 'r') as f:
                vacancies_data = json.load(f)
                return [Vacancy(**data) for data in vacancies_data]
        except FileNotFoundError:
            return []

    def add_vacancy(self, new_vacancy):
        """Добавление вакансий в файл"""
        # try:
        #     with open(self.filepath, 'w') as file:
        #         json.dump([vacancy.__dict__ for vacancy in new_vacancy], file)
        # except FileNotFoundError:
        #     return []
        data = self.get_vacancy()
        data.extend(new_vacancy)

        with open(self.filepath, "w", encoding="utf8") as file:
            return json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_vacancy(self):
        pass