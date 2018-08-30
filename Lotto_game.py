from random import randint


class LottoCard:

    def __init__(self, name):
        lotto_pool = [x for x in range(1, 91)]
        self.card = [
            LottoCard.make_str_card(lotto_pool),
            LottoCard.make_str_card(lotto_pool),
            LottoCard.make_str_card(lotto_pool)
                     ]
        self.name = name
        self.max_numb = 15

    @staticmethod
    # Объявляем метод создания карточки
    def make_str_card(lotto_pool):
        #Создаем пустой словарь с 9 элементами
        lotto_card = ['' for _ in range(9)]
        #Механизм генерации случайной позиции в строке по условию из 5 штук
        for x in range(8,3,-1):
            num = randint(0,x)
            # Проверяем если строка пуста, то берем рандомное число из пула бочонков + удаляем сразу используемое значение
            while lotto_card[num] != '':
                num += 1
            lotto_card[num] = lotto_pool.pop(randint(0, len(lotto_pool) - 1))
        return lotto_card
    #Переопределяем метод вывода строки
    def __str__(self):
        lotto_str = '{:-^26}\n'.format(self.name)
        for x in range(3):
            #Форматируем строку под условия задачи!
            lotto_str += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'\
                    .format(*self.card[x]) + '\n'
        return lotto_str + '-' * 26
class Game:

    def __init__(self, player, npc='Компьютер'):
        self._player = player
        self._npc = npc
    def start(self):
        lotto_pool = [x for x in range(1, 91)]
        game_count = 0
        while True:
            if len(lotto_pool) > 0:
                new_round = lotto_pool.pop(randint(0,len(lotto_pool) - 1))
                game_count += 1
                print(f'[Ход {game_count}] Выпал бочонок: {new_round}!(В мешке осталось: {len(lotto_pool)})\n')
                print(player)
                print(npc)
                confirm = (input('Зачеркнуть цифру? (y/n)'))
                confirm = confirm.lower()
                if confirm == 'y':
                    check = False
                    for x in range(3):
                        if new_round in player.card[x]:
                            check = True
                            player.card[x][player.card[x].index(new_round)] = '-'
                            player.max_numb -= 1
                        if new_round in npc.card[x]:
                            check = True
                            npc.card[x][npc.card[x].index(new_round)] = '-'
                            npc.max_numb -= 1
                    if check:
                        if player.max_numb < 1:
                            print('Вы победили! Поздравляю!')
                            break
                        if npc.max_numb < 1:
                            print('Победил компьютер!')
                            break
                elif confirm == 'n':
                    check = False
                    for x in range(3):
                        if new_round in player.card[x]:
                            print('Вы проиграли, так как данное число есть на Вашей карточке!')
                            check = True
                            break
                        if new_round in npc.card[x]:
                            npc.card[x][npc.card[x].index(new_round)] = '-'
                            npc.max_numb -= 1
                    if check:
                        break
                else:
                    print('Нет такой команды!')
                    break
            else:
                print('Закончились бочонки в мешке!')
                break

player = LottoCard('Artem')
npc = LottoCard('Компьютер')
game = Game(player,npc)
game.start()