class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run(self):
        print('Dog is running')

class Cat(Animal):
    def run(self):
        print('Cat is running')

def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Animal())
run_twice(Dog())
dog = Dog()
print(isinstance(dog, Cat))
print(isinstance('sd', object))


class Student(object):
    count = 0

    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
        Student.count += 1

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            self.__gender = 'Wrong'

bart = Student('Bart', 'male')
print(bart.get_gender())
bart.set_gender('fffmael')
print(bart.get_gender())
bart.set_gender('female')
print(bart.get_gender())
lisa = Student('Lisa', 'female')
print(Student.count)
