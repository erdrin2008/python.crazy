class Vertebrate():
    def __init__(self, backbone=True):
        self.has_Backbone=backbone
    def vertebrate_info(self):
        print("vertebrates have a backbone")


class Aquatic:
    def __init__(self, habitat="water"):
        self.habitat=habitat
    def aquatic_info(self):
        print("aquatic live on the water is super easy to understand just by the name")

class Fish(Vertebrate,Aquatic):
    def __init__(self,species, backbone=True,habitat="water"):
        super().__init__(backbone=backbone)
        self.species=species
        self.habitat=habitat
    def fish_info(self):
        print(f"the{self.species} is a type of fish found in {self.habitat}")
    def swim(self):
        print("the fish is swimming? aint that considered walking for them?")

goldfish=Fish("Goldfish")
print(goldfish.has_Backbone)
print(goldfish.habitat)
goldfish.vertebrate_info()