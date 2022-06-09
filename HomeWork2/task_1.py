word = input("Enter string:")
word_leng = len(word)
if word_leng % 2 == 0:
    start = word_leng//2 - 1
    print("result:", word[start:start+2])
else:
    print("result:", word[word_leng//2])