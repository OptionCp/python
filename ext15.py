from sys import argv

script, filename = argv
txt = open(filename)
print(f"here's your file {filename}")
print(txt.read())

print("type the filename agagin ")
fileAgain = input('>')
txtAgain = open(fileAgain)

print(txtAgain.read())