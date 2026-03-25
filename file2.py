file = open('hello.txt', 'r')
print("file in read mode -")
print(file.read())
file.close()

file = open('hello.txt', 'w')
file.write("File in write mode")
file.write("Hi i am a lion")
file.close()

file = open('hello.txt', 'a')
file.write("File in append mode")
file.write("Hi i am a lion")
file.close()

