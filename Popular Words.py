ss = "When I was One I had just begun When I was Two I was nearly new"
# ss = ss.lower()
# ss = ss.split()
# print (ss)
# count=ss.count
# print (count)


def popular_words(text, words):
    text = text.lower()
    splitted_words = text.split()
    answer = {}
    for word in words:
        answer[word] = splitted_words.count(word)
    return answer


print(popular_words(ss, ["i", "was"]))

from collections import Counter
def mode (l):
    return Counter (l).most_common(1)[0][0]
m_c = (1,1,1,1,2,4,5,6)
print (mode(m_c))
