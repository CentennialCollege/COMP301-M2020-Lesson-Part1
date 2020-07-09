#step 1 is open a file
fileObject = open("numbers.txt", "r")

#step 2 - read from the file
contents = fileObject.read()

#step 3 - close out
fileObject.close()


print(contents)


fileObject = open("numbers2.txt", "w+")
numbers = [33, 55, 66, 77, 88, 99, 110, 121]

count = 0

for number in numbers:
    count += 1
    if count == len(numbers):
        fileObject.write(str(number))
    else:
        fileObject.write(str(number) + ",")

fileObject.close()