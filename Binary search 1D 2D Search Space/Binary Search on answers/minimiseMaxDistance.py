def minimiseMaxDistance(arr, k):
    newStationPlacement = [0] * (len(arr) - 1)

    for gasStation in range(k):
        maxDist = -1
        maxIndex = -1
        for j in range(len(arr)-1):
            distance = arr[j+1] - arr[j]
            if maxDist < distance/(newStationPlacement[j] + 1):
                maxDist = distance/(newStationPlacement[j] + 1)
                maxIndex = j

        newStationPlacement[maxIndex] += 1

    maxDist = -1
    for i in range(len(arr)-1):
        distance = (arr[i+1] - arr[i])/(newStationPlacement[i] + 1)
        if maxDist < distance:
            maxDist = distance

    return maxDist

arr = [1, 4, 6, 10, 11] 
k = 1

minimiseMaxDistance(arr, k)