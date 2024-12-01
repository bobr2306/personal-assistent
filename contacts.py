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
            
    def edit_contact(self, contact_id, name, phone, email):
        contact = next((c for c in self.contacts if c.contact_id == contact_id), None)
        if contact is None:
            print('Контакт не найден')
        else:
            contact.name = name
            contact.phone = phone
            contact.email = email
            self.save_contacts()
            print('Контакт успешно изменен')
            
    def remove_contact(self, contact_id):
        try:
            contact = next(c for c in self.contacts if c.contact_id == contact_id)
            self.contacts.remove(contact)
            self.save_contacts()
            print('Контакт успешно удален')
        except:
            print('Контакт не найден')
    def save_contacts_csv(self):
        with open('contacts.csv', 'w', encoding='utf-8') as f:
            fieldnames = ['contact_id', 'name', 'phone', 'email']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            for contact in self.contacts:
                writer.writerow(contact.__dict__)
        print('Контакты успешно экспортированы в CSV файл "contacts.csv"')
        
    def load_contacts_csv(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                contact_id = int(row['contact_id'])
                name = row['name']
                phone = row['phone']
                email = row['email']
                self.create_contact(name, phone, email)
                
    def search_contact(self, q):
        results = [contact for contact in self.contacts if q in contact.name or q in contact.phone]
        if results:
            print('Найденные контакты:')
            for contact in results:
                print(f'ID: {contact.contact_id}, Имя: {contact.name}, Телефон: {contact.phone}, Email: {contact.email}')
        else:
            print('Контакты не найдены')

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