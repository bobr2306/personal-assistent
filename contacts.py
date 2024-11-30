import csv
import datetime
from base_functions import *

class Contact:
    def __init__(self, contact_id, name, phone, email):
        self.contact_id = contact_id
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def save_contacts(self):
        pass
    


def menu_contacts():
    while True:
        print('Управление контактами: \n 1. Добавить контакт \n 2. Посмотреть контакты \n 3. Редактировать контакт \n 4. Удалить контакт \n 5. Найти контакт по имени или номеру телефона \n 6. Экспортировать в CSV \n 7. Импортировать задачи из CSV \n 8. Вернуться в главное меню')
        choice = input('Выберите действие:')
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        elif choice == '7':
            pass
        elif choice == '8':
            break
        else:
            print('Введите корретное значение')