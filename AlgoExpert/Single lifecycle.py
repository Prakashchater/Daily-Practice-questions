# O(N) time | O(1) space
def hassinglecycle(array):
    elevisited=0
    currIdx=0
    while elevisited < len(array):
        if elevisited > 0 and currIdx == 0:
            return False
        elevisited +=1
        currIdx = getnextidx(currIdx,array)
    return currIdx == 0
def getnextidx(currIdx, array):
    jump= array[currIdx]
    nextidx= (currIdx +jump) % len(array)
    return nextidx if nextidx >=0 else nextidx + len(array)


