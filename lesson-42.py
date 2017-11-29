# Animal is-a object(yes, sort of connfusing) look at the extra credit
class Animal(object):
    pass


# is-a
class Dog(Animal):
    def __init__(self, name):
        # has-a
        self.name = name


# is-a
class Cat(Animal):
    def __init__(self, name):
        # has-a
        self.name = name


# is-a
class Person(object):
    def __init__(self, name):
        # has-a
        self.name = name
        # Person has-a pet of some kind
        self.pet = None


# is-a
class Employee(Person):
    def __init__(self, name, salary):
        # has-a hmm what is this strange magic?
        super(Employee, self).__init__(name)
        # has-a
        self.salary = salary


# is-a
class Fish(object):
    pass


# is-a
class Salmon(Fish):
    pass


# is-a
class Halibut(Fish):
    pass


# rover is-a dog
rover = Dog('Rover')

# satan is-a cat
satan = Cat('Satan')

# Mary is-a person
mary = Person('Mary')

# Mary has-a pet name satan
mary.pet = satan

# frank is-a employee and his salary is 12000
frank = Employee('Frank', 12000)

# frank's pet is rover
frank.pet = rover

# is-a
flipper = Fish()

# is-a
crouse = Salmon()

# is-a
harry = Halibut()


# creat a class
class Student(object):
    # declare a specia method __init__
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # declare a function
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    # declare another function
    def get_grade(self, score):
        if self.score >= 90:
            return 'A'
        elif self.score >=80:
            return 'B'
        else:
            return 'C'


# create a instance name bart and take two argument 'Bart Simpson', 59
bart = Student('Bart Simpson', 59)
# bart call the method print_score
bart.print_score()

print(bart.get_grade(100))
