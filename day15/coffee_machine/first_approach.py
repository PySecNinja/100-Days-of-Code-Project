from data import MENU, resources

espresso_requirements = MENU['espresso']
latte_requirements = MENU['latte']
cappuccino_requirements = MENU['cappuccino']
money = 0
done_ordering = False
# print(espresso_requirements)

def start_machine():
    return input("What would you like? (espresso/latte/cappuccino): ").lower()
    

def money_inserted():
    print("Please Insert coins")
    quarters_inserted = float(input("How many quarters?: "))
    dimes_inserted = float(input("How many Dimes?: "))
    nickles_inserted = float(input("How many Nickles?: "))
    pennies_inserted = float(input("How many Pennies?: "))
    total_inserted = float((quarters_inserted * .25) + (dimes_inserted * .10) + (nickles_inserted * .05) + (pennies_inserted * .01))
    return total_inserted


def espresso():
    if total_inserted > espresso_requirements['cost']:
        if resources['water'] > espresso_requirements['ingredients']['water']:
            if resources['coffee'] > espresso_requirements['ingredients']['coffee']:
                print("Here is your coffee")
            else:
                print("Sorry theres not enough coffee.")
        else:
            print("Sorry there's not enough water.")
    else:
        print("Sorry that's not enough money. Money refunded.")            


def latte():
    if total_inserted > latte_requirements['cost']:
        if resources['water'] > latte_requirements['ingredients']['water']:
            resources['water'] = resources['water'] - latte_requirements['ingredients']['water']
            print(resources['water'])
            if resources['coffee'] > latte_requirements['ingredients']['coffee']:
                if resources['milk'] > latte_requirements['ingredients']['milk']:
                    print("Here is your coffee")
                else:
                    print("Sorry theres not enough milk")
            else:
                print("Sorry theres not enough coffee.")
        else:
            print("Sorry there's not enough water.")
    else:
        print("Sorry that's not enough money. Money refunded.")  


def cappuccino():
    if total_inserted > cappuccino_requirements['cost']:
        if resources['water'] > cappuccino_requirements['ingredients']['water']:
            if resources['coffee'] > cappuccino_requirements['ingredients']['coffee']:
                if resources['milk'] > cappuccino_requirements['ingredients']['milk']:
                    print("Here is your coffee")
            else:
                print("Sorry theres not enough coffee.")
                end_program()
        else:
            print("Sorry there's not enough water.")
            end_program()
    else:
        print("Sorry that's not enough money. Money refunded.")
        end_program() 

def end_program():
    done_ordering == True

while done_ordering == False:
    drink_choice = start_machine()

    if drink_choice == "espresso" or drink_choice == 'latte' or drink_choice == 'cappuccino':
        total_inserted = money_inserted()
        if drink_choice == "espresso":
            espresso()
        elif drink_choice == "latte":
            latte()
        elif drink_choice == "cappuccino":
            cappuccino()
    elif drink_choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
        start_machine()
    else:
        print("Wrong Input")
        
    
total_inserted += money



