x = 1
y = x
del x
print(y)


a = 3
b = 3
 
c = [1, 2]
d = [1, 2]
 
print(a is b)
print(c is d)


a = 3
b = 3
 
c = [1, 2]
d = [1, 2]
 
print(a == b)
print(c == d)


mytuple = ("john", "jim", "jack")
print(mytuple.count("john"))



class Computer:
 
    def __init__(self, model, memory, processor):
        self.memory = memory
        self.processor = processor
 
    def price(self):
        return (self.memory * self.processor) / 10
 
macbook = Computer('Macbook Pro 15" 2016', 16, 2400)
print(macbook.price())


numbers = ()
i = 0
while i <= 5:
    numbers.append(i)
    i += 1