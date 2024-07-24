# Shopping Catalogue by Bright Onyekachi
print("Welcome to the shopping catalogue")
def into():
    print("""
Please select one of the following: 
1. Add item
2. Remove item
3. View cart
4. Compute total
5. Quit """)
          
into() 
list=input("What do you want to do")
if list =="1":   
    my_list = []          
    while True:
    
        my_list = input("Enter Item Name")
        if my_list == "":
            break
        my_list.append(my_list)
    print("Your inputs are:")
    for item in my_list:
        print(item)
       
  