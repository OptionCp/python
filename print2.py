print("mary had a little lamb")
print("it's fleece was white as {}.".format('snow')) #format the {}
print("and everywhere that mary went.")
print("." * 10)

end1 = 'C'
end2 = 'H'
end3 = 'E'
end4 = 'V'
end5 = 'c'
end6 = 'd'

print(end1 + end2 + end3, end = '')
print(end4 + end5 + end6)

formatter = "{} {} {} {}"
print(formatter.format(1,2,3,4))
print(formatter.format(formatter,formatter,formatter,formatter))