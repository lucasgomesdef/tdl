import sys
from todo import Todo


def todo():
    todos = Todo()
    if len(sys.argv) == 1:
        print('Incorrect usage!')
    else:
        cmd = sys.argv[1]
        if cmd == 'add':
            name = sys.argv[2]
            todos.add(name)
        elif cmd == 'remove':
            id = sys.argv[2]
            todos.remove(id)
        elif cmd == 'show':
            todos.show()
        elif cmd == 'done':
            id = sys.argv[2]
            todos.done(id)
        elif cmd == 'undone':
            id = sys.argv[2]
            todos.undone(id)
        elif cmd == 'clear':
            todos.clear()
    todos.save()


if __name__ == '__main__':
    todo()
