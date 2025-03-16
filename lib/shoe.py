class Shoe:
    def __init__(self, brand, size, color):
        self.brand = brand
        self._size = None
        self.size = size
        self.color = color
        self.condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    def __str__(self):
        return f"{self.color} {self.brand} shoe, size {self.size}"

# Example usage:
# shoe = Shoe("Nike", 42, "black")
# print(shoe)
# shoe.cobble()