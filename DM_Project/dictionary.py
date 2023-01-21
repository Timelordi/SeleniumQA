#list = []
#tuple = ()
#dictionary = {}

Cities = {1:"Dallas",2:"Addisson", 3:"Carrollton", 4:"Frisco",5:"Garland", 6:["Siski", "Piski"], 7:("Nos", "Hvost")}

#print(Cities[7][0])

Item = {"Type":"Vehicle",
        'CC':"1500",
        "Wheels":"4",
        "Model":"Land Rover"}
#print(Item)

for key, value in Item.items():
    print(key + " - " + value)

Towns = {1:"Dallas",2:"Addisson", 3:"Carrollton", 4:"Frisco",5:"Garland", 6:["Siski", "Piski"], 7:("Nos", "Hvost")}
#print(Towns.get(6))


