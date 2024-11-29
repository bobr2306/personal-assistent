import pandas as pd
import json
import datetime

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
        
    
class Note:
    def __init__(self, note_id, title, content, timestamp):
        self.id = note_id
        self.title = title
        self.content = content
        self.timestamp = timestamp
        
class NoteManager:
    def __init__(self):
        self.notes = []
        
    def create_note(self, title, content):
        note_id = len(self.notes) + 1
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_note = Note(note_id, title, content, timestamp)
        self.notes.append(new_note)
        
    def show_note(self, note_id):
        note = next((n for n in self.notes if n['note_id'] == note_id), None)
        if note is None:
            print('Заметка не найдена')
        else:
            print('Вот ваша заметка')
            print(f"ID: {note.id}")
            print(f"Заголовок: {note.title}")
            print(f"Содержание: {note.content}")
            print(f"Дата создания: {note.timestamp}")

    def show_notes(self):
        print('Ваши заметки:')
        for note in self.notes:
            print(f'Заметка{note['id']}: {note['title']} - {note['timestamp']}')
            print(note['content'])
        choice = input('Введите ID заметки для просмотра или 0 для возврата в меню: ')
        if choice == '0':
            menu_notes()
        else:
            try:
                show_note(int(choice))
            except:
                print('Введите корректный номер заметки')
    

        
def menu_notes():
    notes_manager = NoteManager()
    print('Управление заметками: \n 1. Создать заметку \n 2. Просмотреть заметки \n 3. Редактировать заметку \n 4. Удалить заметку \n 5. Вернуться в главное меню')
    choice = input('Введите:')
    if choice == '1':
        title = input('Введите заголовок заметки: ')
        content = input('Введите содержание заметки: ')
        notes_manager.create_note(title, content)
        print('Заметка создана успешно!')
    elif choice == '2':
        notes_manager.show_notes()
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        main_menu()

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