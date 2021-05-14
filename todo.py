import json
import os


class Todo:
    def __init__(self):
        self.path = f'{os.path.expanduser("~")}/.tdl/todo.json'
        self.todos = json.load(open(self.path))

    def list(self):
        if (len(self.todos.keys()) > 0):
            print('todo list:')
            for id in self.todos:
                name = self.todos[id]['name']
                done = '[x]' if self.todos[id]['done'] else '[ ]'
                print(f'{id}. {done} {name}')
        else:
            print('todo list empty!')

    def add(self, name):
        next_id = len(self.todos.keys())
        self.todos[next_id] = {
            'name': name,
            'done': False
        }
        print('todo item added!')

    def remove(self, id):
        del self.todos[id]
        self.reorder()
        print('todo item removed and list reordered!')

    def reorder(self):
        new_id = 0
        new_todos = {}
        for id in self.todos:
            new_todos[new_id] = {
                'name': self.todos[id]['name'],
                'done': self.todos[id]['done'],
            }
            new_id = new_id+1
        self.todos = new_todos

    def done(self, id):
        self.todos[id]['done'] = True
        print('todo item mark as done!')

    def undone(self, id):
        self.todos[id]['done'] = False
        print('todo item unmark as done!')

    def clear(self):
        self.todos = {}
        print('todo list cleared!')

    def save(self):
        json.dump(self.todos, open(self.path, 'w+'))
