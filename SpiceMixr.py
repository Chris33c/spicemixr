BlendDict = {}

#add spices into catalogue and write into text file
def AddSpice(spice):
    spice = spice.lower()
    catalogue = open("spice.txt", "w")
    catalogue.write(spice)
    catalogue.close()
#read into catalogue for spices and specify which to mix. return error if not found and prompt user to add spice.

def MixSpice(spice):
    blend = []
    spice = spice.lower()
    catalogue = open("spice.txt", "r")
    if spice in catalogue:
        blend.append(spice)
        print("Spice added to blend")
    else:
        print("Spice not found in catalogue. Add spice to catalogue")
        AddSpice(spice)    
    return blend

#add spices to blend and write into text file

def AddBlend(blendname, blend):
    blendname = blendname.lower()
    BlendDict[blendname] = blend
    

def main():
    print("Welcome to SpiceMixr")
    UserInput = input("Press 1 to add spices to catalogue, 2 to mix spices, 3 to access available spice mixes: ")
    if UserInput == "1":
        spice = input("Enter spice to add to catalogue. Press enter when finished: ")
        while spice != "":
            spice = input("Enter spice to add to catalogue. Press enter when finished: ")
            AddSpice(spice)
        print("Spices added to catalogue")
    if UserInput == "2":
        print("Blend from the following list of spices: ")
        catalogue = open("spice.txt", "r")
        print(catalogue.read())
        spice = input("Enter spice to add to blend. Press enter when finished: ")
        while spice != "":
            spice = input("Enter spice to add to blend. Press enter when finished: ")
            blend = MixSpice(spice)
        blendname = input("Name your blend: ")
        AddBlend(blendname, blend)
        print("Blend added to catalogue")
    if UserInput == "3":
        print("Available spice blends: ")
        print(BlendDict)



main()



#prompt for quanity 

#write mix to file 

#spellcheck for name
