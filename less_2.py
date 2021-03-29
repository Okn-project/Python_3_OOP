# Названия классов - с большой буквы
# Анеалог в JS - объекты

class product:
    price = 100
    color = 'red'
    def get_price(self):
        print(self.price)
        return self
    def get_disc(self, disc=0):
        print(self.price - (self.price/100*disc), 'with dics'  )
        return self

product.get_price(product).get_disc(product,10)

# Получить все атрибуты - __dict__

print(product.__dict__, sep = ',')

# Альтернатива
print(getattr(product,  'price', 'параметр по умолчанию, если такого атрибута нет'))

# изменеие атрибутов

product.price = 80
print(product.price)

# создание нового атрибута
product.model = 'bmw'
print(product.model)

# создание нового атрибута сетером. Также может менять имеющиеся атрибуты
setattr(product, 'year', 1990)
print(product.year)

# Удаление атрибутов
delattr(product, 'year')

# Все атрибуты классов автоматически присваюваются всем его экземплярам. То же с удалением.

# NB!!!Все аргументы передаются строкой!!
