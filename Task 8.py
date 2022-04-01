
print('=================Task8.1=================')
while True:
    print('welcome to vending machine')
    user=input('Hey sir/mam do uh want to buy something or exit : \n')
    if user =='buy':
        pass
    elif user=='exit':
        break
    print ('What would you like to have?')
    chocolates = 200
    icecream =   200
    chips =  200
    drinks= 200
    juices= 200
    customer=input('Chocolates, Juices, Ice cream, Chips ,Cold drink \n')
    if customer =='chocolates':
        print('Which one do you like?')
        flavour= input('dairy milk, perk, kitkat, twix, mars \n')
        dairymilk = 40
        perk= 40
        kitkat = 40
        twix =40
        mars= 40
        if flavour== 'dairy milk':
            dairymilk-= 1
            print('Here is your order,Thank you')
        elif flavour =='perk':
            perk -= 1
            print('Here is your order. thank you')
        elif flavour=='kitkat':
            kitkat-=1
            print('Here is your order. Thank you')
        elif flavour=='twix':
            twix-=1
            print('Here is your order. Thank you!')
        elif flavour == 'mars':
            mars-=1
            print('Here is your order. thank you')
        else :
            print ('Sorry sir! Try again.')
    elif customer == 'juice':
        print('Which one do you like?')
        apple=40
        slice = 40
        red_grapes = 40
        chounsa = 40
        orange =40
        flavour= input('Slice, Apple, Red grapes, Chounsa, Orange \n')
        if flavour =='slice':
            slice-= 1
            print('Here is your Order. Thank you')
        elif flavour=='apple':
            apple-=1
            print ('Here is your order. Thank you')
        elif flavour== 'orange':
            orange-= 1
            print('Here is your order. Thank you')
        elif flavour =='red grapes':
            red_grapes -= 1
            print('Here is your order. Thank you')
        elif flavour=='chounsa':
            chounsa-=1
            print('Here is your order. Thank you')
        else :
            print ('Sorry sir! Try again.')
    elif customer=='ice cream':
        print('Which one do you like?')
        flavour=input('mango, pista, orange,vanilla,rainbow \n')
        mango=40
        pista=40
        rainbow=40
        orange=40
        vanilla=40
        if flavour== 'pista':
            pista-= 1
            print('Here is your order. thank you')
        elif flavour =='mango':
            mango -= 1
            print('Here is your order. Thank you')
        elif flavour=='rainbow':
            rainbow-=1
            print('Here is your order. Thank you')
        elif flavour=='orange':
            orange-=1
            print('Here is your order. Thank you')
        elif flavour == 'vanilla':
            vanilla-=1
            print('Here is your order. Thank you')
        else :
            print ('Sorry sir! Try again.')
    elif customer=='chips':
        print('which one do you like?')
        flavour=input('lays, kurkure,  kurleez, wavy \n')
        lays=40
        kurkure=40
        wavy=40
        kurleez=40
        asli=40
        if flavour== 'lays':
            lays-= 1
            print('Here is your order.thank you')
        elif flavour=='kurkure':
            kurkure-=1
            print('Here is your order.Thank you')
        elif flavour=='kurleez':
            kurleez-=1
            print('Here is your order. Thank you')
        elif flavour == 'wavy':
            wavy-=1
            print('Here is your order.Thank you')
        else :
            print ('Sorry sir! Try again.')
    elif customer=='cold drink':
        print('Which one do you like?')
        flavour=input('pepsi, marinda, 7up, sprite, deo \n')
        deo=40
        sprite=40
        pepsi=40
        up=40
        marinda=40
        if flavour== 'pepsi':
            pepsi-= 1
            print('Here is your order. Thank you')
        elif flavour =='marinda':
            marinda-= 1
            print('Here is your order.thank you')
        elif flavour=='sprite':
            sprite-=1
            print('Here is your order.thank you')
        elif flavour=='7up':
            up-=1
            print('Here is your order.Thank you')
        elif flavour == 'deo':
            deo-=1
            print('Here is your order.Thank you')
        else :
            print ('Sorry sir! Try again.')
print('Thank you for shoping.')


print('==================task8.2========================')
print('hello welcome to ATM machine')
Amount = 5000
print('select the option 1,2,3,4')
option = int(input('1.check balnce ,2.withdraw , 3.deposit amount,4.exit'))
if option==1:
    print('your current balance is:',Amount)
elif option == 2:
    x = int(input("Enter amount to withdraw"))
    if x > Amount:
        print('Insufficient balance')
    else:
        print('Amount withdrawn successfully!')

elif option == 3:
    y = int(input('Enter the amount you want to deposit'))
    Amount += y
    print('Amount Deposited successfully!')
    print('Your new balance is: ', Amount)
elif option==4:
        print('exit')
else:
    print('Invalid choice')
print('==========================task8.3========================')
print('control applications')
appliances = input('which one uh want to control please choose tv,fans,bulb,lights')
remote =input('on or off or exit')
if remote=='on':
    print('bulb is on')
elif remote=='off':
    print('bulb is off')
    if remote=='exit':
        print('terminate')
print('=========================Task8.4=====================')
print('Ac controller')
AC = int(input('what is temperature of room'))
if AC<16:
    print('the compressor of ac is off')
elif AC>20 :
    print('the compressor is on')


