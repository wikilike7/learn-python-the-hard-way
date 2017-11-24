class Mystuff(object):
    def __init__(self):
        self.tangerine = 'And now a thousand years between'

    def apple(self):
        print('I AM CLASSY APPLES!')


thing = Mystuff()
thing.apple()
print(thing.tangerine)


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(['Happy birthday to you',
                   'I don\'t want to get sued',
                   'So i\'ll stop right there'])

bulls_on_parade = Song(['They rally around the family',
                       'With pockets full of shells'])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


class City(object):
    def __init__(self, people, cars):
        self.people = people
        self.cars = cars

    def print_people_cars(self):
        print('In city we have %s people and %s cars' % (self.people, self.cars))


result = City(1000, 200)
result.print_people_cars()
