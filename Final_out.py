import random
print("                        MINI_PROJECT \n\n                       TEXT_BASED TRADING\n\n\n"        )
a=[
            {"stock_name":"sajith","stock_price":random.randint(1,500)},
            {"stock_name":"ragul","stock_price":random.randint(1,500)},
            {"stock_name":"lokesh","stock_price":random.randint(1,500)}
            ]
for s in a:
    print(s)


class SimpleTrading:
    def __init__(self):
        
        self.balance = 10000 #Total balance
        self.portfolio = [] #List to store stocks..

    def display_menu(self):
        print("\n1.Buy Stock")
        print("2.Sell Stock")
        print("3.Display portfolio")
        print("4.Display Amount")
        print("5.Quit")


    def buy_stock(self):
        stock_name =input("Enter the Stock name:")
        quantity =int(input("Enter the Quantity to Buy:"))
        for b in a:
            if stock_name == b["stock_name"]:
                stock_price = b["stock_price"]
                total_cost = quantity * stock_price
            

                if total_cost > self.balance:
                    print("Insufficient funds.")
                else:
                    self.balance -= total_cost
                    self.portfolio.append({"name":stock_name,"quantity":quantity})

    def sell_stock(self):
        a=[
            {"stock_name":"sajith","stock_price":random.randint(1,500)},
            {"stock_name":"ragul","stock_price":random.randint(1,500)},
            {"stock_name":"lokesh","stock_price":random.randint(1,500)}
        ]
        for c in a:
            print(c)
        y=input("you  sell stock yes or no:")
        if y == "yes":
            stock_name = input("Enter the stock name:")
            quantity =int(input("Enter the quantity to sell:"))
            for stock in self.portfolio:
                if stock_name == stock["name"] and stock["quantity"] >=quantity:
                    for b in a:
                        if b["stock_name"]==stock_name:
                            stock_new=b["stock_price"]
                            total_earnings = quantity * stock_new
                            self.balance += total_earnings
                            stock["quantity"] -= quantity

                    if stock["quantity"] == 0:
                        self.portfolio.remove(stock)
                    break
            else:
                print("Invalid.operation.Check your Portfolio or Quantity.")
        else:
            print("ok")



    def display_portfolio(self):
        print("\n Portfolio:")
        for stock in self.portfolio:
            print(f"Name:{stock['name']},Quantity:{stock['quantity']}")


            
    def display_balance(self):
        print(f"\n Balance:${self.balance}")



        
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter Your choice (1-5):")

            if choice == "1":
                self.buy_stock()
            elif choice == "2":
                self.sell_stock()
            elif choice =="3":
                self.display_portfolio()
            elif choice =="4":
                self.display_balance()
            elif choice =="5":
                print("Exiting the program .Thank You")
                break
            else:
                print("Invalid choice.please enter a number between 1 and 5.")
mini_project = SimpleTrading()
mini_project.run()
                
            
                      
        
