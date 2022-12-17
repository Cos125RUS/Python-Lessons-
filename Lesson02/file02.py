path = 'C:\\repo\Python\Lessons\Lesson02\\file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()