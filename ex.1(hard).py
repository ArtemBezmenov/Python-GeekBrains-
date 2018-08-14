name = input('Введите Ваше имя:')
player = {'Player Name':name,'HP':100,'Dmg':20}
enemy = {'Player Name':'Enemy','HP':100,'Dmg':15}

def attack(player1,player2):
    dmg = player1['Dmg']
    new_hp = player2['HP'] - dmg
    player2['HP'] = new_hp
attack(player,enemy)
print (player,enemy)