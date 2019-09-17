# Here you need to put an algorithm

print("You can travel: (N)orth")
direction_str = str(input("Direction: "))

if direction_str == "n":
    print("You can travel: (N)orth or (E)ast or (S)outh")
    directionn1_str = str(input("Direction: "))

    if directionn1_str =="n":
        print("You can travel: (E)ast or (S)outh")
        directionn2_str = str(input("Direction: "))
        if directionn2_str == "e":
            print("You can travel: (E)ast or (W)est")
            directionn2e1_str = str(input("Direction: "))

    elif directionn1_str == "e":
        print("You can travel: (N)orth or (W)est)")

    elif directionn1_str == "s":
        print("you can travel: (N)orth")
    
    else:
        print("Not a valid direction!")
else:
    print("Not a valid direction!")