from base_functions import *
import datetime
import csv
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
        note_id = max([note.note_id for note in self.notes], default=0) + 1
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_note = Note(note_id, title, content, timestamp)
        self.notes.append(new_note)
        self.save_notes()
        print('Заметка создана успешно!')

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

    def show_notes(self):
        print('Ваши заметки:')
        self.load_notes()
        for note in self.notes:
            print(f"Заметка {note.note_id}: {note.title} - {note.timestamp}")
            print(note.content)
        choice = input('Введите ID заметки для просмотра или 0 для возврата в меню: ')
        if choice == '0':
            exit
        else:
            try:
                self.show_note(int(choice))
            except:
                print('Введите корректный номер заметки')
    def edit_note(self, note_id, new_title, new_content):
        note = next((n for n in self.notes if n.note_id == note_id), None)
        if note is None:
            print('Заметка не найдена')
        else:
            note.title = new_title
            note.content = new_content
            self.save_notes()
            print('Заметка отредактирована')
        
    def remove_note(self, note_id):
        note = next((n for n in self.notes if n.note_id == note_id), None)
        if note is None:
            print('Заметка не найдена')
        else:
            self.notes.remove(note)
            self.save_notes()
            print('Заметка успешно удалена')
    
    def save_notes_csv(self):
        with open('notes.csv', 'w', encoding='utf-8', newline='')  as f:
            writer = csv.DictWriter(f, delimiter=',', fieldnames=['note_id', 'title', 'content', 'timestamp'])
            for note in self.notes:
                writer.writerow(note.__dict__)
        print('Заметки успешно экспортированы в CSV!')      
            
    def import_notes_csv(self):
        file_name = input('Введите имя CSV-файла: ')
        if not os.path.exists(file_name):
            print("Файл не найден")
        with open(file_name, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                note_id = max([note.note_id for note in self.notes], default=0) + 1
                title = row[1]
                content = row[2]                
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                note = Note(note_id, title, content, timestamp)
                self.notes.append(note)
                self.save_notes()
            print('Данные успешно импортированы!')

notes_manager = NoteManager()
        
def menu_notes():
    while True:
        print('Управление заметками: \n 1. Создать заметку \n 2. Просмотреть заметки \n 3. Редактировать заметку \n 4. Удалить заметку \n 5. Экспортировать в CSV \n 6. Импортировать заметки из CSV \n 7. Вернуться в главное меню')
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
        elif choice == '4':
            note_id = input('Введите ID заметки для удаления: ')    
            try:    
                notes_manager.remove_note(int(note_id))
            except:
                print('Введите корректный номер заметки')                
        elif choice == '5':
            notes_manager.save_notes_csv()
        elif choice == '6':
            notes_manager.import_notes_csv()
        elif choice == '7':
            break
        else:
            print('Введите корректное значение:')
