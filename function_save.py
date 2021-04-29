#save(datas)->null 
#melakukan save pada folder yang akan diinput user. Overwrite/new folder function sudah termasuk
import os

def writecsv(data,folder,file): #membuat csv baru/overwrite pada path yang diberikan
    f=open(folder+"\\"+file,"w+")
    for i in range(len(data)):
        for j in range(len(data[i])):
            f.write(str(data[i][j]))
            if j!=len(data[i])-1:
                f.write(";")
        f.write("\n")
    f.close()
    
def save(user,gadget,consumable,consumable_history,gadget_borrow_history,gadget_return_history): 

    filename=str(input("Masukkan nama folder penyimpanan:"))
    print("Saving...")
    fullfilename=filename
    #finding the folder
    for (root, folder, file) in os.walk("C:", topdown=True):
        if filename in folder:
            if root!="C:":
                root+="\\"
            fullfilename = root+filename
            fullfilename=fullfilename[2:]
    #if path doesn't exist, make one
    if not os.path.exists(fullfilename):
        os.makedirs(fullfilename)
    
    #writing time
    writecsv(user,fullfilename,"user.csv")
    writecsv(gadget,fullfilename,"gadget.csv")
    writecsv(consumable,fullfilename,"consumable.csv")
    writecsv(consumable_history, fullfilename, "consumable_history.csv")
    writecsv(gadget_borrow_history, fullfilename, "testcsv/gadget_borrow_history.csv")
    writecsv(gadget_return_history,fullfilename,"gadget_return_history.csv")
    print("Data telah disimpan pada folder "+filename+"!")