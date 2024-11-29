import pandas as pd
import json
import datetime

def main_menu():
    print('Добро пожаловать в Персональный помощник! \n Выберите действие: \n 1. Управление заметками \n 2. Управление задачами \n 3. Управление контактами \n 4. Управление финансовыми записями \n 5. Калькулятор \n 6. Выход')
    choise = input()
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
    def create_note(self):
        pass
    def show_notes(self):
        pass
        
class NoteManager:
    pass
        
def menu_notes():
    pass

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