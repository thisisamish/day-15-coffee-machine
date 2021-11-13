# "Coffee Machine" program written by - Amish Verma
# Twitter - www.twitter.com/thisisamish
# GitHub - www.github.com/thisisamish

# Importing data about coffee types
import data

is_off = False

# Declaring and initialize coffee resources variables
curr_water = 1000
curr_milk = 500
curr_coffee = 760
total_money = 0


# Defining the coffee_machine function
def coffee_machine(curr_water, curr_milk, curr_coffee, total_money):
    global is_off
    while not is_off:
        user_response = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # Turning the coffee machine off
        if user_response == "off":
            is_off = True

        # Providing a report of the resources currently available
        elif user_response == "report":
            print(f"Water: {curr_water}ml")
            print(f"Milk: {curr_milk}ml")
            print(f"Coffee: {curr_coffee}g")
            print(f"Money: ${total_money}")
        elif user_response == "espresso" or "latte" or "cappuccino":

            # Creating a coffee type list so as to ease the process of accessing data about the various coffee types
            coffee_type_list = ['espresso', 'latte', 'cappuccino']

            # Checking if the resources available to coffee machine are enough to make the ordered coffee
            if curr_water >= data.coffee_ingredients[coffee_type_list.index(user_response)]['water']:
                if curr_milk >= data.coffee_ingredients[coffee_type_list.index(user_response)]['milk']:
                    if curr_coffee >= data.coffee_ingredients[coffee_type_list.index(user_response)]['coffee']:

                        # Asking to enter coins for the ordered coffee
                        quarters = float(input("Enter quarters: "))
                        dimes = float(input("Enter dimes: "))
                        nickles = float(input("Enter nickles: "))
                        pennies = float(input("Enter pennies: "))

                        # Calculating the total money entered as coins in dollars
                        money_entered = (data.coin_value['quarter'] * quarters) \
                                        + (data.coin_value['dime'] * dimes) \
                                        + (data.coin_value['nickle'] * nickles) \
                                        + (data.coin_value['penny'] * pennies)

                        # Checking if money entered is equal to, greater than or lower than the cost of the coffee
                        if money_entered == data.coffee_ingredients[coffee_type_list.index(user_response)]['cost']:
                            total_money += money_entered
                            curr_water -= data.coffee_ingredients[coffee_type_list.index(user_response)]['water']
                            curr_milk -= data.coffee_ingredients[coffee_type_list.index(user_response)]['milk']
                            curr_coffee -= data.coffee_ingredients[coffee_type_list.index(user_response)]['coffee']
                            print(f"Here is your {data.coffee_ingredients[coffee_type_list.index(user_response)]['coffee_type']}. Enjoy!")

                            # Asking for a new order after the current order has been served.
                            coffee_machine(curr_water, curr_milk, curr_coffee, total_money)

                        elif money_entered > data.coffee_ingredients[coffee_type_list.index(user_response)]['cost']:

                            # Returning the extra money entered
                            return_amt = money_entered - data.coffee_ingredients[coffee_type_list.index(user_response)]['cost']
                            print(f"Here is ${return_amt} in change.")

                            total_money += money_entered - return_amt
                            curr_water -= data.coffee_ingredients[coffee_type_list.index(user_response)]['water']
                            curr_milk -= data.coffee_ingredients[coffee_type_list.index(user_response)]['milk']
                            curr_coffee -= data.coffee_ingredients[coffee_type_list.index(user_response)]['coffee']
                            print(f"Here is your {data.coffee_ingredients[coffee_type_list.index(user_response)]['coffee_type']}. Enjoy!")

                            # Asking for a new order after the current order has been served.
                            coffee_machine(curr_water, curr_milk, curr_coffee, total_money)

                        elif money_entered < data.coffee_ingredients[coffee_type_list.index(user_response)]['cost']:
                            print(f"Sorry that's not enough money. Money refunded.")

                            # Asking for a new order after the money for current order is refunded.
                            coffee_machine(curr_water, curr_milk, curr_coffee, total_money)

                    else:
                        print("Sorry there is not enough coffee.")
                else:
                    # Checking to see if there's enough milk and coffee so as to provide correct feedback to the user.
                    if not curr_coffee >= data.coffee_ingredients[coffee_type_list.index(user_response)]['coffee']:
                        print("Sorry there is not enough milk and coffee.")
            else:
                string = "Sorry there is not enough water."

                # Checking to see if there's enough milk and coffee so as to provide correct feedback to the user.
                if not curr_milk >= data.coffee_ingredients[coffee_type_list.index(user_response)]['milk']:
                    string = "Sorry there is not enough milk and water."
                if not curr_coffee >= data.coffee_ingredients[coffee_type_list.index(user_response)]['coffee']:
                    string = "Sorry there is not enough milk, water and coffee."

                print(string)


# Calling the coffee_machine function
coffee_machine(curr_water, curr_milk, curr_coffee, total_money)
