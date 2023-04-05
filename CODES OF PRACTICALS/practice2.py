nm = input("enter name :- ")

chk = False

while chk != True :
    for i in nm :
        jck = ord(i)
        if (jck >= 65 and jck <=90) or (jck >= 97 and jck <=122) :
            chk = True
        else :
            nm = input("enter corregct name :- ")
            chk = False
            break
chk = False
add = input("enter address :- ")
while chk != True :
    for i in add :
        jck = ord(i)
        if (jck >= 65 and jck <=90) or (jck >= 97 and jck <=122) or (jck >= 48 and jck <=57):
            chk = True
        else :
            nm = input("enter corregct add :prav- ")
            chk = False
            break