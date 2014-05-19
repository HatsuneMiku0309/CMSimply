import hashlib
import random
import string
import smtplib
from email.mime.text import MIMEText  
from email.header import Header
 
''' sha1 secure hashes '''
 
def gen_password(user_password,salt):
    return hashlib.sha1(user_password.encode("utf-8")).hexdigest()

seed = "1234567890abcdefghijklmnopqrstuvwxyz"
sa = []
 
# use gen_password() to write users.auth.php
with open("10yoyo1.txt","wt") as out_file:
    with open("10yoyo.txt", "r", encoding='utf-8') as in_file:
        for index in in_file:
            for i in range(8):
                sa.append(random.choice(seed))
            salt = ''.join(sa)
            print(salt)
            std_num,std_name = index.strip().split(' ')
            std_mail = std_num + '@gm.nfu.edu.tw'
            print(std_num, std_name)
            out_file.write(str(std_num)+':'+gen_password(salt)+':'+str(std_mail)+':'+str(std_mail)+':'+'cd,user'+"\n")
        