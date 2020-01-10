import os.path
fileName = 'test.txt'
with open(os.path.join(os.getcwd(), fileName)) as f:
    print(f.read())