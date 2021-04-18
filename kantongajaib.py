#main program
import argparse, os
from function_register import register_user #F01
from function_login import login_user #F02
from function_carirarity import carirarity #F03
from function_caritahun import caritahun #F04
from function_tambahitem import tambahitem #F05
from function_hapusitem import hapusitem #F06
from function_ubahjumlah import ubahjumlah #F07
from function_load import load #F14
from function_save import save #F15
from function_help import bantuan #F16
from function_exit import keluar #F17

user=[]
gadget=[]
consumable=[]
consumable_history=[]
gadget_borrow_history=[]
gadget_return_history=[]
role="user" #default role

def dir_path(filename): #argparse awal, dengan mengecek apakah file lengkap
    listcsv=['consumable.csv','consumable_history.csv','gadget.csv','gadget_borrow_history.csv','gadget_return_history.csv','user.csv']
    #finding the folder
    fullfilename=filename
    for (root, folder, file) in os.walk("C:", topdown=True):
        if filename in folder:
            if root!="C:":
                root+="\\"
            fullfilename = root+filename
            fullfilename=fullfilename[2:]
    for (root, folder, file) in os.walk(fullfilename, topdown=True):
        if root==fullfilename and (all (x in file for x in listcsv)):
            return fullfilename
    raise NotADirectoryError(filename)
    
    
if __name__== '__main__':
    #auto load sequence
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=dir_path)
    args=parser.parse_args()
    arr=load(args.path)
    user=arr[0]
    gadget=arr[1]
    consumable=arr[2]
    consumable_history=arr[3]
    gadget_borrow_history=arr[4]
    gadget_return_history=arr[5]
    
    #login wajib
    role=login_user(user)
    command=""
    while(command!="exit"):
        command=str(input())
        if command=="register" and role=="admin":
            register_user(user)
        elif command=="carirarity":
            carirarity(gadget)
        elif command=="caritahun":
            caritahun(gadget)
        elif command=="tambahitem" and role=="admin":
            arr=tambahitem(gadget,consumable)
            gadget=arr[0]
            consumable=arr[1]
        elif command=="hapusitem" and role=="admin":
            arr=hapusitem(gadget,consumable)
            gadget=arr[0]
            consumable=arr[1]
        elif command=="ubahjumlah" and role=="admin":
            arr=ubahjumlah(gadget,consumable)
            gadget=arr[0]
            consumable=arr[1]
        elif command=="save":
            save(user,gadget,consumable,consumable_history,gadget_borrow_history,gadget_return_history)
        elif command=="help":
            bantuan(role) #help reserved word
        elif command=="exit":
            keluar(user,gadget,consumable,consumable_history,gadget_borrow_history,gadget_return_history) #exit reserved word
        else:
            print("Command tidak valid, ketik \"help\" untuk menampilkan command list")
        print()
            