#Логика игры:
def play_drunkard_game(player1, player2):
    from collections import deque
    
    deck1 = deque(player1)
    deck2 = deque(player2)
    rounds = 0
    max_rounds = 10**6

    while deck1 and deck2:
        if rounds > max_rounds:
            return "botva"
        
        card1 = deck1.popleft()
        card2 = deck2.popleft()
        
        if (card1 > card2 and not (card1 == 9 and card2 == 0)) or (card1 == 0 and card2 == 9):
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card1)
            deck2.append(card2)
        
        rounds += 1

    if deck1:
        return f"first {rounds}"
    else:
        return f"second {rounds}"
#Механизм взаимодействия с пользователем:
def main():
    print("Добро пожаловать в игру 'Пьяница'!")
    print("Введите карты первого игрока (5 чисел, разделенных пробелами):")
    player1 = list(map(int, input().strip().split()))
    print("Введите карты второго игрока (5 чисел, разделенных пробелами):")
    player2 = list(map(int, input().strip().split()))

    result = play_drunkard_game(player1, player2)
    
    if "first" in result:
        winner = "первый игрок"
    elif "second" in result:
        winner = "второй игрок"
    else:
        winner = "Ничья"

    print("\nРезультаты игры:")
    if result == "botva":
        print("Игра длилась слишком долго и закончилась ничьей (botva).")
    else:
        rounds = result.split()[1]
        print(f"Победитель: {winner}")
        print(f"Количество ходов: {rounds}")

if __name__ == "__main__":
    main()
