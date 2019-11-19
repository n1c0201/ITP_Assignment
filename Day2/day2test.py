invites = ["Hitler", "Obama", "Xi Jinping"]
for i in range(len(invites)):
    print(invites[i] + " is invited ot the party")


print(invites)
name1 = invites.pop(0)
print(name1 + " can't make it he died")

invites.insert(0,"Stalin")
print(invites)

invites.insert(0,"Elvis")
invites.insert(2,"Jason")
invites.append("Ninja")
for i in range(len(invites)):
    print(invites[i] + " is invited to the party")
print("lmao nvm dinner table broke")

bye1 = invites.pop()
print("whoops sorry but you can't come " + bye1)
bye2 = invites.pop()
print("whoops sorry but you can't come " + bye2)
bye3 = invites.pop()
print("whoops sorry but you can't come " + bye3)

locations = ["Christmas Island", "America", "Russia", "Poland", "Australia"]

print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

