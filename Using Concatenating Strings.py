#Using Concatenating Strings 
for num in range(1,101):
    string = ""
    if num % 3 == 0:
        string = "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if string == "":
        string = str(num)
    print(string)
