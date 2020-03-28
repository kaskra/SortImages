class Processor:
    def __init__(self, data):
        self.EXTENSIONS = []
        self.data = data

    def validate_data(self):
        if not all(list(map(lambda e: e[0] == '.', self.EXTENSIONS))):
            raise ValueError("Extensions must start with '.'")

    def process(self):
        raise NotImplementedError()

    def out(self):
        raise NotImplementedError()
