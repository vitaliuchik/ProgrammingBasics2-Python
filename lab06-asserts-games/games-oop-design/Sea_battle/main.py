import game

if __name__ == '__main__':
    field1 = game.Field()
    field2 = game.Field()
    player1 = game.Player(field1, field2)
    player2 = game.Player(field2, field1)

    end = False
    while True:
        player1_status = 'injure'
        player2_status = 'injure'

        while player1_status != 'past':
            pos = tuple(map(int, input('Player1 - y,x: ').split(',')))
            if pos[0] < 1 or pos[0] > 10 or pos[1] < 1 or pos[1] > 10:
                print("Incorrect input")
                continue

            player1_status = player1.enemy_field.shoot_at(pos)
            print('\n' + player1_status + '\n')
            print("Own field")
            print(player1.get_own_field())
            print("Enemy field")
            print(player1.get_enemy_field())


        if player1.enemy_field.kill_count == 10:
            print('Player1 won!')
            break

        while player2_status != 'past':
            pos = tuple(map(int, input('Player2 - y,x: ').split(',')))
            if pos[0] < 1 or pos[0] > 10 or pos[1] < 1 or pos[1] > 10:
                print("Incorrect input")
                continue

            player2_status = player2.enemy_field.shoot_at(pos)
            print('\n' + player2_status + '\n')
            print("Own field")
            print(player2.get_own_field())
            print("Enemy field")
            print(player2.get_enemy_field())


        if player2.enemy_field.kill_count == 10:
            print('Player2 won!')
            break