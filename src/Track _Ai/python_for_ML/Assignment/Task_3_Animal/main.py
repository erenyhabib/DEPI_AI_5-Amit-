from Dog import Dog
from Cat import Cat
from Cow import Cow


dog = Dog()
cat = Cat()
cow = Cow()

print("Dog:")
print(dog.make_sound())
dog.describe()

print("\nCat:")
print(cat.make_sound())
cat.describe()

print("\nCow:")
print(cow.make_sound())
cow.describe()