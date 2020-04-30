""" coded Triangle numbers """

i = 1
# lst_1 for append calculated triangle numbers
lst_1 = []
# while loop for get only 100 triangle numbers
while i <= 100:
    # formula for get triangle number
    series = 1/2 * i * (i + 1)
    lst_1. append(int(series))
    i += 1

# get input from user(a word)
word = input("Enter a word: ").lower()
# lst_2 for append equal values of number  from given word
lst_2 = []
# dictionary for pick the assigned value for each letter in word
alphabets = {
        "a" : "1",
        "b" : "2",
        "c" : "3",
        "d" : "4",
        "e" : "5",
        "f" : "6",
        "g" : "7",
        "h" : "8",
        "i" : "9",
        "j" : "10",
        "k" : "11",
        "l" : "12",
        "m" : "13",
        "n" : "14",
        "o" : "15",
        "p" : "16",
        "q" : "17",
        "r" : "18",
        "s" : "19",
        "t" : "20",
        "u" : "21",
        "v" : "22",
        "w" : "23",
        "x" : "24",
        "y" : "25",
        "z" : "26"
}

for ch in word:
    lst_2.append(int(alphabets.get(ch)))
n = sum(lst_2)
if n in lst_1:
    # count for know the position of total word in triangle numbers
    count = 0
    for i in lst_1:
        if i != n:
            count += 1
            pass
        else:
            break
    print("Your total word value is ", n, "it's the value of ", count+1, "triangle number")
    print('Your word is a "Triangle word"')
else:
    print('Your word is "Not a triangle word"')
