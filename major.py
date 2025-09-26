import re;

def replaceLetters(words: list[str]) -> list[str]:
    cutWords = []
    for word in words:
        word = re.sub(r'(?<![pt])h(?!\w)', '', word)
        word = word.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '').replace('w', '')
        cutWords.append(word)
    return cutWords

def makeNumberCode(word):
        word = word.lower()
        result = []
        i = 0
        while i < len(word):
            found = False
            if i+1 < len(word):
                two_chars = word[i:i+2]
                for idx, sounds in enumerate(majorLetters):
                    if two_chars in sounds:
                        result.append(str(idx))
                        i+=2
                        found = True
                        break
            
            if not found:
                one_char = word[i]
                for idx, sounds in enumerate(majorLetters):
                    if one_char in sounds:
                        result.append(str(idx))
                        i+=1
                        found = True
                        break
            
            if not found:
                i+=1
            
        return ''.join(result)

def bold_text(text):
    return f"\033[1m{text}\033[0m"

n = input("Geben Sie eine Zahl ein: ")

majorLetters = [["s","z"],
                ["t","d","th"],
                ["n"],
                ["m"],
                ["r"],
                ["l"],
                ["j","ch","sh"],
                ["c","k","g","q","ck"],
                ["v","f","ph"],
                ["p","b"]]

words = ["waterline", "rline","banana", "hello", "photograph", "thought", "check", "shakespeare", "llaaaa", "jeremiah"]

cutWords = replaceLetters(words)
possibleLongWords = []
possibleShortenedWords = []

for word in cutWords:   
    result = makeNumberCode(word)
    if result == str(n):
        idx = cutWords.index(word)
        #print(words[idx], end="\n-----\n")
        possibleLongWords.append(words[idx])

print(bold_text("Long words:"))
for word in possibleLongWords:
    print(word)

for word in cutWords: #waterline
    result = makeNumberCode(word) #1452
    if result == str(n)[1:]:
        idx = cutWords.index(word)
        #print(words[idx], end="\n-----\n")
        possibleShortenedWords.append(words[idx])

print(bold_text("Shortened words:"))
for word in possibleShortenedWords:
    print(word)