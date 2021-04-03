# Статические методы

class My_class:
    color = 'red'
    year = 1990
    def some_method(self):
        print('method is working')
    @ staticmethod
    def static_method():
        print('method is working')



myex = My_class()

myex.size = 'big'
print(myex.size)
My_class.size = 'small'
print(My_class.size, myex.size)

# у  класса и экземпаляра свои области видимости

My_class.some_method(My_class)
myex.some_method()
My_class.static_method()
myex.static_method()