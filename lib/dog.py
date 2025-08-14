APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer",
    "Blue Tick"   
]

class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            raise ValueError("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed):
        if isinstance(breed, str):
            breeds_list = [b.strip() for b in breed.split(",")]
            if all(b in APPROVED_BREEDS for b in breeds_list):
                self._breed = breed
                return
        raise ValueError("Breed(s) must be in list of approved breeds.")
