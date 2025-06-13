#DECLARE Animal: ARRAY[0:19] OF STRING
#DECLARE Colour: ARRAY[0:9] OF STRING
#DECLARE AnimalTopPointer,ColourTopPointer:INTEGER
# Initialization
Animal = [""] * 20
Colour = [""] * 10
AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DataToPush):
    global AnimalTopPointer, Animal
    if AnimalTopPointer == len(Animal):
        print("Animal Stack Overflow")
        return False
    Animal[AnimalTopPointer] = DataToPush
    AnimalTopPointer += 1
    return True

def PopAnimal():
    global AnimalTopPointer, Animal
    if AnimalTopPointer == 0:
        print("Animal Stack Underflow")
        return ""
    AnimalTopPointer -= 1
    return Animal[AnimalTopPointer]

def PushColour(DataToPush):
    global Colour, ColourTopPointer
    if ColourTopPointer == len(Colour):
        print("Colour Stack Overflow")
        return False
    Colour[ColourTopPointer] = DataToPush
    ColourTopPointer += 1
    return True

def PopColour():
    global ColourTopPointer, Colour
    if ColourTopPointer == 0:
        print("Colour Stack Underflow")
        return ""
    ColourTopPointer -= 1
    return Colour[ColourTopPointer]

def ReadData():
    global Animal, Colour
    with open("AnimalData.txt") as myfile:
        for line in myfile:
            PushAnimal(line.strip())
    with open("ColourData.txt") as myfile_2:
        for line in myfile_2:
            PushColour(line.strip())

def OutputItem():
    Animal_returned = PopAnimal()
    Colour_returned = PopColour()
    if Colour_returned=="":
        if Animal_returned:
            PushAnimal(Animal_returned)
        print("No colour")
    elif Animal_returned=="":
        if Colour_returned:
            PushColour(Colour_returned)
        print("No animal")
    else:
        print(f"{Colour_returned} {Animal_returned}")

# Execution
ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()