class News:
    def __init__(self, source, name, content, time):
        self.source = source
        self.name = name
        self.content = content
        self.time = time

    def __repr__(self):
        return f"{self.source}\n {self.name}\n {self.content}\n {self.time}"
