with open('test.txt','r') as f:
    file=f.read()
with open('testcopy.txt','r') as f:
    filecheck=f.read()

if (file==filecheck):
    print('files are same')
else:
    print('files are not same')