class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if not name:
            raise Exception("Name cannot be empty")
        if pet_type not in self.PET_TYPES:
            raise Exception("pet_type must be one of: " + ", ".join(self.PET_TYPES))
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("owner must be an instance of Owner")
        
        self._name = name
        self._pet_type = pet_type
        self._owner = owner
        if owner is not None:
            owner.add_pet(self)  # Automatically add this pet to the owner's _pets list
        Pet.all.append(self)

    @property
    def name(self):
        return self._name
    
    @property
    def pet_type(self):
        return self._pet_type
    
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, value):
        if value is not None and not isinstance(value, Owner):
            raise Exception("owner must be an instance of Owner")
        self._owner = value
        
        

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