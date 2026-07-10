from src.task import Task

tasks = []
next_id = 1


def add_task(title, description, priority):

    global next_id

    task = Task(next_id, title, description, priority)

    tasks.append(task)

    next_id += 1


def get_tasks():

    return tasks


def delete_task(task_id):

    global tasks

    tasks = [t for t in tasks if t.id != task_id]


def toggle_task(task_id):

    for task in tasks:

        if task.id == task_id:

            task.completed = not task.completed