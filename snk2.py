file=open("Encrypted_file.txt","w")
with open("file2.txt") as f:
    cc=f.read()
    for c in cc: file.write(chr((ord(c)-97+2)%26+97)) if (c in 'aeiou') else (file.write(chr((ord(c)+3-97)%26+97)) if(c in 'bcdfghjklmnpqrstvwxyz') else file.write(' '))
file.close()