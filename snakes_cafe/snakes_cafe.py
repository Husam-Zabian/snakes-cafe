
def welcome():
    print("**************************************")
    print("**    Welcome to the Snakes Cafe!   **")
    print("**    Please see our menu below.    **")
    print("**")
    print('** To quit at any time, type "quit" **')
    print("**************************************")
    print('')

menu ={
      "Appetizers" : ["Wings","Cookies","Spring Rolls"],
      "Entrees":["Salmon","Steak","Meat Tornado","A Literal Garden"],
      "Desserts":["Ice Cream","Cake","Pie"],
      "Drinks":["Coffee","Tea","Unicorn Tears"]
    }
theMenu = []

def Menu():
    
    for item in menu:
        print(item)
        print("------")
        for z in menu[item]:
         print(z)
         theMenu.append(z)
        print('')

def MyOrder(orders):
    print('')
    for item, quantity in orders.items():
        if(quantity==1):
            print(f"** {quantity} order of {item.capitalize()} have been added to your meal **")
        else:
            print(f"** {quantity} orders of {item.capitalize()} have been added to your meal **")
    print('')       

def Asking():
    orders={}
    print("**************************************")
    print("** What would you like to order? **")
    print("**************************************")
    while True:
     x = input("> ")
     if x == "quit":
       return False          
     elif x in orders:
            orders[x] += 1
     elif x in theMenu:
            orders[x] = 1
     else:
         print("Your order is not included to our menu")       
     MyOrder(orders)  

if __name__ == '__main__':
 welcome()
 Menu()
 Asking()
 print("Thanks for trying snakes_cafe !")
