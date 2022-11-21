file = open('.\\07-FileHandling\\countries.txt', 'r')
file_content = file.read()
print(file_content)
file.close()