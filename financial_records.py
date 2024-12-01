import csv
import datetime
from base_functions import *

class Finance:
    def __init__(self, id, amount, category, date, description):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

class FinancialManager:
    def __init__(self):
        self.records = []
    
    def save_finances(self):
        data = [f.__dict__ for f in self.records]
        save_data('finances.json', data)

    def load_finances(self):
        data = load_data('finances.json', [])
        self.records = [Finance(**f) for f in data]

    def add_finance_record(self, amount, category, date, description):
        id = max([f.id for f in self.records], default=0) + 1  # Исправлено на f.id
        finance = Finance(id, amount, category, date, description)
        self.records.append(finance)
        self.save_finances()  # Сохраняем после добавления

    def view_finance_records(self, filter_by=None):
        self.load_finances()
        
        if filter_by:
            filtered_records = []
            for record in self.records:
                if filter_by in (record.category, record.date):
                    filtered_records.append(record)
            return filtered_records
        
        return self.records

    def generate_report(self, start_date: str, end_date: str):
        try:
            start_date_obj = datetime.datetime.strptime(start_date, "%d-%m-%Y")
            end_date_obj = datetime.datetime.strptime(end_date, "%d-%m-%Y")
            
            report = [record for record in self.records if start_date_obj <= datetime.datetime.strptime(record.date, "%d-%m-%Y") <= end_date_obj]
            
            return report
        except ValueError:
            print("Ошибка: Неверный формат даты. Используйте ДД-ММ-ГГГГ.")
            return []

    def save_finance_csv(self):
        try:
            with open('records.csv', 'w', encoding='utf-8', newline='') as f:
                fieldnames = ['id', 'amount', 'category', 'date', 'description']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()  # Записываем заголовок
                for r in self.records:
                    writer.writerow(r.__dict__)
            print('Записи успешно экспортированы в CSV файл "records.csv"')
        except Exception as e:
            print(f'Ошибка при экспорте в CSV: {e}')
        
    def load_finance_csv(self):
        filename = input('Введите название CSV файла: ')
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f) 
                for row in reader:
                    try:
                        amount = float(row['amount'])
                        category = row['category']
                        date = row['date']
                        description = row['description']
                        self.add_finance_record(amount, category, date, description)    
                    except ValueError as ve:
                        print(f'Ошибка при добавлении записи из CSV: {ve}')
            print('Записи успешно импортированы из CSV файла.')
        except FileNotFoundError:
            print('Ошибка: Файл не найден.')
        except Exception as e:
            print('Ошибка при импорте!', e)

finance_manager = FinancialManager()

def menu_financial_records():   
    while True:
        print('Управление финансами:')
        print(' 1. Добавить новую финансовую запись \n 2. Посмотреть все записи \n 3. Генерация отчета за определенный период \n 4. Экспорт в CSV \n 5. Импорт из CSV \n 6. Вернуться в главное меню')
        
        choice = input('Выберите действие: ')

        if choice == '1':
            try:
                amount = float(input("Введите сумму (положительное число для доходов и отрицательное для расходов): "))
                category = input("Введите категорию операции: ")
                date = input("Введите дату (ДД-ММ-ГГГГ): ")
                datetime.datetime.strptime(date, "%d-%m-%Y")  
                
                description = input("Введите описание операции: ")
                finance_manager.add_finance_record(amount, category, date, description)
                print("Запись добавлена.")
            except ValueError as ve:
                print(f'Ошибка: {ve}. Убедитесь, что сумма и дата введены правильно.')

        elif choice == '2':
            filter_choice = input(
                "Фильтровать по дате или категории? (введите дату или категорию или оставьте пустым для просмотра всех): ")
            records = finance_manager.view_finance_records(filter_choice)
            if records:
                for record in records:
                    print(
                        f"ID: {record.id}, Сумма: {record.amount}, Категория: {record.category}, Дата: {record.date}, Описание: {record.description}")
            else:
                print("Нет записей для отображения.")

        elif choice == '3':
            start_date = input("Введите начальную дату (ДД-ММ-ГГГГ): ")
            end_date = input("Введите конечную дату (ДД-ММ-ГГГГ): ")
            report = finance_manager.generate_report(start_date, end_date)
            if report:
                for record in report:
                    print(
                        f"ID: {record.id}, Сумма: {record.amount}, Категория: {record.category}, Дата: {record.date}, Описание: {record.description}")
            else:
                print("Нет записей за указанный период.")

        elif choice == '4':
            finance_manager.save_finance_csv()

        elif choice == '5':
            finance_manager.load_finance_csv()

        elif choice == '6':
            break

if __name__ == '__main__':
    menu_financial_records()