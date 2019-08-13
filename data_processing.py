list_of_lists = []

with open('data.txt') as file:
    for line in file:
        inner_list = [words.strip() for words in line.split(" ")] 
        list_of_lists.append(list(filter(('').__ne__,inner_list)))

list_of_lists = list(filter(lambda a: len(a) != 0, list_of_lists))

alphabet = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for inner_list in list_of_lists:
    for words in inner_list:
        for characters in words:
            index = ord(characters.lower())-97
            if index in range(26):
                alphabet[index] = alphabet[index] + 1

separator = ""
for i in range(len(list_of_lists)):
    separator += " ".join(list_of_lists[i])
print("Contents of the Data.txt File :")
print(separator)

print("Count of Alphabets : ")
for i in range(26):
    print(chr(i+97), " occurs ", alphabet[i], " times")
    
print("Count of Vowels only : ")
for i in list(filter(lambda a: a in [0,4,8,14,20], range(26))):
    print(chr(i+97), " occurs ", alphabet[i], " times")

print("Count of Consonents only : ")
for i in list(filter(lambda a: a not in [0,4,8,14,20], range(26))):
    print(chr(i+97), " occurs ", alphabet[i], " times")

palindrome = []
for inner_list in list_of_lists:
    for words in inner_list:
        if words[::] == words[::-1] and len(words) != 1:
            palindrome.append(words)

print("No. of Palindrome in the Text file is ",len(palindrome))
print("List of palindromes in the file are : ")
for i in palindrome:
    print(i)
