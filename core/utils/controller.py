class Chain:
    def __init__(self, name="Chain"):
        self.container = []
        self.name = name

    def add_node(self, node):
        self.container.append(node)

    def remove_node(self, name):
        del self.container[name]

    def forward(self):
        for processor in self.container:
            processor.process()
        


