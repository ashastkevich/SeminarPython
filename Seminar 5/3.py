"""
Создайте программу для игры в Крестики-нолики
"""
win = False
counter = 0
my_list = list(range(1,10))
def print_list(my_list):
    for i in range(3):
        print(my_list[i*3], my_list[i*3+1], my_list[i*3+2])
def game_move(my_list, N, player):
    if N in my_list:
        if player == 0:
            my_list[my_list.index(N)] = "X"
        else:
            my_list[my_list.index(N)] = "O"
    else:
        print("Неправильный ход")
def check_win(my_list):
    win_list = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in win_list:
        if my_list[each[0]] == my_list[each[1]] == my_list[each[2]]:
            global win
            win = True
            return my_list[each[0]]
    return False
print_list(my_list)
while not check_win(my_list):
    player = counter % 2
    N = int(input(f"Ход игрока {player}: "))
    game_move(my_list, N, player)
    counter += 1
    print_list(my_list)
    if counter == 9:
        print("Ничья!")
        break  
if win:
    print("Игрок ", player, "выиграл!")