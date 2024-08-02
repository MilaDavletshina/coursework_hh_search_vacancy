import json
# import os
from abc import ABC, abstractmethod
from src.vacancies import Vacancy


class AbstractFile(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def save_vacancy(self):
        """Сохранение вакансий в файл"""
        pass

    @abstractmethod
    def add_vacancy(self, new_vacancy):
        """Добавление вакансий в файл"""
        pass

    @abstractmethod
    def delete_vacancy(self):
        """Удаление вакансии из файла"""
        pass


class JSONSaver(AbstractFile):
    """Класс для сохранения информации о вакансиях в JSON формате"""

    def __init__(self, filepath):
        self.filepath = filepath

    def save_vacancy(self):
        """Сохранение вакансий в файл"""

        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                vacancies_data = json.load(f)
                return [Vacancy(**data) for data in vacancies_data]
        except FileNotFoundError:
            return []

    def add_vacancy(self, new_vacancy):
        """Добавление вакансий в файл"""
        try:
            with open(self.filepath, 'w', encoding='utf-8') as file:
                json.dump([vacancy.__dict__ for vacancy in new_vacancy], file, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            return []

    def delete_vacancy(self):
        pass

