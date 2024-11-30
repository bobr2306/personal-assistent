class Note:
    def __init__(self, note_id, title, content, timestamp):
        self.id = note_id
        self.title = title
        self.content = content
        self.timestamp = timestamp


class NoteManager:
    def __init__(self):
        self.notes = []

    def save_notes(self):
        pass

    def create_note(self, title, content):
        note_id = len(self.notes) + 1
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_note = Note(note_id, title, content, timestamp)
        self.notes.append(new_note)
        menu_notes()

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
        self.show_notes()

    def show_notes(self):
        print('Ваши заметки:')
        for note in self.notes:
            print(f"Заметка{note.id}: {note.title} - {note.timestamp}")
            print(note['content'])
        choice = input('Введите ID заметки для просмотра или 0 для возврата в меню: ')
        if choice == '0':
            menu_notes()
        else:
            try:
                self.show_note(int(choice))
            except:
                print('Введите корректный номер заметки')

    def edit_note(self, note_id, new_title, new_content):
        note = next((n for n in self.notes if n.id == note_id), None)
        note.title = new_title
        note.content = new_content
        print('Заметка успешно отредактирована')
        self.menu_note(note_id)
def menu_notes():
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
        choice = input('Введите ID заметки для редактирования: ')
        try:
            notes_manager.show_note(int(choice))
        except:
            print('Введите корректный номер заметки')
        else:
            title = input('Введите новое название:')
            content = input('Введите новое содержание:')
            notes_manager.edit_note(int(choice), title, content)
            print('Заметка успешно отредактирована')
    elif choice == '4':
        pass
    elif choice == '5':
        main_menu()
