username=input("lotfan shomare daneshjooee khod ra vared konid:")
while username !="1401231014":
   print('shomare daneshjooee eshtebahe')
   username=input("lotfan shomare daneshjooee khod ra vared konid:")
password=input("lotfan kode melli khod ra vared konid:")
while password != "0650171004" :
   print('kode melli eshtebahe')
   password=input("lotfan kode melli khod ra vared konid:")
print(" shoma vared shodid ")  
import random
emtiaz_p1 = 0
emtiaz_p2 = 0
while emtiaz_p1 <=3 or emtiaz_p2 <=3:
    print('sang')
    print('kaghaz')
    print('gheichi')
    player1 = (input('player 1 lotfan harkat khod ra entekhab konid: '))
    randomnumber = random.randint(1,3)
    if randomnumber==1:
        player2='sang' 
        print('entekhab player2=', player2)
    elif randomnumber==2:
        player2='kaghaz'
        print('entekhab player2=', player2)
    elif randomnumber==3:
        player2='gheichi'
        print('entekhab player2=', player2)
    if player1==player2:
        print('mosavi')
    elif player1 == 'sang' and player2 =='kaghaz' :
        print ('player 2 win')
        emtiaz_p2 +=1
    elif player1 == 'sang' and player2 =='gheichi' :
        print ('player 1 win')
        emtiaz_p1 +=1
    elif player1 == 'kaghaz' and player2 =='sang' :
        print ('player 1 win') 
        emtiaz_p1 +=1
    elif player1 == 'kaghaz' and player2 =='gheichi' :
        print ('player 2 win')
        emtiaz_p2 +=1
    elif player1 == 'gheichi' and player2 =='sang' :
        print ('player 2 win')
        emtiaz_p2 +=1
    elif player1 == 'gheichi' and player2 =='kaghaz' :
        print ('player 1 win')
        emtiaz_p1 +=1
    else:
        print ('ye chizi eshtebahe')
    print('\n')
    print(f"emtiaz_p1 : {emtiaz_p1}")
    print(f"emtiaz_p2 : {emtiaz_p2}")
    if emtiaz_p1 == 3 or emtiaz_p2 == 3:
        break
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')