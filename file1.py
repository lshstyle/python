try:
    with open(r'../test/file/123.txt') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('File does not exist')
except PermissionError:
    print('Permission denied')