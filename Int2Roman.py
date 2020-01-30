num = 3999
charlookup = ["I","V","X","L","C","D","M"]
numlookup = [1,5,10,50,100,500,1000]
textoutput = ""
for i in range(0,len(numlookup)):
    if i == 1 and num >= 900:
        textoutput += "CM"
        num -= 900
    if i == 2 and num >= 400:
        textoutput += "CD"
        num -= 400
    if i == 3 and num >= 90:
        textoutput += "XC"
        num -= 90
    if i == 4 and num >= 40:
        textoutput += "XL"
        num -= 40
    if i == 5 and num >= 9:
        textoutput += "IX"
        num -= 9
    if i == 6 and num >= 4:
        textoutput += "IV"
        num -= 4
    while numlookup[len(numlookup)-1-i]<=num:
        textoutput += charlookup[len(numlookup)-1-i]
        num -= numlookup[len(numlookup)-1-i]

print(textoutput)
