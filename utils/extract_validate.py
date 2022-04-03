import json
import os
from zipfile import ZipFile

def lis_import_file(contract):
    li=contract["import-files"]
    return li

def match_two_lis(li1,li2):
    for i in li1:
        if i not in li2:
            return False
    return True

def validation(last_index,dir):
    with ZipFile('files/model_'+str(last_index)+'.zip', 'r') as zipObj:
    # Extract all the contents of zip file in current directory
        zipObj.extractall(dir)
    f = open(dir+"/contract.json")
    contract = json.load(f)
    path = dir
    dir_list = os.listdir(path)
    contract_lis=lis_import_file(contract)

    filecheck=match_two_lis(contract_lis,dir_list)
    
    return filecheck
