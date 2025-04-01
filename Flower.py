#Michael Siggers
#3/31/25
#This code creates and uses 3 different flowers using OOP
class Flower:
    def __init__(self, name):
        self.name = name #Gives the flower a name attribute

    def grow(self):
        print("The " +self.name + " is growing.") #When the method runs, the flower will begin growing

    def bloom(self):
        print("The " + self.name + " is blooming.") #when this method runs, the flower will then start blooming

def main():
    flower1 = Flower("Rose") #Assigns "Rose" to the name attribute of the first flower
    flower1.grow() #Uses the grow method to grow the rose flower
    flower1.bloom() #Uses the bloom method to bloom the rose flower
    flower2 = Flower("Daisy") #Assigns "Daisy" to the name attribute of the second flower
    flower2.grow() #Uses the grow method to grow the daisy flower
    flower2.bloom() #Uses the bloom method to bloom the daisy flower
    flower3 = Flower("Poppy")
    flower3.grow()
    flower3.bloom()

if __name__ == "__main__":
  main() #Calls the "Main" function to create the new flowers