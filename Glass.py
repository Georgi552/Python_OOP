class Glass:
    capacity = 250  # class Attribute

    def __init__(self):
        self.content = 0  # instance Atrribute

    def fill(self, ml):
        if self.content + ml <= Glass.capacity:
            self.content += ml
            return f"Glass filled with {ml} ml"
        else:
            return f"Cannot add {ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        return f"{Glass.capacity - self.content} ml left"



glass = Glass()

print(glass.fill(100))

print(glass.fill(200))

print(glass.empty())

print(glass.fill(200))

print(glass.info())