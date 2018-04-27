
#lists

players = ["gk", "md", "cf", "mf"]

#change list values

players[0] = "ngk"

#add list temporally
print(players + ["ff", "lf"])

print(players)

#permament add
players.append("nff")
print(players)

#print list
print(len(players))
#slicing
print(players[2:5])
#delete elements
players[0] = []
print(players)
players[:] = []
print(players)

#shopping
groceries = {'cereal', 'milk', 'sandwich', 'yogurt', 'lotion', 'beer'}
print(groceries)

if 'milk' in groceries :
    print("You already have milk")
else:
    print("oh yeah, you need milk")

#dictionary

classmates = {'Tony': 'A male given name', 'Vivian':'A female given name', 'max': 'snabbt mat foretag i Sverige'}

print(classmates)
for k, v in classmates.items():
    print(k , v)

#print particular entry in dictionary
print(classmates['Tony'])
print(classmates['Vivian'])
print(classmates['max'])