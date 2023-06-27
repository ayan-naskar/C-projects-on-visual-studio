try:
    f = open("demofile.txt")
    f.write("hello world")
except:
    print("Something went wrong when writing to the file")