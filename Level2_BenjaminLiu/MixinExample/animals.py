# Putting everything in a single file, for simplicity (in practice, should separate into modules).

# Using naive string formatting, since we have not yet learned about string formatting.

class Animal(object):
    '''
    The abstract Animal base class -- it should never be instantiated directly.
    It's 'abstract' since there is a function that raises a NotImplementedError().
    However, unlike C++, this is not enforced.
    '''
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def eat(self):
        # This will call the correct derived-class' primaryFood function!
        print self._name + ' is eating ' + self.primaryFood() + '.'

    def sleep(self):
        print self._name + ' is sleeping.'

    def weight(self):
        '''
        :return: The weight if this animal.
        For almost every animal type, this is straightforward, so we can define this in the base class.
        See WingedAnimalMixin for the exception to this rule.
        '''
        return self._weight

    def primaryFood(self):
        '''
        This should be overridden in the derived classes.
        :return: A name of a food.
        '''
        raise NotImplementedError()

class TailedAnimalMixin(object):
    '''
    Mixin class for tailed animals. Note how the class does *not* derive from Animal.
    However, it is meant to be 'mixed into' a class that does derive from Animal.
    Mixin classes should almost never be instantiated directly (i.e. p TailedAnimalMixin() is wrong).
    This avoids the diamond inheritance problem (see other example).
    '''
    def __init__(self, name, weight, tailLength):
        # Animal.__init__(self, name) # Old syntax. Super is preferred.
        # This calls super despite the fact that this is not a derived class from Animal.
        # The reason for this is that this mixin class is expected to be mixed-into
        # a class that does derive from Animal. Hence, we call super here to ensure
        # that the Animal __init__ gets called after this one.
        super(TailedAnimalMixin, self).__init__(name, weight)
        self._tailLength = tailLength

    def wagTail(self):
        '''
        Function specific to tailed animals.
        '''
        print self._name + ' wagged its ' + str(self._tailLength) +  ' inch tail!'

class WingedAnimalMixin(object):
    '''
    Mixin class for winged animals. Note how the class does *not* derive from Animal.
    However, it is meant to be 'mixed into' a class that does derive from Animal.
    This avoids the diamond inheritance problem (see other example).
    '''
    def __init__(self, name, weight, wingSpan):
        # Animal.__init__(self, name)

        # Same comment as for TailedAnimalMixin
        super(WingedAnimalMixin, self).__init__(name, weight)
        self._wingSpan = wingSpan

    def fly(self):
        '''
        Function specific to winged animals.
        '''
        self._isFlying = True
        print self._name + ' is flying with its ' + str(self._wingSpan) + ' wing span!'

    def land(self):
        self._isFlying = False
        print self._name + 'landed.'

    def weight(self):
        '''
        This overrides the (expected) base class, since when an animal is flying, it's weightless.
        HINT: We will use a similar mechanism for PMI when writing MortgageMixin in the exercises.
        '''
        # Get the weight from the base class.
        # This is better than duplicating the code contained in the base class version.
        weight = super(WingedAnimalMixin, self).weight()

        # Winged-animal specific logic
        return weight if self._isFlying else 0.0

class PetMixin(object):
    '''
    Mixin class for pets. Note how the class does *not* derive from Animal.
    However, it is meant to be 'mixed into' a class that does derive from Animal.
    '''
    # Notice how there is no __init__ function here,
    # as there is nothing we wish to initialize specific to pets.

    def takeToVet(self):
        '''
        Function specific to pets.
        '''
        print self._name + 'is ill.'

####################################
class Dog(PetMixin, TailedAnimalMixin, Animal):
    '''
    A dog is a tailed pet. Hence, it derives from the two mixin classes first, then Animal.
    '''
    def __init__(self, name, weight, tailLength, breed):
        '''
        This __init__ function overrides all the __init__ functions in its base classes.
        The call to 'super' resolves to whichever base class has an __init__ function,
        when reading from left to right. It first checks PetMixin for an __init__ function.
        Since it does not have one, it then checks TailedAnimalMixin.
        TailedAnimalMixin has an __init__ function, so that one is called.
        See the comment in TailedAnimalMixin's __init__ function regarding what happens once it is called.
        '''
        super(Dog, self).__init__(name, weight, tailLength)
        self._breed = breed

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed):
        self._breed = breed

    def bark(self):
        '''
        Dog-specific function.
        '''
        print 'Woof!'

    def primaryFood(self):
        '''
        Overrides the base class. This ensures that the common 'eat' function works correctly.
        '''
        return 'biscuits'

class Bat(WingedAnimalMixin, Animal):
    # Nothing to initialize specifically for Bats,
    # so the first __init__ function in the above base class list is called.
    # Since WingedAnimalMixin has an __init__, it is called.
    # However, WingedAnimalMixin's __init__ itself calls super, which calls Animal's __init__.
    def hangUpsideDown(self):
        '''
        Bat-specific function.
        '''
        print self._name + ' is hanging upside down in a cave.'

    def primaryFood(self):
        '''
        Overrides the base class. This ensures that the common 'eat' function works correctly.
        '''
        return 'mosquitoes'