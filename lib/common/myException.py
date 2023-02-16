class MyException(Exception):
    def __init__(self, name, reason):
        self.name = name
        self.reason = reason
