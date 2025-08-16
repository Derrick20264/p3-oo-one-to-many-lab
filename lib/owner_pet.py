class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type")

        self.name = name
        self.pet_type = pet_type

        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an Owner instance")

        self.owner = owner

        # Add this instance to Pet.all
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return all pets that belong to this owner"""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Assign this owner to the pet if it's a Pet instance"""
        if not isinstance(pet, Pet):
            raise Exception("Must be a Pet instance")
        pet.owner = self

    def get_sorted_pets(self):
        """Return pets sorted by name"""
        return sorted(self.pets(), key=lambda pet: pet.name)
