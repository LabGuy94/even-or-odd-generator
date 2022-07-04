count = int(input("Enter the highest number to check"))


f = open("file.py", "w")
f.write("number = int(input('What is your number '))\n")

for i in range(0, count + 1):
    if i % 2 == 0:
        f.write("\nif number == " + str(i) + ":\n   print('Your number is even')")
    else:
        f.write("\nif number == " + str(i) + ":\n   print('Your number is odd')")
        
f.close()
