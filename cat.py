# Shopping Catalogue by Bright Onyekachi
print("Welcome to the shopping catalogue")
def into():
    print("""
This Program was written by: Mazi Bright Chidozie Onyekachi         
Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit """)
    
          
into() 
# Create a list to store the user inputs
shopping = []

# Use a loop to prompt the user for input and add the input to the list
while True:
    user=input("Input the Number of what you want to do")
    if user == "1":
        item = input("Enter your input: ")
        price= float(input("Enter Price in $"))
        shopping.append({"item":item, "price": price })
        print(item + " Has been Added")
           
    elif user == "2":
        print("Your inputs are:")
        for item in shopping:
             
             print(f"{item['item']} - ${item['price']:.2f}")
             
    elif user == "3":
        while True:
            item_to_delete = input("Enter the name of the item you want to delete: ")

      # Search the item in the list and delete it
            for item in shopping:
                if item["item"] == item_to_delete:  
                 shopping.remove(item)
                 break

        # Prompts the User to delete an Item
            delete_more = input("Do you want to delete more items from the list? (Y/N): ")
            if delete_more != "Y":
                 break
        # Calculates the total price of the items in the list
    elif user == "4":
        total_price = 0.0
        for item in shopping:
            total_price += item["price"]

        # Display the total price of items purchased by user.
        print(f"The total price of your shopping cart is: ${total_price}")
    elif user == "5":
        quit("GOOD BYE")   
      
            

