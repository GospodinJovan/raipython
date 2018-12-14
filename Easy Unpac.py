"""""
Your mission here is to create a function that gets an tuple and returns a tuple with 3 elements - first, third and second to the last for the given array

Input: A tuple, at least 3 elements long.

Output: A tuple.


easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
easy_unpack((6, 3, 7)) == (6, 7, 3)"""""



def easy_unpack(t):
    tup2 = (t[0],t[2], t[-2])
    return (tup2)

beisp=(6,3,7)
print (easy_unpack(beisp))
