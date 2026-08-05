import random
posture = random.choice(["sitting", "standing"]) 
direction = random.choice(["left", "right", "facing"]) 
distance = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 
print(f"Start State -> Posture: {posture}, Direction: {direction}, Distance:  {distance}")
#second state
if posture=="sitting":
    print("stand up ,nexus")
elif posture=="standing":
    print("nexus is already standing")
#third state
if direction=="left" or direction== "right":
    print("nexus, turns towards the door")
elif direction=="facing":
    print("nexus is already facing the door")
#forth state
while distance:
    print(f"moving... {distance} steps left")
    distance-=1
print("nexus reached the door and opened it")