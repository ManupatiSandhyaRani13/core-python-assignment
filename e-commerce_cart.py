def cal_tot_price(cart_items):
    Total_price=0
    length=len(cart_items)
    if length==0:
        print("Cart is empty")
    for i in cart_items:
        Total_price+=cart_items[i] #total=sum(dict.values())
    if length>5:
        discount=10
        discount_price=Total_price*(discount/100)
        final_price=Total_price-discount_price
        print(f"Total Price : {final_price}")
    else:
        print(f"Total Price : {Total_price}")

cart_items={}
while True:
    key=input("Enter the key ( or type exit to stop) : ")
    if key.lower()=='exit':
        break
    value=int(input(f"Enter the price for the key {key} : "))
    cart_items[key]=value
print(f"cart_items = {cart_items}")
cal_tot_price(cart_items)
