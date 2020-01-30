s = "MDCCCLXXXIV"
if len(s) > 0:
    if len(s) > 0:
        charlookup = ["I","V","X","L","C","D","M"]
        numlookup = [1,5,10,50,100,500,1000]
        outputnum = 0
        lookupcounter = len(charlookup)-1
        while charlookup[lookupcounter] != s[0]:
            lookupcounter -= 1
        i = 0
        while i < len(s):
            while charlookup[lookupcounter] != s[i]:
                lookupcounter -= 1
            if i+1 < len(s):
                #checks for I,X,C mods
                if lookupcounter == 0:
                    if s[i+1] == "V":
                        outputnum += 4
                        i += 2
                    elif s[i+1] == "X":
                        outputnum += 9
                        i += 2
                    else:
                        outputnum += numlookup[lookupcounter]
                        i += 1
                elif lookupcounter == 2:
                    if s[i+1] == "L":
                        outputnum += 40
                        i += 2
                    elif s[i+1] == "C":
                        outputnum += 90
                        i += 2
                    else:
                        outputnum += numlookup[lookupcounter]
                        i += 1
                elif lookupcounter == 4:
                    if s[i+1] == "D":
                        outputnum += 400
                        i += 2
                    elif s[i+1] == "M":
                        outputnum += 900
                        i += 2
                    else:
                        outputnum += numlookup[lookupcounter]
                        i += 1
                else:
                    outputnum += numlookup[lookupcounter]
                    i += 1
            else:
                outputnum += numlookup[lookupcounter]
                i += 1
        
        
        print("solution:")
        print(outputnum)
