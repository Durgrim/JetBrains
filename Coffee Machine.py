class Coffee():
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        

    def remaining(self):
        print('The coffee machine has:')
        print(str(self.water) + ' of water')
        print(str(self.milk) + ' of milk')
        print(str(self.beans) + ' of coffee beans')
        print(str(self.cups) + ' of disposable cups')
        print('$' + str(self.money) + ' of money')


    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        selection = str(input())
        if selection == '1':
            if self.water < 250:
                print('Sorry, not enough water!')
            elif self.beans < 16:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough disposable cups!')
            else:
                print('I have enough resources, making you a coffee!')
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
        elif selection == '2':
            if self.water < 350:
                print('Sorry, not enough water!')
            elif self.milk < 75:
                print('Sorry, not enough milk!')
            elif self.beans < 20:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough disposable cups!')
            else:
                print('I have enough resources, making you a coffee!')
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
        elif selection == '3':
            if self.water < 200:
                print('Sorry, not enough water!')
            elif self.milk < 100:
                print('Sorry, not enough milk!')
            elif self.beans < 12:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough disposable cups!')
            else:
                print('I have enough resources, making you a coffee!')
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
        elif selection == 'back':
            return
        

    def fill(self):
        print('Write how many ml of water do you want to add:')
        self.water += int(input())
        print('Write how many ml of milk do you want to add:')
        self.milk += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self.beans += int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        self.cups += int(input())

    def take(self):
        print('I gave you $' + str(self.money))
        self.money -= self.money
        
    
    def work(self):
        while True:
            print('Write action (buy, fill, take, remaining, exit):')
            action = str(input())
            if action == 'remaining':
                machine.remaining()
            elif action == 'fill':
                machine.fill()
            elif action == 'take':
                machine.take()
            elif action == 'buy':
                machine.buy()
            elif action == 'exit':
                break


machine = Coffee()
machine.work()
