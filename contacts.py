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
        data = [c.__dict__ for c in self.contacts]
        save_data('contacts.json', data)
            
    def load_contacts(self):
        data = load_data('contacts.json', [])
        self.contacts = [Contact(**c) for c in data]
        
    def create_contact(self, name, phone, email):
        contact_id = max([contact.contact_id for contact in self.contacts], default=0) + 1
        contact = Contact(contact_id, name, phone, email)
        self.contacts.append(contact)
        self.save_contacts()
        
    def show_contacts(self):
        print('Список контактов:')
        for contact in self.contacts:
            print(f'ID: {contact.contact_id}, Имя: {contact.name}, Телефон: {contact.phone}, Email: {contact.email}')

contacts_manager = ContactManager()

def menu_contacts():
    while True:
        print('Управление контактами: \n 1. Добавить контакт \n 2. Посмотреть контакты \n 3. Редактировать контакт \n 4. Удалить контакт \n 5. Найти контакт по имени или номеру телефона \n 6. Экспортировать в CSV \n 7. Импортировать задачи из CSV \n 8. Вернуться в главное меню')
        choice = input('Выберите действие:')
        if choice == '1':
            name = input('Введите имя контакта: ')
            phone = input('Введите номер телефона: ')
            email = input('Введите email: ')
            contacts_manager.create_contact(name, phone, email)
        elif choice == '2':
            contacts_manager.show_contacts()
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