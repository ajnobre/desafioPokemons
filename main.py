#!/usr/bin/env python

def move(currPos, direction):
    match direction:
        case "E":
            currPos[0] -=1
        case "W":
            currPos[0] +=1
        case "S":
            currPos[1] -= 1
        case "N":
            currPos[1] +=1
        
def checkCaught(pastPostions, currPos):
    caught = 0
    currPosKey = str(currPos[0]) + "," +str(currPos[1]) 
    if currPosKey not in pastPostions:
        pastPostions.add(currPosKey)
        caught = 1
    return caught
    
if __name__ == '__main__':

    moves = input().strip()

    currPos = [0,0]
    pastPostions = {"0,0"}
    totalCaught= 1

    for m in moves:
        move(currPos, m)
        totalCaught += checkCaught(pastPostions, currPos)

    print(totalCaught)

