print("\n" * 1)                  

import datetime                    
import os                          

list_foods = []                  
list_cus = []
list_item_price = [0] * 100        
                                  
navigator_symbol = "/" 
if os.name == "nt":
    navigator_symbol = "\\" 

def def_default():
    global list_foods, list_item_order, list_item_price    
    list_item_order = [0] * 100                     
def_default() 

def main():
   while True:
        print("*" * 28 + "ORDERING SYSTEM" + "*" * 24 + "\n") 
        print("#" * 31 + "MAIN MENU" + "#" * 32 + "\n"     
              "\t(1) CUSTOMER\n"                              
              "\t(2) ADMIN\n"
              "\t(3) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Parth: ")).upper()    
        if (len(input_1) == 1):                                           
            if (input_1 == '1'):                                          
                print("\n" * 1)                                        
                c_user()                                          
                break                                                     
            elif (input_1 == '2'):                                        
                print("\n" * 1)                                        
                a_user()                                             
                break                                                                                                         
            elif (input_1 == '3'):                                        
                print("*" * 32 + "THANK YOU COME AGAIN" + "*" * 31 + "\n")           
                break                                                     
            else:                                                                                 
                print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + ").Something Went Wrong ,Try again!")     
        else:                                                                                     
            print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!")

def c_user():                                                                               
    while True:                                             
        print("*" * 31 + "LOGIN AND SING UP PAGE" + "*" * 31 + "\n"    
              "\t(1) SING UP\n"
              "\t(2) LOGIN\n"
              "\t(3) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Parth: ")).upper() 
        if len(input_1) == 1:
            if (input_1 == '1'):  
                print("\n" * 1)
                c_register()
                break
            elif (input_1 == '2'):
                print("\n" * 1)
                c_login() 
                break
            elif (input_1 == '3'):
                print("*" * 32 + "THANK YOU COME AGAIN" + "*" * 31 + "\n")
                break
            else:
                print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!") 
        else:
            print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!")

def c_register():
    n = input(" "*20+"Your Name: ")
    p = input(" "*20+"Your Password: ")
    success = True
    file = open('files'+navigator_symbol+'customer', 'a')
    file.write(n+" - "+p+"\n")
    print(" ")
    if(success):
        print(" ")
        print("-" * 20 + " Hey " + n + "-" * 20)
        print(" ")
        order()
    else:
        print("Something Went Wrong ,Try again!")

def c_login():
    u = input(" "*20+"Username: ")
    p = input(" "*20+"Password: ")
    success = False
    file = open('files'+navigator_symbol+'customer', 'r')
    for i in file:
        a,b = i.split(" - ")
        b = b.strip()
        if(a==u and b==p):
            success = True
            break
    file.close()
    if(success):
        print(" ")
        print("-" * 20 + "Login Successful" + "-" * 20)
        print()
        order()
    else:
        print("Incorrect username or password")

def a_user():                                                                               
    while True:                                             
        print("*" * 25 + "LOGIN AND SING UP PAGE" + "*" * 25 + "\n"    
              "\t(1) SING UP\n"
              "\t(2) LOGIN\n"
              "\t(3) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Parth: ")).upper() 
        if len(input_1) == 1:
            if (input_1 == '1'):  
                print("\n" * 1)
                a_register()
                break
            elif (input_1 == '2'):
                print("\n" * 1)
                a_login() 
                break
            elif (input_1 == '3'):
                print("*" * 25 + "THANK YOU COME AGAIN" + "*" * 25 + "\n")
                break
            else:
                print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!") 
        else:
            print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!")

def a_register():
    n = input(" "*20+"Name: ")
    p = input(" "*20+"Password: ")
    success = True
    print(" ")
    file = open('files'+navigator_symbol+'admin', 'w')
    file.write(n+" - "+p+"\n")
    print(" ")
    if(success):
        print("-" * 20 + " Hey " + n + "-" * 20)
        print(" ")
        Item_edit()
    else:
        print("Something Went Wrong ,Try again!")

def a_login():
    u = input(" "*20+"Username: ")
    p = input(" "*20+"Password: ")
    success = False
    file = open('files'+navigator_symbol+'admin', 'r')
    for i in file:
        a,b = i.split(" - ")
        b = b.strip()
        if(a==u and b==p):
            success = True
            break
    file.close()
    if(success):
        print()
        print("-" * 20 + "Login Successful" + "-" * 20)
        print()
        Item_edit()
    else:
        print("Incorrect username or password")

# --------------------------------------Customer Works--------------------------------------
def order():
   while True:
        print("*" * 31 + "ORDER MENU" + "*" * 32 + "\n"     
              "\t(O) ORDER\n"                              
              "\t(L) Item List\n"
              "\t(E) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Operation: ")).upper()    
        if (len(input_1) == 1):                                           
            if (input_1 == 'O'):                                          
                print("\n" * 1)                                        
                order_menu()                                          
                break                                                     
            elif (input_1 == 'L'):                                        
                print("\n" * 1)                                        
                viewAll_foods()                                             
                break                                                    
            elif (input_1 == 'E'):                                        
                print("*" * 32 + "THANK YOU COME AGAIN" + "*" * 31 + "\n")           
                break                                                     
            else:                                                                                 
                print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + ").Something Went Wrong ,Try again!")     
        else:                                                                                     
            print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!") 

def order_menu():                                                                               
    while True:                                             
        print("*" * 31 + "ORDER PAGE" + "*" * 31 + "\n"    
              "\t(F) ORDER FOODS\n"
              "\t(M) MAIN MENU\n"
              "\t(E) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Parth: ")).upper() 
        if len(input_1) == 1:
            if (input_1 == 'F'):  
                print("\n" * 1)
                food_order()
                break
            elif (input_1 == 'M'):
                print("\n" * 1)
                viewAll_foods() 
                break
            elif (input_1 == 'E'):
                print("*" * 32 + "THANK YOU COME AGAIN" + "*" * 31 + "\n")
                break
            else:
                print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!") 
        else:
            print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!")

def food_file_reader():                                                                        
    file_foods = open('files'+navigator_symbol+'list_food', 'r') 
    for i in file_foods: 
        list_foods.append(str(i.strip())) 
    file_foods.close()



    i = 0
    while i <= (len(list_foods) - 1): 
        if 'Rs' in list_foods[i]:
            list_foods[i] = str(list_foods[i][:list_foods[i].index('Rs') - 1]) + ' ' * (20 - (list_foods[i].index('Rs') - 1)) + str(list_foods[i][list_foods[i].index('Rs'):])
        i += 1
food_file_reader()

def food_file_sorter(): 
    global list_foods
    list_foods = sorted(list_foods)
    

    i = 0
    while i < len(list_foods):
        list_item_price[i] = float(list_foods[i][int(list_foods[i].index("Rs") + 2):]) 
        i += 1
food_file_sorter()

def viewAll_foods():
    while True:
            print("*" * 30 + "ORDER FOODS" + "*" * 30)
            print()
            print(" "*20+"-" * 40)
            print(" "*20+" |NO| |FOOD NAME|         |PRICE|")
            print(" "*20+"-" * 40)

            i = 0
            while i < len(list_foods):
                var_space = 1
                if i <= 8:                      
                    var_space = 2

                if i < len(list_foods):
                    food =" "*20+ " (" + str(i + 1) + ")" + " " * var_space + str(list_foods[i]) 
                else:
                    food = " "*20+" " * 36
                
                print(food)
                i += 1

            print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)

            print()
            input_1 = input(" "*20+"Please Select Your Want or Parth: ").upper() 
            if (input_1 == 'M'):
                print("\n" * 1)
                exit 
                break
            if (input_1 == 'E'):
                print("*" * 25 + "THANK YOU COME AGAIN" + "*" * 25 + "\n") 
                break
            if (input_1 == 'P'):
                print("\n" * 1)
                exit 
                break
            try:        
                int(input_1)
                if ((int(input_1) <= len(list_foods) and int(input_1) > 0)):
                     try:
                        print("\n" + "_" * 72 + "\n" + str(list_foods[int(input_1) - 1])) 
                     except:
                        pass
            except:
                print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!")

def food_order():
    while True:
            print("*" * 30 + "ORDER FOODS" + "*" * 30)
            print()
            print(" "*20+"-" * 40)
            print(" "*20+" |NO| |FOOD NAME|         |PRICE|")
            print(" "*20+"-" * 40)

            i = 0
            while i < len(list_foods):
                var_space = 1
                if i <= 8:                      
                    var_space = 2

                if i < len(list_foods):
                    food =" "*20+ " (" + str(i + 1) + ")" + " " * var_space + str(list_foods[i]) 
                else:
                    food = " "*20+" " * 36
                
                print(food)
                i += 1

            print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)

            print()
            input_1 = input(" "*20+"Please Select Your Want or Parth: ").upper()  
            if (input_1 == 'M'):
                print("\n" * 1)
                main() 
                break
            if (input_1 == 'E'):
                print("*" * 32 + "THANK YOU COME AGAIN" + "*" * 31 + "\n") 
                break
            if (input_1 == 'P'):
                print("\n" * 1)
                payment() 
                break
            try:        
                int(input_1)
                if ((int(input_1) <= len(list_foods) and int(input_1) > 0)):
                     try:
                        print("\n" + "_" * 72 + "\n" + str(list_foods[int(input_1) - 1]))
                        print() 
                     except:
                        pass

                     input_2 = input("Enter the quantity you want?: ").upper() 

                     if int(input_2) > 0:
                        list_item_order[int(input_1) - 1] += int(input_2)
                        print()
                        print("Successfully next order!")
                        print()
                        food_order() 
                        break
                     else:
                        print("\n" * 1 + "ERROR: Invalid Input (" + str(input_2) + "). Something Went Wrong ,Try again!")
            except:
                print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!")

def payment():
    while True:
        print("*" * 32 + "PAYMENT" + "*" * 33 + "\n") 
        total_price = 0 
            

        report_new = "\n\n\n" + " " * 17 + "*" * 35 + "\n" + " " * 17 + "DATE: " + str(datetime.datetime.now())[:19] + "\n" + " " * 17 + "-" * 35 
        i = 0
        while i < len(list_item_order): 
            if(list_item_order[i] != 0):
                if (i >= 0) and (i < 40):
                    report_new += "\n" + " " * 17 + str(list_foods[i]) + "  x  " + str(list_item_order[i]) 
                    print(" " * 17 + str(list_foods[i]) + "  x  " + str(list_item_order[i])) 
                    total_price += list_item_price[i] * list_item_order[i] 
                i += 1
            else:
                i += 1
        
        report_new += "\n" + " " * 17 + "-" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35
        print(" " * 17 + "_" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)))
        print("\n (P) PAY           (M) MAIN MENU               (E) EXIT\n" + "_" * 72)
        input_1 = str(input("Please Select Your Operation: ")).upper()
        if (input_1 == 'P'):
            print("\n" * 1)
            print("Paid Successfully !")
            payment()
            break
        elif (input_1 == 'M'):
            print("\n" * 1)
            main() 
            break
        
        elif ('E' in input_1) or ('e' in input_1):
            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
            break
        else:
            print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!")

# --------------------------------------Admin Works--------------------------------------
def Item_edit():
    while True:
        print("*" * 28 + "ITEM EDIT MENU" + "*" * 28 + "\n"     
              "\t(1) Item Add\n"
              "\t(2) View All Items\n"
              "\t(3) View All Customers\n"
              "\t(4) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Operation: ")).upper()    
        if (len(input_1) == 1):                                           
            if (input_1 == '1'):                                          
                print("\n" * 1)                                        
                ItemAdd()                                          
                break
            elif (input_1 == '2'):                                        
                print("\n" * 1)                                        
                viewAll_foods()                                              
                break
            elif (input_1 == '3'):                                        
                print("\n" * 1)                                        
                cus_view()                                              
                break                                                      
            elif (input_1 == '4'):                                        
                print("*" * 32 + "THANK YOU COME AGAIN" + "*" * 31 + "\n")           
                break                                                     
            else:                                                                                 
                print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + ").Something Went Wrong ,Try again!")     
        else:                                                                                     
            print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!")

def ItemAdd():
    f = input("Food Name : ")
    s = input("selling Price : ")
    print(" ")
    success = True
    file_foods = open('files'+navigator_symbol+'list_food', 'a') 
    file_foods.write(f+" "+"Rs "+s+".00"+"\n")
    print(" ")
    file_foods.close()
    if(success):
        print("----------------Item add Successful----------------")
        Item_edit()
    else:
        print("Wrong input")

def Cus_file_reader():                                                                        
    file_cus = open('files'+navigator_symbol+'customer', 'r') 
    for i in file_cus: 
        list_cus.append(str(i.strip())) 
    file_cus.close()



    i = 0
    while i <= (len(list_cus) - 1): 
        if '- ' in list_cus[i]:
            list_cus[i] = str(list_cus[i])
        i += 1
Cus_file_reader()

def cus_view():
    while True:
            print("*" * 30 + "SING UP CUSTOMERS" + "*" * 30)
            print()
            print(" "*20+"-" * 30)
            print(" "*20+" |NO| |NAME| - |PASSWORD|")
            print(" "*20+"-" * 30)

            i = 0
            while i < len(list_cus):
                var_space = 1
                if i <= 8:                      
                    var_space = 2

                if i < len(list_cus):
                    food =" "*20+ " (" + str(i + 1) + ")" + " " * var_space + str(list_cus[i]) 
                else:
                    food = " "*20+" " * 36
                
                print(food)
                i += 1

            print("\n (M) MAIN MENU                   (E) EXIT\n" + "_" * 72)

            print()
            input_1 = input(" "*20+"Please Select Your Want or Parth: ").upper() 
            if (input_1 == 'M'):
                print("\n" * 1)
                Item_edit()
                break
            if (input_1 == 'E'):
                print("\n" * 1)
                print("*" * 25 + "THANK YOU COME AGAIN" + "*" * 25 + "\n") 
                exit 
                break
            try:        
                int(input_1)
                if ((int(input_1) <= len(list_cus) and int(input_1) > 0)):
                     try:
                        print("\n" + "_" * 72 + "\n" + str(list_cus[int(input_1) - 1])) 
                     except:
                        pass
            except:
                print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!")


main()