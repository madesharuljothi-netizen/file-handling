file = open("hello.txt" , "w")

file.write("speedaman")

file.close()



file = open("hello.txt" , "r")

print(file.read())

file.close()



file = open("hello.txt" , "a")

file.write(" I am a fast pace bowler")

file.close()

