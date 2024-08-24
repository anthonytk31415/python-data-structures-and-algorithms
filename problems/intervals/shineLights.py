from heapq import heappush, heappop, heapify 


def shineLights(lights): 
    lights = [[light, False] for light in lights]
    heapify(lights)

    print(lights)

    res = 0
    while lights: 
        print(lights)
        curLight = heappop(lights)
        curInterval, overlap = curLight
        x0, x1 = curInterval
        if not overlap and (not lights or x1 < lights[0][0][0]):
            res += x1 - x0 - 1
        else:         
            topLights = lights[0]
            y0, y1 = topLights[0]
            #equal
            if x0 == y0 and x1 == y1: 
                lights[0][1] = True
            # engorged
            elif x0 < y0 and y1 < x1: 
                heappop(lights)
                heappush(lights, [[y0, y1], True])
                heappush(lights, [[x0, y0 - 1], False])
                heappush(lights, [[y1+1, x1], False])

            elif x0 == y0 and x1 < y1: 
                heappop(lights)
                heappush(lights, [[y0, y1], True])
                heappush(lights, [[y1+1 , x1], True])

            elif y1 == x1 and x0 < x0: 
                heappop(lights)
                heappush(lights, [[y0, y1], True])
                heappush(lights, [[x0 , x1 - 1], False])

            # overlap 
            else: 
                heappop(lights)
                heappush(lights, [[x0, y0 - 1], False])
                heappush(lights, [[y0, x1], True])
                heappush(lights, [[x1 + 1, y1], False])
    return res



# arr = [[-5, 2], [2, 4], [-2, 7]]

arr = [[-5, 2], [2, 4]]



# x = [[[1,2], False], [[3, 7], True], [[1, 3], False], [[2, 3], True]]

# heapify(x)
# while x: 
#     y = heappop(x)
#     print(y)


print(shineLights(arr))