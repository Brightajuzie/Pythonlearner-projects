#Milestone Assignment
# Program to calculate the price of meal

#Prompts User to input Price for Child's meal
ChildP=float(input("Enter Price for Child's meal:"))

#Prompts User to input Price for Adult's meal
adulp= float (input ("Enter Price for Adult's Meal:"))

#Prompts User to input number of chldren
Numberofc= int(input("Enter Number of Children:"))

#Prompts User to input number of Adults
NumberofA= int(input("Enter Number of Adults:"))

#Computes the Total for childs meal
MealTotalc = ChildP * Numberofc 

#Computes the Total for Adult meal
MealTotala = adulp * NumberofA

#Sums the two values
Subtotal = MealTotalc + MealTotala

#Displays the Subtotal
print("Subtotal: $", Subtotal)

#Adding Tax Rate
Taxr= float(input("Enter Tax Rate:"))

#Computing Sales Tax
Stax= Subtotal*Taxr/100

print("Sales Tax: $",Stax)

#Determining the Total meal price
Tprice = Subtotal + Stax

#Display Total meal price
print("Total meal price:$",Tprice)

#Payment Amount
pmnt=float(input("Enter Payment Amount:"))

#calculating change
chng= pmnt + Stax

#Dispaly the change
print("Change: $",chng)







