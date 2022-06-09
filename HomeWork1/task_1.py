phrase_1 = input("Введите строку 1: ")
phrase_2 = input("Введите строку 2: ")

def len_diff(str1, str2):
    if len(str1) > len(str2):
        print("Фраза 1 длиннее фразы 2")
    elif len(str1) < len(str2):
        print("Фраза 2 длиннее фразы 1")
    else: print("Фразы равной длины")
pass
print("task_1 ----->")
len_diff(phrase_1, phrase_2)
