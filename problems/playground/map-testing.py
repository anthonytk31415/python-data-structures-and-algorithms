
from heapq import nlargest, nsmallest

arr = [1,3,2,8,5,10]
arr1 = list(map(lambda x: x + 1, arr))

print(arr1)


words = "1 100 2 333 44 5555"
words0 = words.split()
print(words0)
words1 = list(map(int, words.split()))
words2 = [int(x) for x in words0]
print(words1)
print(words2)



nlargestTest = nlargest(4, arr)
nsmallestTest = nsmallest(4, arr)

print("nlargest: ", nlargestTest)
print("nsmallest: ", nsmallestTest)

x = "13 7 8 9 \n"
data0 = list(map(int, x.split()))
data1 = [int(y) for y in x.split()]

print(data0, data1)

# use input to get the line and get the string
# use split 

a = ["clem", "is", "the", "world", "champ"]
b = " ".join(a)
print(b)




