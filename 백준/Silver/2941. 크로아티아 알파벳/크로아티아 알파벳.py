alist = ['c=','c-','dz=','d-','lj','nj','s=','z=']

string = input()

count = 0

for i in alist:
   if i in string:
       string = string.replace(i," ")

print(len(string))