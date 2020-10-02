rmd3 = 0
rmd5 = 0
print("\t\t\t\t\tWELCOME TO FIZZBUZZ")
print("This program will print the numbers from 1 to 100.\n"
      "But for multiples of three this will print “Fizz” instead of the number and for the multiples of five it will "
      "print “Buzz”.\nFor numbers which are multiples of both three and five it will print “FizzBuzz” \n\n")
a = int(input("Enter the number till you want\n"))
for num in range(1, a+1):
    rmd3 += 1
    rmd5 += 1
    string = ""

    if rmd3 == 3:
        rmd3 = 0
        string = "Fizz"

    if rmd5 == 5:
        rmd5 = 0
        string += "Buzz"

    if string == "":
        string = str(num)

    print(string)
