katea = "{[()]}"
kontagailua = 0
for i in range(len(katea)):
    if (i == 0) or (i == 5) and (katea[i] == "{" or katea[i] == "}"):
        kontagailua += 1
    elif (i == 1) or (i == 4) and (katea[i] == "[" or katea[i] == "]"):
        kontagailua += 1
    elif (i == 2) or (i == 3) and (katea[i] == "(" or katea[i] == ")"):
        kontagailua += 1

if kontagailua == 6:
    print("Katea ondo balantzeatua dago")
else:
    print("Ez dago ondo balantzeatua")