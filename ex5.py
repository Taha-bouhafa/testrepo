def reverse(mot):
    c=[]
    for i in mot:
        c.append(i)
    result=""
    while c:       
     result+=c.pop()
    print(f"l'inverse du mot {mot} est : {result}")
chaine=input("Veuillez entre le mot : ")
reverse(chaine)
