"""""
You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence.

Input: a list of strings.

Output: a string.

Example:

most_frequent([
    'a', 'b', 'c', 
    'a', 'b',
    'a'
]) == 'a'
most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
"""""


def most_frequent(data):
    return max(data, key=lambda a: data.count(a))




blu=(['a', 'b', 'c', 'a', 'b', 'a'])

print (most_frequent(blu))
