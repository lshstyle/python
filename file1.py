try:
    with open(r'E:/pythonProject/test/file/123.txt', mode='a') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('File does not exist')
except PermissionError:
    print('Permission denied')