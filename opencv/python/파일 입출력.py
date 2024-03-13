import os

print(os.getcwd())
path='/'
fp=open(path)
str=fp.read()
print(str, end="")
fp.close()