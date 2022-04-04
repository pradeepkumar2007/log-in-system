import re
def register():
    db = open("database.txt", "r")
    gmail = input("enter your mail id:")
    password = input("create your password:")
    password1 = input("confirm password:")
    d = []
    f = []
    for i in db:
        a,b = i.split(",")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d,f))
    if password != password1:
        print("password don't match")
        register()
    else:
        if len(password)<5:
            print('your password is too short')
            register()
        elif len(password)>16:
            print("your password is too length you can't remeber is easily")
            register()
        elif not re.search('[a-z]',password):
            print("enter a valid password")
            register()
        elif not re.search('[A-Z]',password):
            print("enter a valid password")
            register()
        elif not re.search('[0-9]',password):
            print("enter a valid password")
            register()
        elif not  re.search('[@#$]',password):
            print("enter a valid password")
            register()
        elif gmail in d:
            print("this mail id already exists")
            register()
        elif "@" not in gmail:
            print("enter a valid mail")
            register()
        elif "@." not in gmail:
            print("enter a valid mail")
            register()
        elif gmail == "@gmail.com":
            print('enter a valid mail')
            register()
        else:
            db = open("database.txt","a")
            db.write(gmail+","+password+"\n")
            print("registered succesfully")

def access():
    db = open("database.txt", "r")
    gmail = input("enter your gmail:")
    password = input("enter your password")
    if not len( gmail or password )<1:
           d = []
           f = []
           for i in db:
            a,b = i.split(",")
            b = b.strip()
            d.append(a)
            f.append(b)
            data = dict(zip(d,f))
            try:
                if data[gmail]:
                   try:
                       if password ==data[gmail]:
                             print('Log in success')
                             print("welcome")
                             break
                       else:
                            print("incorrect password or gmail")
                            print("if u forget your password")
                            access()
                            break
                   except:
                        print("incorrectpassword or gmail")
                        access()
                        break
                else:
                    print("user name doesn't exists")
                    access()
                    break
            except:
                 print("password in correct")
                 access()
                 break
def forget():
    db = open("database.txt", "r")
    gmail = input("enter your gmail:")
    d = []
    f =  []
    for i in db:
                a,b = i.split(",")
                b = b.strip()
                d.append(a)
                f.append(b)
                data = dict(zip(d,f))
                print("this is your password",data.get(gmail))
                break
def  option():
        user = input("login || signup || forget password:")
        if user =="login":
            access()
        elif user == "signup":
            register()
        elif user =="forget":
            forget()
option()
