class Pet:
    pass

class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if not name:
            raise Exception("Name cannot be empty")
        self._name = name
        self._pets = []

        @property
        def name(self):
            return self._name

        def pets(self):
            return self._pets

        def add_pet(self, pet):
            if not isinstance(pet, Pet):
                raise Exception("pet must be an instance of Pet")
            if pet not in self._pets:
                self._pets.append(pet)
                pet.owner = self

        def get_sorted_pets(self):
            return sorted(self._pets, key=lambda pet: pet.name)