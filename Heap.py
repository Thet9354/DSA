# importing "heapq" to implement heap quue
import heapq

# initlaizing list
li = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(li)

# using heapify t convert list into heap
print("The created heap is : ", end="")
print(list(li))

# using heappush() to push elements into heap pushes 4
heapq.heappush(li, 4)

# printing modified heap
print("The modified heap after push is: ", end="")
print(list(li))

#using heappop() to pop smallest element
print("The popped and smallest element is: ", end="")
print(heapq.heappop(li))