class Task:

    def __init__(self, id, title, description, priority="Média", completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = completed