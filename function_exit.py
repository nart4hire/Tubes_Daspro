from function_save import save
def keluar(user,gadget,consumable,consumable_history,gadget_borrow_history,gadget_return_history): #exit() command. Menggunakan fungsi save().
    print("Apakah Anda mau melakukan penyimpanan pada file yang sudah diubah? (y/n): ",end="")
    choice=str(input())
    if choice=="y" or choice=="Y":
        save(user,gadget,consumable,consumable_history,gadget_borrow_history,gadget_return_history)
    elif choice!="n" or choice!="N":
        print("Masukan tidak valid")
        keluar(user,gadget,consumable,consumable_history,gadget_borrow_history,gadget_return_history)
