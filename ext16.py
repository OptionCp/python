from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print(f"If you don't want to erase, plesase hit ctrl-c(^C)")
print(f"If you want to do it, hit return")

input("?")

print(f"opening the file...")
target = open(filename, 'w') #打开文件，若无此文件会自动新建该文件
print("Truncating the file. Goodbye")
target.truncate() #清空文件，当文件以‘w’方式打开时，写入会自动清空文件内的所有内容，若不删除原有内容的话，需要使用'a'来进行追加

print("i'm going to ask you for three lines")


line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("i'm going to write these to the file")

line4 = line1 + '\n' + line2 + '\n' + line3 + '\n'

target.write(line4)
target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("and finally, we close it ")
content = open(filename)
print(content.read())
target.close()