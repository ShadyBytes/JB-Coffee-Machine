# print('Starting to make a coffee')
# print('Grinding coffee beans')
# print('Boiling water')
# print('Mixing boiled water with crushed coffee beans')
# print('Pouring coffee into the cup')
# print('Pouring some milk into the cup')
# print('Coffee is ready!')
import math

# water_per_cup = 200
# milk_per_cup = 50
# beans_g_per_cup = 15

# print('{0} ml of water'.format(water_per_cup * cups_amount))
# print('{0} ml of milk'.format(milk_per_cup * cups_amount))
# print('{0} g of coffee beans'.format(beans_g_per_cup * cups_amount))

# available_water = int(input('Write how many ml of water the coffee machine has:\n'))
# available_milk = int(input('Write how many ml of milk the coffee machine has:\n'))
# available_beans = int(input('Write how many grams of coffee beans the coffee machine has:\n'))
# cups_requested = int(input('Write how many cups of coffee you will need:\n'))


# limit_factor_list = [available_water / water_per_cup, available_milk / milk_per_cup, available_beans / beans_g_per_cup]
# max_cups_can_do = math.floor(min(limit_factor_list))


# if max_cups_can_do == cups_requested:
#     print('Yes, I can make that amount of coffee')
# elif max_cups_can_do > cups_requested:
#     print('Yes, I can make that amount of coffee (and even {0} more than that)'.format(max_cups_can_do - cups_requested))
# elif max_cups_can_do < cups_requested:
#     print('No, I can make only {0} cups of coffee'.format(max_cups_can_do))

machine_money = 550
machine_water = 400
machine_milk = 540
machine_beans = 120
machine_cups = 9


def display_supplies():
    global machine_water, machine_money, machine_milk, machine_milk, machine_beans, machine_cups
    print('The coffee machine has:')
    print('{0} of water'.format(machine_water))
    print('{0} of milk'.format(machine_milk))
    print('{0} of coffee beans'.format(machine_beans))
    print('{0} of disposable cups'.format(machine_cups))
    print('{0} of money'.format(machine_money))


# display_supplies()


def buy():
    global machine_water, machine_money, machine_milk, machine_milk, machine_beans, machine_cups
    buy_option = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    espresso_water = 250
    espresso_beans = 16
    espresso_cost = 4

    latte_water = 350
    latte_milk = 75
    latte_beans = 20
    latte_cost = 7

    cappuccino_water = 200
    cappuccino_milk = 100
    cappuccino_beans = 12
    cappuccino_cost = 6

    if buy_option == '1' and machine_water >= espresso_water and machine_beans >= espresso_beans:
        print('I have enough resources, making you a coffee!')
        machine_water -= espresso_water
        machine_beans -= espresso_beans
        machine_money += espresso_cost
        machine_cups -= 1
    elif buy_option == '1' and machine_water < espresso_water:
        print('Sorry, not enough water!')
    elif buy_option == '1' and machine_beans >= espresso_beans:
        print('Sorry, not enough beans!')

    elif buy_option == '2' and machine_water >= latte_water and machine_beans >= latte_beans \
            and machine_milk >= latte_milk:
        print('I have enough resources, making you a coffee!')
        machine_water -= latte_water
        machine_beans -= latte_beans
        machine_milk -= latte_milk
        machine_money += latte_cost
        machine_cups -= 1
    elif buy_option == '2' and machine_water >= latte_water:
        print('Sorry, not enough water!')
    elif buy_option == '2' and machine_beans >= latte_beans:
        print('Sorry, not enough beans!')
    elif buy_option == '2' and machine_milk >= latte_milk:
        print('Sorry, not enough milk!')

    elif buy_option == '3' and machine_water >= cappuccino_water and machine_beans >= cappuccino_beans \
            and machine_milk >= cappuccino_milk:
        print('I have enough resources, making you a coffee!')
        machine_water -= cappuccino_water
        machine_beans -= cappuccino_beans
        machine_milk -= cappuccino_milk
        machine_money += cappuccino_cost
        machine_cups -= 1
    elif buy_option == '3' and machine_water >= cappuccino_water:
        print('Sorry, not enough water!')
    elif buy_option == '3' and machine_beans >= cappuccino_beans:
        print('Sorry, not enough beans!')
    elif buy_option == '3' and machine_milk >= cappuccino_milk:
        print('Sorry, not enough milk!')

    elif buy_option == 'back':
        pass

    # display_supplies()


def fill():
    global machine_water, machine_milk, machine_milk, machine_beans, machine_cups

    filled_water = int(input('Write how many ml of water do you want to add:\n'))
    machine_water += filled_water

    filled_milk = int(input('Write how many ml of milk do you want to add:\n'))
    machine_milk += filled_milk

    filled_beans = int(input('Write how many grams of coffee beans do you want to add:\n'))
    machine_beans += filled_beans

    filled_cups = int(input('Write how many disposable cups of coffee do you want to add:\n'))
    machine_cups += filled_cups

    # display_supplies()


def take():
    global machine_money
    print('I gave you ${0}'.format(machine_money))
    machine_money = 0

    # display_supplies()


# action = input('Write action (buy, fill, take):')
# if action == 'buy':
#     buy()
# elif action == 'fill':
#     fill()
# elif action == 'take':
#     take()
# elif action == 'remaining':
#     display_supplies()
# elif action == 'exit':
#     break

while True:
    action = input('Write action (buy, fill, take, remaining, exit):')
    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    elif action == 'remaining':
        display_supplies()
    elif action == 'exit':
        break
