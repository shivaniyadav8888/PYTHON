a=input("Enter your Name:")
Vowel=0
Cons =0
for i in range(0,len(a)):
    if(a[i]!=' '):
     if(a[i]=='a') or (a[i]=='e')or (a[i]=='i') or(a[i]=='o')or (a[i]=='u')or(a[i]=='A')or(a[i]=='E')or(a[i]=='i')or(a[i]=='O')or(a[i]=='U'):
        Vowel=Vowel+1
    else:
        Cons=Cons+1
print("Total Vowels=",Vowel)
print("Totel Cons=",Cons)
