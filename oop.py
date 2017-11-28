class City(object):
    def __init__(self, people, machine, building):
        self.people = people
        self.machine = machine
        self.building = building

    def print_city(self):
        print(self.people, self.machine, self.building)


result = City(123, 456, 'Park plaza')
print(result.print_city())
