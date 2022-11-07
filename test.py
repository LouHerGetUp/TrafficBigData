l = []
f = open("LINE.txt", encoding='gbk')             # 返回一个文件对象
line = f.readline()             # 调用文件的 readline()方法
while line:
    l.append(line)       # 在 Python 3中使用
    line = f.readline()

f.close()
print(l)

for i in range(len(l)):

    if str(l[i])[0] == 'L':
        print(l[i])