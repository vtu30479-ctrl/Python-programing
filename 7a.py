def disc(qty):
    if qty<=10:
        return 0
    elif 11<=qty<=20:
        return 15
    else:
        return 20
def buy():
    icode=int(input("Enter item code:"))
    item=input("Enter itwem name:")
    price=float(input('Enter price:'))
    Qty=int(input('ENter quantity:'))
    Disc=disc(Qty)
    Netprice=price*Qty-Disc
    return icode,item,price,Qty,Disc,Netprice
def all(icode,item,price,Qty,Disc,Netprice):
    print(f"Item code:{icode}\nItem:{item}\nPrice{price}:\nQuantity:{Qty}\nDiscount:{Disc}\nNetprice:{Netprice}\n")
icode,item,price,Qty,Disc,Netprice=buy()
all(icode,item,price,Qty,Disc,Netprice)
