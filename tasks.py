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
        data = load_data('tasks.json')
        self.tasks = [Task(**t) for t in data]
        
    def create_task(self, title, description, priority, due_date=None):
        task_id = len(self.tasks) + 1
        task = Task(task_id, title, description, False, priority, due_date)
        self.tasks.append(task)
        self.save_tasks()
        
    def show_tasks(self):
        for task in self.tasks:
            print(f"Задача {task.task_id}: {task.title} \n {task.description} {task.done}, Приоритет: {task.priority}, Due Date: {task.due_date}")

    def edit_task(self, task_id, title, description, priority):
        task = next(([t for t in self.tasks if t.task_id == task_id]), None)
        if task is None:
            print("Задача не найдена")
        else:
            task.title = title
            task.description = description
            task.priority = priority
            print('Задача отредактирована!')
            self.save_tasks()
        
    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.save_tasks()

    def save_tasks_csv(self):
        with open(self.file_name, 'w', newline='') as csvfile:
            fieldnames = ['task_id', 'title', 'description', 'done', 'priority', 'due_date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    def import_tasks_csv(self):
        file_name = input('Введите имя CSV-файла:')    
        if not os.path.exists(file_name):
            print("Файл не найден")
            menu_tasks()
        with open(file_name, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                task_id = len(self.tasks) + 1
                title = row[1]
                description = row[2]         
                done = row[3]
                priority = row[4]
                due_date = row[5]       
                task = Task(task_id, title, description, )
                self.tasks.append(task)
                self.save_tasks()
            print('Данные успешно импортированы!')
            menu_tasks()
    def done_task(self, task_id):
        pass
    
tasks_manager = TaskManager()    

def menu_tasks():
    print('Управление задачами: \n 1. Создать задачу \n 2. Просмотреть задачи \n 3. Редактировать задачу \n 4. Удалить задачу \n 5. Экспортировать в CSV \n 6. Импортировать задачи из CSV \n 7. Вернуться в главное меню')
    choice = input('Введите: ')
    if choice == '1':
        title = input('Введите заголовок задачи: ')
        description = input('Введите описание задачи: ')
        priority = input('Введите приоритет задачи (Высокий, Средний, Низкий): ')
        due_date = input('Введите дедлайн (дд-мм-гггг) - необязательно')        
        tasks_manager.create_task(title, description, priority, due_date)
        menu_tasks()
        
    elif choice == '2':
        tasks_manager.show_tasks()
        menu_tasks()
        
    elif choice == '3':
        choice = input('Введите ID задачи для редактирования: ')
        title = input('Введите новое название: ')
        description = input('Введите новое описание: ')
        priority = input('Введите новый приоритет задачи (Высокий, Средний, Низкий): ')
        tasks_manager.edit_task(int(choice), title, description, priority)
        menu_tasks()
    
    elif choice == '4':
        task_id = input('Введите ID задачи для удаления: ')    
        tasks_manager.remove_task(int(task_id))
        menu_tasks()
    
    elif choice == '5':
        tasks_manager.save_tasks_csv()
    
    elif choice == '6':
        tasks_manager.import_tasks_csv()
    
    elif choice == '7':
        exit
    
    else:
        print('Введите корректное значение:')