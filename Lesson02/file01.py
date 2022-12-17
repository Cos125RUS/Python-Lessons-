with open('C:\\repo\Python\Lessons\Lesson02\\file.txt', 'w') as data:
    data.write('text  ')


colors = ['red', 'green', 'blue']
data = open('C:\\repo\Python\Lessons\Lesson02\\file.txt', 'a')
data.writelines(colors)
data.write('\nLINE 2\n')
data.write('LINE 3\n')
data.close()



#exit()
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()