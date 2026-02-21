import json
import os

class Task:
    def __init__(self, id, title, completed = False):
        self.id = id
        self.title = title
        self.completed = completed
    
    def mark_completed(self):
        self.completed = True
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['id'], data['title'], data['completed'])

class TodoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(len(self.tasks), title, completed = False))   

    def complete_task(self, task_id):
        self.tasks[task_id-1].mark_completed()

    def remove_task(self, task_id):
        self.tasks.pop(task_id - 1)

    def list_tasks(self):
        for i in self.tasks:
            print(i.id + 1, ') ', i.title, ' ', i.completed, sep = '')

    def save_to_file(self):
        try:
            with open('tasks.json', 'w') as file:
                tasks_hash = [self.tasks[i].to_dict() for i in range(len(self.tasks))]
                json.dump(tasks_hash, file)
        except FileNotFoundError:
            print('Файл не найден')
    
    def load_from_file(self):
        try:
            if os.path.getsize('tasks.json') > 0:
                with open('tasks.json', 'r') as file:
                    data = json.load(file)
                    self.tasks = [Task.from_dict(el) for el in data]
            else:
                self.tasks = []
        except FileNotFoundError:
            print('Файл не найден')
    
    def printh(self):
        print(len(self.tasks))


def main():
    mas = TodoManager()
    mas.load_from_file()
    while True:
        print('1. Добавить задачу')
        print('2. Показать задачи')
        print('3. Завершить задачу')
        print('4. Удалить задачу')
        print('5. Выход')

        choice = input('Выберите дейтсвие ')

        if choice == '1':
            title = input('Введите название задачи ')
            mas.add_task(title)
        elif choice == '2':
            mas.list_tasks()
        elif choice == '3':
            id = int(input('Введите id задачи, которую нужно завершить '))
            mas.complete_task(id)
        elif choice == '4':
            id = int(input('Введите id задачи, которую нужно удалить '))
            mas.remove_task(id)
        elif choice == '5':
            print('Выход...')
            mas.save_to_file()
            break

if __name__ == '__main__':
    main()
