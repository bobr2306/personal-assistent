import pandas as pd
import json
import datetime
import os
import csv

def main_menu():
    print('Добро пожаловать в Персональный помощник! \n Выберите действие: \n 1. Управление заметками \n 2. Управление задачами \n 3. Управление контактами \n 4. Управление финансовыми записями \n 5. Калькулятор \n 6. Выход')
    choise = input('Выберите номер действия:')
    if choise == '1':
        menu_notes()
    elif choise == '2':
        menu_tasks()
    elif choise == '3':
        menu_contacts()
    elif choise == '4':
        menu_financial_records()
    elif choise == '5':
        menu_calculator()
    elif choise == '6':
        exit    
    else:
        print('Введите корректное значение:')
        main_menu()
    
def save_data(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_data(path, default_data):
    if not os.path.exists(path):
        save_data(path, default_data)
        return default_data
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

class Note:
    def __init__(self, note_id, title, content, timestamp):
        self.note_id = note_id
        self.title = title
        self.content = content
        self.timestamp = timestamp

class NoteManager:
    def __init__(self):
        self.notes = []

    def save_notes(self):
        data = [n.__dict__ for n in self.notes]
        save_data('notes.json', data)

    def load_notes(self):
        data = load_data('notes.json', [])
        self.notes = [Note(**n) for n in data]
    def create_note(self, title, content):
        note_id = len(self.notes) + 1
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_note = Note(note_id, title, content, timestamp)
        self.notes.append(new_note)
        self.save_notes()
        print('Заметка создана успешно!')
        menu_notes()

    def show_note(self, note_id):
        note = next((n for n in self.notes if n.note_id == note_id), None)
        if note is None:
            print('Заметка не найдена')
        else:
            print('Вот ваша заметка')
            print(f"ID: {note.note_id}")
            print(f"Заголовок: {note.title}")
            print(f"Содержание: {note.content}")
            print(f"Дата создания: {note.timestamp}")
        menu_notes()

    def show_notes(self):
        print('Ваши заметки:')
        self.load_notes()
        for note in self.notes:
            print(f"Заметка {note.note_id}: {note.title} - {note.timestamp}")
            print(note.content)
        choice = input('Введите ID заметки для просмотра или 0 для возврата в меню: ')
        if choice == '0':
            menu_notes()
        else:
            self.show_note(int(choice))
    def edit_note(self, note_id, new_title, new_content):
        note = next((n for n in self.notes if n.note_id == note_id), None)
        if note is None:
            print('Заметка не найдена')
        else:
            note.title = new_title
            note.content = new_content
            print('Заметка успешно отредактирована')
        menu_notes()
    def remove_note(self, note_id):
        note = next((n for n in self.notes if n.note_id == note_id), None)
        if note is None:
            print('Заметка не найдена')
        else:
            self.notes.remove(note)
            self.save_notes()
            print('Заметка успешно удалена')
        menu_notes()
    
    def save_notes_csv(self):
        pass
    def import_notes_csv(self):
        pass

notes_manager = NoteManager()
        
def menu_notes():
    print('Управление заметками: \n 1. Создать заметку \n 2. Просмотреть заметки \n 3. Редактировать заметку \n 4. Удалить заметку \n 5. Экспортировать в CSV \n 6. Импортировать заметки из CSV \n 7.Вернуться в главное меню')
    choice = input('Введите:')
    if choice == '1':
        title = input('Введите заголовок заметки: ')
        content = input('Введите содержание заметки: ')
        notes_manager.create_note(title, content)
    elif choice == '2':
        notes_manager.show_notes()
    elif choice == '3':
        choice = input('Введите ID заметки для редактирования: ')
        title = input('Введите новое название:')
        content = input('Введите новое содержание:')
        notes_manager.edit_note(int(choice), title, content)            
        print('Заметка успешно отредактирована')
        menu_notes()
    elif choice == '4':
        note_id = input('Введите ID заметки для удаления: ')    
        try:    
            notes_manager.remove_note(int(note_id))
        except:
            print('Введите корректный номер заметки')
        menu_notes()
            
    elif choice == '5':
        notes_manager.save_notes_csv()
    elif choice == '6':
        notes_manager.import_notes_csv()
    elif choice == '7':
        main_menu()
    else:
        print('Введите корректное значение:')
        menu_notes()



def menu_tasks():
    pass

def menu_contacts():
    pass

def menu_financial_records():
    pass

def menu_calculator():
    pass



if __name__ == '__main__':
    main_menu()