from base_functions import *
import csv

class Task:
    def __init__(self, task_id, title, description, done, priority, due_date):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date

class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def save_tasks(self):
        data = [t.__dict__ for t in self.tasks]
        save_data('tasks.json', data)
        
    def load_tasks(self):
        data = load_data('tasks.json', [])
        self.tasks = [Task(**t) for t in data]
        
    def create_task(self, title, description, priority, due_date=None):
        task_id = max([task.task_id for task in self.tasks], default=0) + 1
        task = Task(task_id, title, description, False, priority, due_date)
        self.tasks.append(task)
        
    def show_tasks(self):
        print('Ваши задачи: ')
        self.load_tasks()
        for task in self.tasks:
            if task.done:
                done = 'Выполнено'
            else:
                done = 'Не выполнено'
            if not task.due_date:
                due_date = '-'
            print(f"Задача {task.task_id}: {task.title} ({done}) \n {task.description}, Приоритет: {task.priority}, Срок выполнения: {due_date}")
        choice = input('Введите ID задачи для выполнения задачи или 0 для возврата в меню задач: ')
        if choice == '0':
            exit
        else:
            try:
                self.done_task(int(choice))
            except:
                print('Введите корректное значение: ')
                
                
    def edit_task(self, task_id, title, description, priority):
        task = next((t for t in self.tasks if t.task_id == task_id), None)
        if task is None:
            print("Задача не найдена")
        else:
            task.title = title
            task.description = description
            task.priority = priority
            self.save_tasks()
            print('Задача отредактирована!')
        
    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.save_tasks()

    def save_tasks_csv(self):
        with open('tasks.csv', 'w', encoding='utf-8') as f:
            fieldnames = ['task_id', 'title', 'description', 'done', 'priority', 'due_date']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            for task in self.tasks:
                writer.writerow(task.__dict__)
        print('Ваши задачи успешно экспортированы в CSV!')

    def import_tasks_csv(self):
        file_name = input('Введите имя CSV-файла:')    
        if not os.path.exists(file_name):
            print("Файл не найден")
        with open(file_name, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                task_id = max([task.task_id for task in self.tasks], default=0) + 1
                title = row[1]
                description = row[2]         
                done = row[3]
                priority = row[4]
                due_date = row[5]       
                task = Task(task_id, title, description, done, priority, due_date)
                self.tasks.append(task)
                self.save_tasks()
            print('Данные успешно импортированы!')
    def done_task(self, task_id):
        task = next((t for t in self.tasks if t.task_id == task_id), None)
        if task is None:
            print('Задача не найдена')
        else:
            task.done = True
            print('Задача выполнена!')
            self.save_tasks()
    
tasks_manager = TaskManager()    

def menu_tasks():
    while True:
        print('Управление задачами: \n 1. Создать задачу \n 2. Просмотреть задачи \n 3. Редактировать задачу \n 4. Удалить задачу \n 5. Экспортировать в CSV \n 6. Импортировать задачи из CSV \n 7. Вернуться в главное меню')
        choice = input('Введите: ')
        if choice == '1':
            title = input('Введите заголовок задачи: ')
            description = input('Введите описание задачи: ')
            priority = input('Введите приоритет задачи (Высокий, Средний, Низкий): ')
            due_date = input('Введите дедлайн (дд-мм-гггг) - необязательно')        
            tasks_manager.create_task(title, description, priority, due_date)
            
        elif choice == '2':
            tasks_manager.show_tasks()
            
        elif choice == '3':
            choice = input('Введите ID задачи для редактирования: ')
            title = input('Введите новое название: ')
            description = input('Введите новое описание: ')
            priority = input('Введите новый приоритет задачи (Высокий, Средний, Низкий): ')
            try:
                tasks_manager.edit_task(int(choice), title, description, priority)
            except:
                print('Некорректные данные')
        elif choice == '4':
            task_id = input('Введите ID задачи для удаления: ')    
            tasks_manager.remove_task(int(task_id))
        
        elif choice == '5':
            tasks_manager.save_tasks_csv()
        
        elif choice == '6':
            tasks_manager.import_tasks_csv()
        
        elif choice == '7':
            break
        
        else:
            print('Введите корректное значение:')