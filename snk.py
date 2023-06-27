import string
all_letters=string.ascii_letters
dict={}
cipher_text=[]
file=open("Encrypted_file.txt","w")# to store encrypted string
key=1
for i in range(len(string.ascii_letters)): dict[all_letters[i]]=all_letters[(i+2)%(len(all_letters))] if(all_letters[i] in 'aeiou') else all_letters[(i+key)%(len(all_letters))]
with open("file2.txt") as f: # to encrypt the file string
    c=f.read()
    for char in (c): cipher_text.append(dict[char]) if(char in all_letters) else cipher_text.append(char)
cipher_text="".join(cipher_text)# to convert the list to string
file.write(cipher_text)
print(cipher_text)
file.close()