class calculator():
    x = None
    y = None
    z = None
    def add(x,y):
        z = x + y
        return z
    def substract(x, y):
        z = x - y
        return z
    def multiply(x, y):
        z = x * y
        return z
    def divide(x, y):
        z = x / y
        return z

result = calculator.multiply(4, 5)
print(result)