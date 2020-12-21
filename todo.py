import os
import argparse

def create_files(path):
    # create todo.txt and done.txt
    todo_file = os.path.join(path, 'todo.txt')
    done_file = os.path.join(path, 'done.txt')

    if not os.path.isfile(todo_file):    
        with open(todo_file, 'w') as file:
            pass

    if not os.path.isfile(done_file):
        with open(done_file, 'w') as file:
            pass


def resolve_user_args(args):
    if args.add:
        add_todo(args)
    if args.ls:
        ls(args)

def add_todo(args):
    # todo.txt, done.txt todo --> message
    pass

def ls(args):
    pass

def display_stats():
    pass



def parse():
    parser = argparse.ArgumentParser(description='ToDo List App')
    parser.add_argument('add', default='', type=str, help="add todo")
    parser.add_argument('ls', type=str, help="add todo")
    parser.add_argument('report', type=str, help="add todo")
    return parser



if __name__ == '__main__':
    # file_path = os.getcwd()
    # # step 1
    # create_files(file_path)

    # # step 2
    # parser = parse()
    # args = parser.parse_args()

    # # Functions
    # add_todo(args.add)
