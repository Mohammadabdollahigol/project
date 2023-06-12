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
while emtiaz_p1 <3 or emtiaz_p2 <3:
    print('chap')
    print('rast')
    player1 = (input('player 1 lotfan harkat khod ra entekhab konid: '))
    randomnumber = random.randint(1,2)
    if randomnumber==1:
        player2='chap' 
        print('entekhab player2=', player2)
    elif randomnumber==2:
        player2='rast'
        print('entekhab player2=', player2)
    if player1==player2:
        print('Player 1 Win')
        emtiaz_p1 +=1

    else:
        print ('Player 2 Win')
        emtiaz_p2 +=1
    print('\n')
    print(f"emtiaz_p1 : {emtiaz_p1}")
    print(f"emtiaz_p2 : {emtiaz_p2}")
    if emtiaz_p1 == 3 or emtiaz_p2 == 3:
        break
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')