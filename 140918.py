words = ['икра', 'котик', 'дота','аорта', 'сложнота']
preffix = dict()
count = 0
for word in words:
    for i in range(len(word)):
        preffix[word[:-i]] = word

for word in words:
    for i in range(len(word)):
        if len(word[-i:]) > count and word[-i:] in preffix.keys():
            count = len(word[-i:])
            w1 = word
            w2 = preffix[word[:-i]]
            second = (word, preffix[word[:-i]])


print(w1, w2)
print(second)
print(count)
print(preffix)



def mymethod(words):
    count = 0
    for word in words:
        for i in range(len(word)):
            pattern = word[:-i]
            for secondword in words:
                #print(word[:-i] == secondword[-len(word):])
                #if word[:-i] == secondword[-len(word):]:
                if len(pattern) > count and len(pattern)<len(secondword) and pattern == secondword[-len(pattern):]:
                    count = len(pattern)
                    print(word, secondword)


mymethod(words)