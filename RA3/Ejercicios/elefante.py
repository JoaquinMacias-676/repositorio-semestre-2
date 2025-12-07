class Animal:
    def walk(self):
        print("El animal está caminando")
    
class LightweightAnimal(Animal):
    def jump(self):
        print("El animal está saltando")

class Dog(LightweightAnimal):
    pass

class Elephant(Animal):
    pass

def jump_hole(animal: LightweightAnimal):
    animal.walk()
    animal.jump()
    animal.walk()

dog = Dog()
elephant = Elephant()

jump_hole(dog)

# No funcionará, ya que no admite al elefante
#jump_hole(elephant)