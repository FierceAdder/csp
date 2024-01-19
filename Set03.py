F1=open("Story.txt", 'r') 
F2=open("Vaasavi.txt", 'w') 
S=F1.readlines()
for i in S:
    if i[0]=='V': 
        F2.write(i)
print("Written Successfully")
F1.close()
F2.close()