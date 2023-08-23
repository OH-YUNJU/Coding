n = int(input())
people = {}
li = []

for i in range(n):
    name, log = input().split()
    people[name] = log

for key, value in people.items():
    if value == "enter":
        li.append(key)

li = sorted(li, reverse=True)
for i in range(len(li)):
    print(li[i])
