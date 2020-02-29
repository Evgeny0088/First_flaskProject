import json
import os
import hashlib

blockchain = os.curdir + "/blockchain/"
file_prefix = "Block "

def get_files():
    files=os.listdir(blockchain)
    digit_list = sorted([int(i[i.find(' ')+1:]) for i in files])
    return digit_list

def create_genesice():
    data = {
        "name":"Evgeny",
        "amount":5,
        "to_whom":"Next user",
        "hash":""
    }
    with open(blockchain+file_prefix+"1","w") as file:
        json.dump(data,file,indent=4,ensure_ascii=False)

def create_hash(filename):
    file=open(filename,"rb").read()
    hash=hashlib.md5(file).hexdigest()
    return hash

def write_block(name,amount,to_whom):
    files=get_files()
    if not files:
        return
    else:
        last_file=file_prefix + str(files[-1]+1)
        prev_file=file_prefix + str(files[-1])
    data = {
        "name":name,
        "amount":amount,
        "to_whom":to_whom,
        "hash":create_hash(blockchain+prev_file)
    }
    with open(blockchain+last_file,'w') as file:
        json.dump(data,file,indent=4,ensure_ascii=False)

def read_block(block):
    with open(blockchain+block,'r') as file:
        f_content=json.load(file)
    return f_content

def find_block(block):
    digits=get_files()
    file_list = [file_prefix+str(i) for i in digits]
    for i in file_list:
        if i==block:
            flag = True
            break
        else:
            flag = False
    return flag

def check_integrity():
    files=get_files()
    results=[]
    for file in files[1:]:
        prev_file=file_prefix+str(file-1)
        h=json.load(open(blockchain+file_prefix+str(file)))['hash']
        prev_hash=create_hash(blockchain+prev_file)
        if prev_hash==h:
            res="Ok"
        else:
            res="Corrupted"
        results.append({prev_file:res})
    return results

def main():
    write_block('Sam',100,"Phill")
    for i in check_integrity():
        print(i)

if __name__=="__main__":
    main()