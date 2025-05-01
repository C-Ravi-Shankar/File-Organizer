class test:
    def __init__(self):
        self.name = "name"

    def hi(self):
        print("name:",self.name)
    
b = test()
print(b.name)
b.hi()