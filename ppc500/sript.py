import os
import random


flag = "1l0ve4rc1ve5"


try:
    file = open("flag.txt", "x")
    file.write(flag)
    file.close()
except:
    print("File exist")
    
    
password = random.randint(10**5, 10**6)
print(os.popen("zip --password %d archive.zip flag.txt" % password).read())
try:
    file = open("pass.txt", "x")
    file.write(str(password))
    file.close()
except:
    print("File exist")

password = random.randint(10**5, 10**6)
print(os.popen("zip --password %d myarchive.zip archive.zip pass.txt" % password).read())
os.remove("pass.txt")
try:
    file = open("pass.txt", "x")
    file.write(str(password))
    file.close()
except:
    print("File exist")

for i in range(250):
    os.remove("archive.zip")
    os.remove("pass.txt")
    os.rename("myarchive.zip", "archive.zip")
    password = random.randint(10**5, 10**6)
    try:
        file = open("pass.txt", "x")
        file.write(str(password))
        file.close()
    except:
        print("File exist")
    print(os.popen("zip --password %d myarchive.zip archive.zip pass.txt" % password).read())
    
os.remove("archive.zip")
os.remove("flag.txt")
os.rename("myarchive.zip", "archive.zip")
