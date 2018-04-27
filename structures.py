
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
