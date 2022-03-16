from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_continue=True
while(is_continue):
  menu=Menu()
  moneyMachine=MoneyMachine()
  cofffeeMaker=CoffeeMaker()
  choice=input(f"What Would you like {menu.get_items()}")
  if(choice == 'off'):
    is_continue = False
  elif(choice == "report"):
    cofffeeMaker.report()
    moneyMachine.report()
  elif(choice == 'latte','espresso','cappuccino'):
    drink=menu.find_drink(choice)
    if(cofffeeMaker.is_resource_sufficient(drink)):
      if(moneyMachine.make_payment(drink.cost)):
        cofffeeMaker.make_coffee(drink)
        
    
  
