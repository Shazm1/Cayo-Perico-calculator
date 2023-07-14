import time
count_players = 0
bag_main = 1
spawn_gold = 0
spawn_cash = 0
spawn_paint = 0

cost_main = 0
cost_gold = 0
cost_cash = 0
cost_paint = 0

extra_summ = 0
all_summ = 0

def welcome():
    print('Hey! Its nice to see you there!')
    print('This is  shazmones Cayo Perico Calculator v1.0.0')
    print('Last update date: 07/14/23')
    
def asks():
    global hardmode
    global count_players
    global bag_main
    global spawn_gold
    global spawn_cash
    global spawn_paint
    global spawn_cocaine
    global spawn_weed
    global cost_cocaine
    global cost_weed
    global cost_main
    global cost_gold
    global cost_cash
    global cost_paint
    global all_summ
    
    print('')
    print('Please, answer some questions:')
    print('')
    hardmode = input('Is Hard Mode on(y/n): ')
    count_players = input('Amount of players(1-4): ')
    print('1. Pink Diamond; 2. Bearer Bonds; 3. Tequila; 4. Ruby Necklace; 5. Panther Statue;')
    bag_main = input('The Main target(1-4): ')
    spawn_gold = input('Amount of Gold Spawned(0-6): ')
    spawn_paint = input('Amount of Paintings Spawned(0-5): ')
    spawn_cash = input('Amount of Cash Spawned(0-12): ')
    spawn_cocaine = input('Amount of Cocaine Spawned(0-12): ')
    spawn_weed = input('Amount of Weed Spawned(0-12): ')

def summ():
    global hardmode
    global count_players
    global bag_main
    global spawn_gold
    global spawn_cash
    global spawn_paint  
    global spawn_cocaine
    global spawn_weed
    global cost_cocaine
    global cost_weed
    global cost_main
    global cost_gold
    global cost_cash
    global cost_paint
    global all_summ

    if bag_main == "1":
        cost_main = 1300000
        
    if bag_main == "2":
        cost_main = 1100000
    
    if bag_main == "3":
        cost_main = 900000
        
    if bag_main == "4":
        cost_main = 1000000
        
    if bag_main == "5":
        cost_main = 1900000

    max_bag_limit = 99.9999 * float(count_players)
    bag_limit = 0
    
    gold_limit = 67
    gold_summ = 0
    gold_stack_price = 330888
    bag_gold = 0

    cash_limit = 25
    cash_summ = 0
    cash_stack_price = 83950
    bag_cash = 0
    
    paint_limit = 50
    paint_summ = 0
    paint_stack_price = 187950
    bag_paint = 0
    
    cocaine_limit = 50
    cocaine_summ = 0
    cocaine_stack_price = 222750
    bag_cocaine = 0
    
    weed_limit = 50
    weed_summ = 0
    weed_stack_price = 147623
    bag_weed = 0

    while max_bag_limit >= bag_limit: # +GOLD
        if float(spawn_gold) >= 1:
            bag_limit = bag_limit + float(gold_limit)
            spawn_gold = float(spawn_gold) - 1
            bag_gold = float(bag_gold) + 1       

        else:
            break
    
    while max_bag_limit >= bag_limit: # +COCAINE
        if float(spawn_cocaine) >= 1:
            bag_limit = bag_limit + float(cocaine_limit)
            spawn_cocaine = float(spawn_cocaine) - 1
            bag_cocaine = float(bag_cocaine) + 1
        else:
            break 
    
    while max_bag_limit >= bag_limit: # +PAINTS
        if float(spawn_paint) >= 1:
            bag_limit = bag_limit + float(paint_limit)
            spawn_paint = float(spawn_paint) - 1
            bag_paint = float(bag_paint) + 1       

        else:
            break  
        
    while max_bag_limit >= bag_limit: # +CASH
        if float(spawn_cash) >= 0.005:
            bag_limit = bag_limit + 0.125
            bag_cash = float(bag_cash) + 0.005
            spawn_cash = float(spawn_cash) - 0.005       

        else:
            break
        
        
    while max_bag_limit >= bag_limit: # +WEED
        if float(spawn_weed) >= 0.005:
            bag_limit = bag_limit + 0.1875
            bag_weed = float(bag_weed) + 0.005
            spawn_weed = float(spawn_weed) - 0.005       

        else:
            break
    
    print('')
    print('')
    
    gold_summ = float(bag_gold) * gold_stack_price
    cash_summ = float(bag_cash) * cash_stack_price
    paint_summ = float(bag_paint) * paint_stack_price
    cocaine_summ = float(bag_cocaine) * cocaine_stack_price
    weed_summ = float(bag_weed) * weed_stack_price
    
    extra_summ = gold_summ + cash_summ + paint_summ + cocaine_summ +weed_summ
    
    if str(hardmode) == 'y':
        cost_main = cost_main * 1.1
    else:
        cost_main = cost_main
        
    all_summ = extra_summ + cost_main
    all_summ = all_summ * 0.88 + 74000
    
    print('Take', round(bag_gold, 1), 'gold stacks')
    print(round(bag_gold, 1), 'Gold Stacks costs: ', round(gold_summ))
    print('')
    print('Take', round(bag_cash, 1), 'cash stacks')
    print(round(bag_cash, 1), 'Cash Stacks costs: ', round(cash_summ))
    print('')
    print('Take', round(bag_paint, 1), 'paints')
    print(round(bag_paint, 1), 'paints costs: ', round(paint_summ))
    print('')
    print('Take', round(bag_cocaine, 1), 'cocaine stacks')
    print(round(bag_cocaine, 1), 'Cocaine Stacks costs: ', round(cocaine_summ))
    print('')
    print('Take', round(bag_weed, 1), 'weed stacks')
    print(round(bag_weed, 1), 'Weed Stacks costs: ', round(weed_summ))
    print('')
    print('')
    print('Extra Targets cost: ', round(extra_summ))
    print('Main Target cost: ', round(cost_main))
    
    
    print('Profit: ', round(all_summ), '(-12% fee; +~74000$ from safe.)')
   
def perc():
    global count_players
    global bag_main
    global spawn_gold
    global spawn_cash
    global spawn_paint
    global cost_main
    global cost_gold
    global cost_cash
    global cost_paint
    global all_summ
    
    print('')
    perc = input('Your cut(15-100): ')
    user_cut = all_summ / 100 * int(perc)
    print('Is about.. ', round(user_cut),'$')
    time.sleep(300)
    print('Cya!')
    
welcome()
asks()
summ()
perc()