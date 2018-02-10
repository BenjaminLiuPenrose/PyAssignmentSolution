# This program is an example of using mixin classes.

import animals

###############################################################

def main():
    # This is wrong, since animal is abstract.
    # However, Python does not prevent you from doing it.
    animal = animals.Animal('Harry', 65)
    # The below will throw an error, since eat() relies on primaryFood(),
    # which is not implemented in the base class.
    # animal.eat()

    # Should never do this.
    # tailedAnimal = animals.TailedAnimalMixin('Rex', tailLength=6.5)

    dog = animals.Dog('Rex', 65, tailLength=6.5, breed='Dalmatian')
    dog.bark()
    dog.eat()
    dog.sleep()
    dog.wagTail()
    print dog.weight()
    dog.takeToVet()

    # Bat itself does not have an __init__, but its first base class (WingedAnimalMixin) does.
    # Hence, we pass in three parameters, to match the signature of WingedAnimalMixin's __init__.
    bat = animals.Bat('Ted', 0.5, wingSpan=1.2)
    bat.fly()
    print bat.weight()
    bat.land()
    print bat.weight()
    bat.eat()
    bat.sleep()
    bat.hangUpsideDown()

#########################################
if __name__ == '__main__':
    main()