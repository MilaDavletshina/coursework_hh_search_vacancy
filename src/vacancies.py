class Vacancy:
    """Класс для работы с вакансией"""
    def __init__(self, name, salary, url, description):
        self.name = name
        self.salary = salary if salary is not None else "По найденной позиции зарплата не указана"
        self.url = url
        self.description = description

    def __str__(self):
        """Метод для отображения информации при  выводе информации"""
        return (f"Вакансия: {self.name}\n"
                f"Зарплата: {self.salary}\n"
                f"Ссылка на вакансию: {self.url}\n"
                f"Описание: {self.description}"
                )

    def __lt__(self, other):
        """Метод сравнения вакансий между собой по зарплате"""
        return self.salary < other.salary


    # def vacancies_to_dict(self) -> dict:
    #     """ Метод возвращает данные по вакансии в виде словаря """
    #
    #     return {
    #         "Вакансия": self.name,
    #         "Зарплата": self.salary,
    #         "Ссылка на вакансию": self.url,
    #         "Занятость": self.employment,
    #     }


# if __name__ == "__main__":
#     hh = Vacancy("слесарь", "Москва", 20000, "https://api.hh.ru/vacancies?employer_id=10913256", "полная")
#     print(hh)
