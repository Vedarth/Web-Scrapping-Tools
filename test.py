def ss(st, tVal):
    #remove items greater than target from list
    cleaned = [c for c in st if c < tVal]
    #sort the list
    cleaned.sort()  

    occurance = 0
    leftIndex = 0
    rightIndex = len(cleaned) - 1
    print("rI length: ", rightIndex)

    while(leftIndex < rightIndex):
        #if target value found
        if cleaned[leftIndex] + cleaned[rightIndex] == tVal:
            print("found!!! ", cleaned[leftIndex], " + ", cleaned[rightIndex])
            #occurance += 1
            leftIndex += 1
            rightIndex += 1
        #else if left index + right index < target increment left index
        elif cleaned[leftIndex] + cleaned[rightIndex] < tVal:
            leftIndex += 1
        #otherwise decrement right index
        else:
            rightIndex -= 1

cities = [18897109, 12828837, 9661105, 6371773, 5965343, 5926800, 5582170, 5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279933, 3095213, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508, 2134411]
target = 101000000 

ss(cities, target)
