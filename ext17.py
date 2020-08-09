from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")
in_file = open(from_file)
indata = in_file.read()

if indata:
    print("indata is exist")
else:
    print("indata is empty")

print(f"the input file is {len(indata)} byte long")

print(f"dose the output file exist?{exists(to_file)}")  #exists 检测文件是否存在，返回bool值
print("Ready, hit return to continue, ctrl-c to abort")
input()

out_file = open(to_file, 'a')
out_file.write(indata)

print(f"well the {indata} is writed") #f格式化输出方式

out_file.close()
in_file.close() #由于写入文件由操作系统进行调用，先写入到内存，再在空闲的时候写入到硬盘，故若未使用close方法可能导致写入不全