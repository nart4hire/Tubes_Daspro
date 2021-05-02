#to do: F09
#main program
import argparse, os
from function_register import register_user #F01
from function_login import login_user #F02
from function_carirarity import carirarity #F03
from function_caritahun import caritahun #F04
from function_tambahitem import tambahitem #F05
from function_hapusitem import hapusitem #F06
from function_ubahjumlah import ubahjumlah #F07
from function_pinjam import meminjam_gadget #F08
from function_kembalikan import mengembalikan_gadget #F09
from function_minta import meminta_consumable #F10
from function_riwayatpinjam import riwayatpinjam #F11
from function_riwayatkembali import riwayatkembali #F12
from function_riwayatambil import riwayatambil #F13
from function_load import load #F14
from function_save import save #F15
from function_help import bantuan #F16
from function_exit import keluar #F17
from function_gacha import gacha #FB03

user=[]
gadget=[]
consumable=[]
consumable_history=[]
gadget_borrow_history=[]
gadget_return_history=[]
role="user" #default role
ID=0 #user ID

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
    arr=login_user(user) #temporary arr
    ID=arr[0]
    role=arr[1]
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
            arr=tambahitem(gadget,consumable) #temporary arr
            gadget=arr[0]
            consumable=arr[1]
        elif command=="hapusitem" and role=="admin":
            arr=hapusitem(gadget,consumable) #temporary arr
            gadget=arr[0]
            consumable=arr[1]
        elif command=="ubahjumlah" and role=="admin":
            arr=ubahjumlah(gadget,consumable) #temporary arr
            gadget=arr[0]
            consumable=arr[1]
        elif command=="pinjam" and role=="user":
            arr=meminjam_gadget(gadget,gadget_borrow_history,ID)
            gadget=arr[0]
            gadget_borrow_history=arr[1]
        elif command=="kembalikan" and role=="user":
            arr=mengembalikan_gadget(gadget,gadget_borrow_history,gadget_return_history,ID)
            gadget=arr[0]
            gadget_borrow_history=arr[1]
            gadget_return_history=arr[2]
        elif command=="minta" and role=="user":
            arr=meminta_consumable(consumable,consumable_history,ID)
            consumable=arr[0]
            consumable_history=arr[1]
        elif command=="riwayatpinjam" and role=="admin":
            riwayatpinjam(user,gadget,gadget_borrow_history)
        elif command=="riwayatkembali" and role=="admin":
            riwayatkembali(user,gadget,gadget_borrow_history,gadget_return_history)
        elif command=="riwayatambil" and role=="admin":
            riwayatambil(user,consumable,consumable_history)
        elif command=="save":
            save(user,gadget,consumable,consumable_history,gadget_borrow_history,gadget_return_history)
        elif command=="help":
            bantuan(role) #help reserved word
        elif command=="exit":
            keluar(user,gadget,consumable,consumable_history,gadget_borrow_history,gadget_return_history) #exit reserved word
        elif command=="gacha" and role=="user":
            arr=gacha(ID,consumable_history,consumable)
            consumable_history=arr[0]
            consumable=arr[1]
        else:
            print("Command tidak valid, ketik \"help\" untuk menampilkan command list")
        print()
            