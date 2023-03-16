string1 = input("Please type a word: ")
string1_list = list(string1)
string1_list.sort()

string2 = input("Please type another word: ")
string2_list = list(string2)
string2_list.sort()

if string1_list == string2_list:
    print(f"{string1} is an anagram of {string2}.")
else:
    print(f"{string1} is not an anagram of {string2}.")