#multiple eshte kur trashegon nga dy klasa perniher
class Vertebrate:
    def __init__(self,backbone=True):
        self.backbone = backbone

        def vertebrate_info(self):
           print("Vertebrate have a backbone")

class Aquatic:
    def __init__(self,habitat="water"):
        self.habitat = habitat

        def aquatic_info(self):
            print("Aquatic animals live in water")

class Fish(Vertebrate,Aquatic):
    def __init__(self,species,backbone=True,habitat="water"):
      super().__init__(backbone=backbone)
      self.habitat = habitat
      self.species = species

    def fish_info(self):
        print(f"The {self.species} is a type of fish found in {self.habitat}")

    def swim(self):
        print("The fish is swimming")

goldfish = Fish("Goldfish")
print(goldfish.backbone)
print(goldfish.habitat)

goldfish.fish_info()
goldfish.swim()

