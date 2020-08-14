


class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        print("Hello from init")

    def config (self):
        print("config is ", self.cpu, self.ram)
        



c1 = Computer("i5", 16)
c2 = Computer("i3", 8)

c1.config()
c2.config()