import time
mod=137 #ubah untuk mengatur peluang gacha

def generate_inventory(ID, consumable_history):
    for i in range(1,len(consumable_history)):
        if (ID==consumable_history[i][1]): #posisi id di csv
            id_barang=consumable_history[i][2]
            jumlah=consumable_history[i][4]
            if (id_barang in inventory):
                inventory[id_barang]+=jumlah
            else:
                inventory[id_barang]=jumlah

def generate_daftar_nama(inventory, consumable):
    for i in inventory:
        for j in range(1,len(consumable)):
            if i==consumable[j][0]: #nama id sama
                daftar_nama[i]= [consumable[j][1],consumable[j][4]]
                break
def random():
    mult=23
    add=91
    x=round(time.time())%mod #mod global var
    return (x*mult+add)%mod

def interface():
    print("==========Inventory==========")
    counter=0
    for i in inventory:
        print(counter+1,end="")
        print(".", daftar_nama[i][0], "|Rarity", daftar_nama[i][1],"|", inventory[i],"buah")
        counter+=1
    print("=============================")
    print()
    
def maxrarity(a,b):
    rarity=["C","B","A","S"]
    if rarity.index(a)>rarity.index(b):
        return a
    else:
        return b

def generate_id_transaksi (datas):
    tmp = datas[-1][0]
    tmp2 = []
    tmp_id = ""
    for i in tmp:
        tmp2.append(i)
    for i in range (1,(len(tmp2))):
        tmp_id += tmp2[i]
    tmp_id = int(tmp_id) + 1
    id_transaksi = tmp2[0]+str(tmp_id)
    return id_transaksi

    
def gacha(ID, consumable_history, consumable):
    global inventory
    global used
    global daftar_nama
    global idlist
    inventory={} #daftar dictionary {ID: jumlah} dari inventory tiap user
    used={} #daftar consumable yang digunakan {ID: jumlah}
    daftar_nama={} #daftar dictionary {ID: [nama_barang,rarity]} dari tiap consumable yang dimiliki user
    idlist=[] #daftar urutan ID untuk keperluan I/O
    
    generate_inventory(ID, consumable_history)
    generate_daftar_nama(inventory, consumable)
    if not inventory: #gacha tidak bisa jika inventory kosong
        print("Inventory anda kosong")
        return [consumable_history,consumable] #exit
    #gacha rules
    print("Aturan gacha:")
    print("1. Anda boleh menggunakan sampai dengan 100 item.")
    print("2. Kualitas item yang didrop adalah kualitas tertinggi item yang digunakan atau satu kualitas diatasnya.")
    print("3. Peluang upgrade rarity akan dinyatakan sebelum gacha.")
    print("4. Jika anda menggunakan item rarity S, drop akan 100% mengeluarkan rarity S")
    print()
    #list
    for i in inventory:
        idlist.append(i)
    #input
    repeat="y"
    total=0
    rarity="C"
    while (repeat=="y" or repeat=="Y") and total<100:
        interface()
        choice=int(input("Pilih consumable yang ingin digunakan: "))
        while (choice>len(idlist)):
            print("Masukan tidak valid")
            choice=int(input("Pilih consumable yang ingin digunakan: "))
        choice-=1 #keperluan array
        amount=int(input("Jumlah yang digunakan: "))
        while (amount<=0 or amount>inventory[idlist[choice]]):
            print("Masukan tidak valid")
            amount=int(input("Jumlah yang digunakan: "))
        if (total+amount>=100):
            amount=100-total #jika lebih, pakai sampai maks saja
        inventory[idlist[choice]]-=amount #update inventory
        if idlist[choice] in used:
            used[idlist[choice]]+=amount
        else:
            used[idlist[choice]]=amount #update used
        total+=amount #update total
        rarity=maxrarity(rarity,daftar_nama[idlist[choice]][1]) #update max rarity
        #interface
        print()
        if rarity!="S": print("Peluang anda mengupgrade benda rarity", rarity, "adalah", round(total*100/mod,2),"%")
        else: print("Peluang anda mendapatkan benda rarity", rarity, "adalah", 100,"%")
        if total==100: break
        repeat=input("Tambahkan item lagi?(y/n): ")
        while not(repeat in ['y','Y','n','N']):
            print("Masukan tidak valid")
            repeat=input("Tambahkan item lagi?(y/n): ")
            
    #are you sure?
    print()
    ans=input("Apakah anda yakin ingin melakukan gacha?(y/n): ")
    while not(ans in ['y','Y','n','N']):
        print("Masukan tidak valid")
        ans=input("Apakah anda yakin ingin melakukan gacha?(y/n): ")
    if ans=='n' or ans=='N':
        return [consumable_history,consumable] #exit
    
    #rolling interface
    print("Rolling",end="")
    for i in range(3):
        time.sleep(1)
        print(".",end="")
    print()
    
    #quality roll
    if rarity!="S":
        rank=["C","B","A","S"] #array temporary urutan rarity
        if random()<total:
            rarity=rank[rank.index(rarity)+1] #upgrade rarity
        #else rarity tetap
    
    #available item generation
    drops=[] #[[ID,name]]
    for i in range(1,len(consumable)):
        if (consumable[i][3]>0 and consumable[i][4]==rarity): #rarity target ada
            drops.append([consumable[i][0],consumable[i][1]])
    
    #if empty
    if len(drops)==0:
        print("Error: anda mendapatkan item rarity",rarity,"tetapi stok item habis. Silahkan kontak admin.")
        return [consumable_history,consumable] #exit
    
    #item roll
    item_index=random()%len(drops)
    #interface
    print("Selamat, anda mendapatkan", drops[item_index][1], "rarity", rarity )
    
    #transaction
    #consumable_history
    for i in used:
        id_transaksi=generate_id_transaksi(consumable_history)
        consumable_history.append([id_transaksi,ID,i,"01/01/n0001",-1*used[i]]) #tanggal uniform
    id_transaksi=generate_id_transaksi(consumable_history)
    consumable_history.append([id_transaksi,ID,drops[item_index][0],"01/01/0001",1])
    
    #consumable
    for i in used:
        for j in range(1,len(consumable)):
            if i==consumable[j][0]: #ID sama
                consumable[j][3]+=used[i] #tambahkan
                break
    for j in range(1,len(consumable)):
        if drops[item_index][0]==consumable[j][0]: #ID sama
            consumable[j][3]-=1 #ambil 1
            break
    
    #end
    return [consumable_history,consumable]