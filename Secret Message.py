def find_message(text):
    ans=""
    for t in text:
        if t == t.upper() and t.isalpha():
            ans +=t
        return ans
find_message = lambda text: "".join([t for t in text if t == t.upper() and t.isalpha()])


beispiel="Wo bist Du, Du geiler Mann?"

print (find_message(beispiel))

def find_message(s):
    result = []
    for c in s:
        if c.isupper():
            result.append(c)
    return "".join(result)

beispiel="Wo bist Du, Du geiler Mann?"

print (find_message(beispiel))


find_message2 = lambda s: "".join ([c for c in s if c.isupper()])
print (find_message2("How are you? Eh, ok. Lower or Lower"))
