f1 = open("searchtext.txt", 'r', -1, "utf-8")

f2 = open("translatetext.txt", 'r', -1, "utf-8")
t2 = f2.read()

t2copy = t2.replace("\\n", "\n")
f2.close()
f2 = open("translatetext.txt", 'w', -1, "utf-8")
f2.write(t2copy)
f2.close()

f2 = open("translatetext.txt", 'r', -1, "utf-8")

while True:
    line = f1.readline()
    if not line: break
    print(line)
    line = f2.readline()
    if not line: break
    print(line)

rest1 = f1.read()
rest2 = f2.read()
print(rest1)
print(rest2)

f1.close()
f2.close()
