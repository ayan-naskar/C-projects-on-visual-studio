with open("pyfile.txt","w+") as f:
    f.write("hello world")
f.close

with open("pyfile.txt","r+") as f1:
    with open("pyfile2.txt","w+") as f2:
        f2.write(f1.read())
    f2.close
f.close