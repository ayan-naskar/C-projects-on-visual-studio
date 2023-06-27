s=input("Enter the sentence: ")
l=0
for i in s:
    l+=1
flag=1
c=0
mid=l//2
for i in range(0,l):
    if c==mid:
        break
    if s[i]!=s[l-1-i]:
        flag=0
        break
    c+=1
if flag==1:
    print("Yes! It is palindrome")
else:
    print("No! Not a palindrome")