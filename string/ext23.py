import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):      
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()#strip的作用是去掉文件每行后面的\n使得打印出来不会空一行
    raw_bytes = next_lang.encode(encoding, errors = errors)#encode将文件内容编码成字节串
    cooked_string = raw_bytes.decode(encoding, errors = errors)#decode将字节串内容解码成字符串
    #test = cooked_string.encode(encoding, errors = errors)
    #print(test, raw_bytes)

    print(raw_bytes, "<===>", cooked_string)


languages = open("language.txt", encoding = "utf-8")
print(languages)

main(languages, encoding, error)