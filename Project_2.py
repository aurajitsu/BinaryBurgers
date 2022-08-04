####################################################
# CS 31, Prof. Muldrow
# Name: Victoria Clemente
# Assignment: Project 2
# Due Date: May 1st, 2022
####################################################
def main():
    print('Binary Burgers')
    orderNum = 0
    try:
        OrdersToProcess = int(input("How Many Orders?:"))
    except ValueError:
        print('Please enter a number value.')

    while OrdersToProcess < 1:
        print("Please enter a valid number of orders.")
        OrdersToProcess = int(input("How Many Orders?:"))

    #processing orders
    while orderNum < OrdersToProcess:
        orderNum += 1
        showMenu()
        print('---------Processing Order#',orderNum,'------------')
        #take order inputs and write into file.
        entreeOrder,entreeName = getInputEntree()
        sideOrder,sideName = getInputSide()
        drink,drinkSize,drinkName,drinkSizeName = getInputDrink()
        #calculate totals
        subtotal = getSubtotal(entreeOrder,sideOrder,drinkSize)
        SalesTax = subtotal * 0.08
        Total = subtotal + SalesTax
        # print totals
        print('-----Total for Order#',orderNum,'---------')
        print(format(entreeName,'20')+'$'+format(numToPriceEntree(entreeOrder),'6.2f'))
        print(format(sideName,'20')+'$'+format(numToPriceSide(sideOrder),'6.2f'))
        comboName = drinkSizeName + drinkName
        print(format(comboName,'20')+'$'+format(numToPriceDrinkSize(drinkSize),'6.2f'))
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(format('Subtotal:','20')+'$'+format(subtotal,'6.2f'))
        print(format('Sales Tax:','20')+'$'+format(SalesTax,'6.2f'))
        print(format('Total:','20')+'$'+format(Total,'6.2f'))
        writeOrderFile(orderNum, entreeOrder, entreeName, sideOrder, sideName, drinkSize, drinkName, drinkSizeName,
                       subtotal, SalesTax, Total)

def writeOrderFile(orderNum,entreeOrder,entreeName,sideOrder,sideName,drinkSize,drinkName,drinkSizeName,subtotal,SalesTax,Total):
    if orderNum == 1:
        OrdersFile = open('classes completed/Python class/Project2/OrdersFile.txt', 'w')
        comboName = drinkSizeName + drinkName
        comboName = format(comboName,'20')+'$'+format(numToPriceDrinkSize(drinkSize),'6.2f')
        OrdersFile.write('--------------Total of Order#'+str(orderNum)+'--------------'+'\n')
        OrdersFile.write(str(format(entreeName,'20')+'$'+format(numToPriceEntree(entreeOrder),'6.2f')+'\n'))
        OrdersFile.write(str(format(sideName,'20')+'$'+format(numToPriceSide(sideOrder),'6.2f')+'\n'))
        OrdersFile.write(str(comboName)+'\n')
        OrdersFile.write(str('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'+'\n'))
        OrdersFile.write(str(format('Subtotal:','20')+'$'+format(subtotal,'6.2f')+'\n'))
        OrdersFile.write(str(format('Sales Tax:','20')+'$'+format(SalesTax,'6.2f')+'\n'))
        OrdersFile.write(str(format('Total:','20')+'$'+format(Total,'6.2f')+'\n'))
        OrdersFile.close()
    elif orderNum > 1:
        OrdersFile = open('classes completed/Python class/Project2/OrdersFile.txt', 'a')
        comboName = drinkSizeName + drinkName
        comboName = format(comboName, '20') + '$' + format(numToPriceDrinkSize(drinkSize), '6.2f')
        OrdersFile.write('--------------Total of Order#' + str(orderNum) + '--------------' + '\n')
        OrdersFile.write(str(format(entreeName, '20') + '$' + format(numToPriceEntree(entreeOrder), '6.2f') + '\n'))
        OrdersFile.write(str(format(sideName, '20') + '$' + format(numToPriceSide(sideOrder), '6.2f') + '\n'))
        OrdersFile.write(str(comboName) + '\n')
        OrdersFile.write(str('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + '\n'))
        OrdersFile.write(str(format('Subtotal:', '20') + '$' + format(subtotal, '6.2f') + '\n'))
        OrdersFile.write(str(format('Sales Tax:', '20') + '$' + format(SalesTax, '6.2f') + '\n'))
        OrdersFile.write(str(format('Total:', '20') + '$' + format(Total, '6.2f') + '\n'))
        OrdersFile.close()

def showMenu():
    # Print out Menu, have user select menu items by number
    print("~~~~~MENU~~~~~")
    print('Sandwiches: #1 Hamburger:$2.75\t#2 Cheeseburger:$3.25\t#3 Chicken Sandwich:$2.50\t#4 No Sandwich.')
    print('Side Orders: #1 French Fries:$2.25\t#2 Onion Rings:$1.75\t#3 Side Salad:$1.50\t#4 No Side.')
    print('Drinks: #1 Coke\t#2 Sprite\t#3 Lemonade\t#4 Cup of Water is free')
    print('Drink Sizes: #1 Small $1.50\t#2 Medium $2.25\t#3 Large $2.75')
    print('All orders are charged 8% sales tax')

def getInputEntree():
    entree = 0
    entreeName =''
    while entree !='':
        entree = int(input('Enter a Sandwich: '))
        if entree == 1:
            entreeName = 'Hamburger'
            return entree, entreeName
        elif entree == 2:
            entreeName = 'Cheeseburger'
            return entree, entreeName
        elif entree == 3:
            entreeName = 'Chicken Sandwich'
            return entree, entreeName
        elif entree == 4:
            entree = 0
            entreeName = ''
            return entree, entreeName
        else:
            print('Only Enter Options 1-4.')

def getInputSide():
    menu = 0
    while menu == 0:
        side = int(input('Enter a Side Order: '))
        if 1 <= side <=4:
            if side == 1:
                sideName = 'French Fries'
                return side,sideName
            elif side == 2:
                sideName = 'Onion Rings'
                return side,sideName
            elif side == 3:
                sideName = 'Side Salad'
                return side,sideName
            elif side == 4:
                side = 0
                sideName = ''
                return side,sideName
        else:
            print('Only Enter Options 1-4.')

def getInputDrink():
    menu = 0
    while menu !='':
        drink = int(input('Enter a Drink: '))
        if 1 <= drink <= 3:
            drinkSize,drinkSizeName = getInputSize()
            if drink == 1:
                drinkName = 'Coke'
                return drink,drinkSize,drinkName,drinkSizeName
            elif drink == 2:
                drinkName = 'Sprite'
                return drink,drinkSize,drinkName,drinkSizeName
            elif drink == 3:
                drinkName = 'Lemonade'
                return drink,drinkSize,drinkName,drinkSizeName
        elif drink == 4:
            drinkSize = 4
            drinkName = 'Cup of Water'
            drinkSizeName ='' #TODO -remove space - so text is aligned
            return drink,drinkSize,drinkName,drinkSizeName
        elif drink < 0 or drink > 4:
            print('Only Enter Options 1-4.')

def getInputSize():
    menu = 0
    while menu ==0:
        size = int(input('Enter a Drink Size: '))
        if 1 <= size <=3:
            if size == 1:
                drinkSizeName = 'Small '
                return size,drinkSizeName
            elif size == 2:
                drinkSizeName = 'Medium '
                return size,drinkSizeName
            elif size == 3:
                drinkSizeName = 'Large '
                return size,drinkSizeName
            elif size == 4:
                size = 0
                drinkSizeName = 'Cup of Water'
                return size,drinkSizeName
        else:
            print('Only Enter a valid Size 1-3')


def getSubtotal(entreeOrder,sideOrder,drinkSize):
    #add variables here
    subtotal = numToPriceEntree(entreeOrder) + numToPriceSide(sideOrder) + numToPriceDrinkSize(drinkSize)
    #print(subtotal)
    return subtotal

#change num entry to a price
def numToPriceEntree(entree):
    if entree == 1:
        return 2.75
    elif entree == 2:
        return 3.25
    elif entree == 3:
        return 2.50
    elif entree == 4:
        return 0
    elif entree == 0:
        return 0
    else:
        return 'Only Enter Options 1-4.'

def numToPriceSide(sideOrder):
    if sideOrder == 1:
        return 2.25
    elif sideOrder == 2:
        return 1.75
    elif sideOrder == 3:
        return 1.50
    elif sideOrder == 4:
        return 0
    elif sideOrder == 0:
        return 0
    else:
        return 'Only Enter Options 1-4.'

def numToPriceDrinkSize(drinkSize):
    if drinkSize == 1:
        return 1.50
    elif drinkSize == 2:
        return 2.25
    elif drinkSize == 3:
        return 2.75
    elif drinkSize == 4:
        return 0
    else:
        return 'Only Enter Options:1-Small, 2-Med or 3-Large'


# def enterOrders():
#     OrdersToProcess = int(input("How Many Orders?:"))
#     while OrdersToProcess > 0:
#     # take order inputs and write into file.
#         OrdersFile = open('OrdersFile.txt','w')
#         for x in range(1,OrdersToProcess):
            # if each one of these is a fuc, call functions here and remove inputs
            # Sandwich =
            # SideOrder =
            # Drink =
            # OrdersFile.write(Sandwich +'\n')
            # OrdersFile.write(SideOrder + '\n')
            # OrdersFile.write(Drink + '\n')
        OrdersFile.close()
    # else:
    #     print("Please enter a valid number of orders.")
    #     OrdersToProcess = input("How Many Orders?:")

main()