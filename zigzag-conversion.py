numRows = 1
s = "ABC"

StringPositionCounter = 0 # reconrds position along input string
IndexPosition = 0 # records position in index array for placement of letters
DirectionBool = True #true is down, false is up
temp = []
output = str()
for i in range(numRows):
    temp.append([])
    # creates empty array of numRow size
print(temp)
print("s:",s)
print("len(s):",len(s))
print("numRows:",numRows)
while StringPositionCounter<len(s):
    temp[IndexPosition] += s[StringPositionCounter]
    StringPositionCounter += 1        
    if numRows > 1:
        if DirectionBool:
            IndexPosition += 1
            if IndexPosition >= numRows:
                IndexPosition = numRows-2
                DirectionBool = False
            else:
                pass
        else:
            IndexPosition -= 1
            if IndexPosition < 0:
                IndexPosition = 1
                DirectionBool = True
            else:
                pass
    else:
        IndexPosition = 0

for k in range(0,numRows):
    for j in range(len(temp[k])):
        output += temp[k][j]
    print(temp[k],len(temp[k]))
        
print(output)