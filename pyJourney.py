def displayMenu():
    print('1.Stats')
    print('2.Inventory')
    menu = input('Please Enter Menu Option: ')
    return menu

letPlay = 1
while letPlay == 1:

    playerStrength = 1
    playerToughness = 1
    playerDexterity = 1
    playerPerception = 1 
    
    playerBlood = 100
    playerHead = 100
    playerTorso = 100
    playerLeftArm = 100
    playerRightArm = 100
    playerLeftLeg = 100
    playerRightLeg = 100

    armourHead = 0
    armourTorso = 0
    armourLeftArm = 0
    armourRightArm = 0
    armourLeftLeg = 0
    armourRightLeg = 0 

    maxWeight = (19 + (1 * playerStrength))



    menu = displayMenu()
    if menu == 1:

    elif menu == 2:
    