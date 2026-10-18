# Дополнительно
valible_ending = 0
endings = set()
password_for_box = [1, 2, 3, 5]
win = False
# Экипировка для каждого уровня
start_equipment = ("1: Напильник", "2: Супер Энергетик", "3: Телепорт", "4: Рокетница", "5: Телефон", "6: Бур")
basement_equipment = ("1: Неизвестный переключатель", "2: Монтировка")
sides = ("1: Лево", "2: Право")
side_2 = ("1: Налево", "2: По стене")
krisha_equipment = ("1: Гарпун","2: Вантуз","3: Парашют ","4: Реактивный ранец")
store_room = ("1: Стул", "2: Ремень со связкой гранат")
side_pipe = ("1: Налево", "2: Направо")
bur_equipment = ("1: Коробка с кодовым паролем", "2: Лом" )

# Главное меню
print("Добро пожаловать в игру Escape prison")
while True:
    end = False
    print("Что вы хотите открыть: 1: Начать игру, 2: Посмотреть открытые концовки, 3: Выход")
    do_now = int(input("Введите цифру: "))
    if do_now == 1:

#Начало игры
        print("Предусловие: Вы стикман заключенный обладающий невероятным везением и внезапными суперспособностями, ваша цель сбежать из тюрьмы")
        print("Некто подарил вам коробку, там лежит торт внутри торта вы обнаруживаете несколько инструментов")
        while True:
            if end:
                break
            print(start_equipment)
            do_now = int(input("Введите порядковый номер инструмента: "))
            match do_now:
                case 1:
                    while True:
                        if end:
                            break
                        print("Вы можете распилить только решётку у окна или решётку камеры")
                        do_now = int(input("Что выберете? Решётка камеры - 1; решётка у окна - 2: "))
                        if do_now == 1:
                            while True:
                                if end:
                                    break
                                print(f"Вы вырубаете двух полицейских и скрываетесь в кладовке, там вы находите {store_room}")
                                do_now = int(input("Введите порядковый номер инструмента: "))
                                if do_now == 1:
                                    print("Вы подставляете стул и ползёте по трубе")
                                    while True:
                                        if end:
                                            break
                                        print(f"Куда поползёте {side_pipe}")
                                        do_now = int(input("Введите номер стороны: "))
                                        match do_now:
                                            case 1:
                                                print("Вы вылезаете в соседнюю камеру  к полиции (FAILED)")
                                                print("Хотите начать сначала: 1) да 2) нет, вернуться на прошлый шаг")
                                                do_now = 0
                                                while do_now not in range(1, 3):
                                                    do_now = int(input("Введите число: "))
                                                    if do_now == 1:
                                                        end = True
                                                    elif do_now == 2:
                                                        print()
                                                    else:
                                                        print("Введите правильное число")
                                            case 2:
                                                while True:
                                                    if end:
                                                        break
                                                    print(f"Вы выбираете на крышу и перед вами есть 4 предмета {krisha_equipment}")
                                                    do_now = int(input("Что вы выберете: "))
                                                    if do_now == 1:
                                                        print("Вы скатываетесь по верёвке прямо на обочину дороги\nНо внезапно вас сбивает машина (FAILED)")
                                                        print("Хотите начать сначала: 1) да 2) нет, вернуться на прошлый шаг")
                                                        do_now = 0
                                                        while do_now not in range(1, 3):
                                                            do_now = int(input("Введите число: "))
                                                            if do_now == 1:
                                                                end = True
                                                            elif do_now == 2:
                                                                print()
                                                            else:
                                                                print("Введите правильное число: ")
                                                    elif do_now == 2:
                                                        print("По присоскам вы спускаетесь с крыши тюрьмы до земли и успешно сбегаете!!!!!!!")
                                                        print("Хотите перейти к выбору кнопок?: 1) да 2) нет, вернуться на прошлый шаг")
                                                        do_now = 0
                                                        while do_now not in range(1, 3):
                                                            do_now = int(input("Введите число: "))
                                                            if do_now == 1:
                                                                end = True
                                                                win = True
                                                            elif do_now == 2:
                                                                print()
                                                            else:
                                                                print("Введите правильное число: ")

                                                    elif do_now == 3:
                                                        print("Вы одеваете рюкзак с парашютом и прыгаете с крыши тюрьмы но в полёте парашют не раскрывается\nВы упали и разбились (FAILED)")
                                                        print("Хотите перейти к выбору кнопок?: 1) да 2) нет, вернуться на прошлый шаг")
                                                        do_now = 0
                                                        while do_now not in range(1, 3):
                                                            do_now = int(input("Введите число: "))
                                                            if do_now == 1:
                                                                end = True
                                                            elif do_now == 2:
                                                                print()
                                                            else:
                                                                print("Введите правильное число: ")
                                                    elif do_now == 4:
                                                        print("Вы одеваете реактивный ранец\nНо он оказался неуправляемым и с ним вы влетели прямо в стену тюрьмы (FAILED)")
                                                        print("Хотите перейти к выбору кнопок?: 1) да 2) нет, вернуться на прошлый шаг")
                                                        do_now = 0
                                                        while do_now not in range(1, 3):
                                                            do_now = int(input("Введите число: "))
                                                            if do_now == 1:
                                                                end = True
                                                            elif do_now == 2:
                                                                print()
                                                            else:
                                                                print("Введите правильное число: ")
                                                    else:
                                                        print()
                                                        print("Вы ввели неправильное число")





                                            case _:
                                                print("введите правильное число")
                                elif do_now == 2:
                                    print("Вы выбрасываете гранату из комнаты, но она рикошетом прилетает обратно в вас (FAILED)")
                                    print("Хотите начать сначала: 1) да 2) нет, вернуться на прошлый шаг")
                                    do_now = 0
                                    while do_now not in range(1, 3):
                                        do_now = int(input("Введите число: "))
                                        if do_now == 1:
                                            end = True
                                        elif do_now == 2:
                                            print()
                                        else:
                                            print("введите правильное число")
                                else:
                                    print("введите правильное число")
                        elif do_now == 2:
                            print("Вы распиливаете решётку окна и сразу прыгаете в неё.\nВы упали с высокого этажа (FAILED)")
                            print("Хотите начать сначала: 1) да 2) нет, вернуться на прошлый шаг")
                            do_now = 0
                            while do_now not in range(1,3):
                                do_now = int(input("Введите число: "))
                                if do_now == 1:
                                    end = True
                                elif do_now == 2:
                                    print()
                                else:
                                    print("Введите правильное число")


                case 2:
                    print()
                    print("Вы выпиваете супер энергетик, время замедляется, вы ломаете решётку одним прикосновением пальца, никто не может вам помешать сбежать и вот вы уже у выхода, \nНо действие энергетика заканчивается сердце не выдерживает и у вас случается сердечный приступ (FAILED)")
                    print("Хотите начать сначала: 1) да 2) нет, вернуться на прошлый шаг")
                    do_now = int(input("Введите число: "))
                    if do_now == 1:
                        end = True
                    elif do_now == 2:
                        print()
                    else:
                        print("введите правильное число")
                case 3:
                    print("Вы телепортируетесь на стрельбище и в вас застреливают (FAILED)")
                    print("Хотите начать сначала: 1) да 2) нет, вернуться на прошлый шаг")
                    do_now = int(input("Введите число: "))
                    if do_now == 1:
                        end = True
                    elif do_now == 2:
                        print()
                    else:
                        print("введите правильное число")
                case 4:
                    print("Камера оказалась слишком маленькой и вы взрываете себя (FAILED)")
                    print("Хотите начать сначала: 1) да 2) нет, вернуться на прошлый шаг")
                    do_now = int(input("Введите число: "))
                    if do_now == 1:
                        end = True
                    elif do_now == 2:
                        print()
                    else:
                        print("введите правильное число")
                case 5:
                    # Можешь поменять если не будет хватать строк там дальше есть прохождение
                    print("Вы звоните Адвокату но он не поднимет трубку (FAILED)")
                    print("Хотите начать сначала: 1) да 2) нет, вернуться на прошлый шаг")
                    do_now = int(input("Введите число: "))
                    if do_now == 1:
                        end = True
                    elif do_now == 2:
                        print()
                    else:
                        print("введите правильное число")
                case 6:
                    print("Вы бурите пол и попадаете в подвал")
                    print(f"Вы встречаете {bur_equipment}")
                    do_now = int(input("Что выберете "))
                    if do_now == 1:
                        print("В подвале вы находите коробку с кодовым паролем, благо вы умеете взламывать эти замки")
                        steps_box = 0
                        for position_password_number, password_number in enumerate(password_for_box, start=1):
                            while True:
                                user_input = int(input(f"Введите цифру {position_password_number} пароля: "))
                                if 0 <= user_input <= 9:
                                    steps_box += 1
                                    if user_input == password_number:
                                        print(f"Верно {position_password_number} угадана")
                                        break
                                    elif user_input < password_number:
                                        print("Звук щелчка говорит что число больше")
                                    elif user_input > password_number:
                                        print("Звук щелчка говорит что число меньше")
                                else:
                                    print("Введите число от 0 до 9")
                        print(f"Вы взломали пароль {password_for_box} за {steps_box} попыток")
                        print(f"В коробке лежат несколько инструментов {basement_equipment}")
                        while True:
                            if end:
                                break
                            do_now = int(input("Введите порядковый номер инструмента: "))
                            match do_now:
                                case 1:
                                    print("Этот пульт сделал вас призраком теперь вы летите к центру земли (FAILED)")
                                    print("Хотите начать сначала: 1) да 2) нет, вернуться на прошлый шаг")
                                    do_now = int(input("Введите число: "))
                                    if do_now == 1:
                                        end = True
                                    elif do_now == 2:
                                        print()
                                    else:
                                        print("введите правильное число")
                                case 2:
                                    print("Вы через люк проходите к трубе и случайно падаете прям к охранникам, вам нужно срочно бежать")
                                    while True:
                                        if end:
                                            break
                                        print(f"Куда повернете? {sides}")
                                        do_now = int(input("Введите Сторону: "))
                                        match do_now:
                                            case 1:
                                                print("Вы завернули в тупик (FAILED)")
                                                print("Хотите начать сначала: 1) да 2) нет, вернуться на прошлый шаг")
                                                do_now = int(input("Введите число: "))
                                                if do_now == 1:
                                                    end = True
                                                elif do_now == 2:
                                                    print()
                                                else:
                                                    print("введите правильное число")
                                            case 2:
                                                print("Вы бежите дальше по коридору")
                                                while True:
                                                    if end:
                                                        break
                                                    print(f"Впереди поворот, что будете делать {side_2}")
                                                    do_now = int(input("Введите куда будете бежать: "))
                                                    match do_now:
                                                        case 1:
                                                            print("Вы подскользнулись на повороте и упали (FAILED)")
                                                            print("Хотите начать сначала: 1) да 2) нет, вернуться на прошлый шаг")
                                                            do_now = int(input("Введите число: "))
                                                            if do_now == 1:
                                                                end = True
                                                            elif do_now == 2:
                                                                print()
                                                            else:
                                                                print("введите правильное число")
                                                        case 2:
                                                            print("Вы бежите по стене, перепрыгиваете через полицейских, все вспоминают кто вы, вас начинают бояться и вы спокойно выходите из тюрьмы (WIN)")
                                                            valible_ending += 1
                                                            endings.add("Вы показали свои суперспособности и полицейские в страхе выпустили вас")
                                                            end = True
                                                        case _:
                                                            print("Введите правильное число")
                                            case _:
                                                print("Введите правильное число")
                                case _:
                                    print("Введите правильное число")
                    elif do_now == 2:
                        while True:
                            if end:
                                break
                            print("Вы берёте лом и открываете люк который находиться на полу")
                            print("Вы спускаетесь в него и оказываетесь в коридоре с полицейскими")
                            print("Вы убегаете")
                            print(f"В какую сторону побежите {side_pipe}")
                            do_now = int(input("Что выберете "))
                            if do_now == 1:
                                while True:
                                    if end:
                                        break
                                    print("Вы сворачиваете налево и продолжаете бежать")
                                    print("Спереди развилка")
                                    print("Куда повернёте (1: Налево, 2: Продолжить бежать прямо)")
                                    do_now = int(input("Введите число: "))
                                    if do_now == 1:
                                        print("Вы сворачиваете за угол но там вас уже ждёт полиция")
                                        print("Вас поймали (FAILED)")
                                        print("Хотите перейти к выбору кнопок?: 1) да 2) нет, вернуться на прошлый шаг")
                                        do_now = 0
                                        while do_now not in range(1, 3):
                                            do_now = int(input("Введите число: "))
                                            if do_now == 1:
                                                end = True
                                            elif do_now == 2:
                                                print()
                                            else:
                                                print("Введите правильное число: ")
                                    elif do_now == 2:
                                        while True:
                                            if end:
                                                break
                                            print("Вы бежите прямо в стену и отскакиваете от неё через полицейских")
                                            print("Теперь вас окружили полицейские которые готовы в любую секунду открыть огонь")
                                            print("Что выберете (1: Убежать, 2: Уклониться от пуль )")
                                            do_now = int(input("Введите число: "))
                                            if do_now == 1:
                                                print("Вы пытались убежать но полицейские открыли огонь (FAILED)")
                                                print("Хотите перейти к выбору кнопок?: 1) да 2) нет, вернуться на прошлый шаг")

                                                do_now = 0
                                                while do_now not in range(1, 3):
                                                    do_now = int(input("Введите число: "))
                                                    if do_now == 1:
                                                        end = True
                                                    elif do_now == 2:
                                                        print()
                                                    else:
                                                        print("Введите правильное число: ")
                                            elif do_now == 2:
                                                while True:
                                                    if end:
                                                        break
                                                    print("Вы уклонились от всех пуль")
                                                    print("Полицейские друг друга переубивали")
                                                    print("Вы выходите из тюрьмы но перед вами стена")
                                                    print("Что выберете (1: Перелезть через стену, 2: Сделать подкоп)")
                                                    do_now = int(input("Введите число: "))
                                                    if do_now == 1:
                                                        print("Вы начали перелезать через стену но запутались в проволке которая стоит на вершине (FAILED)")
                                                        print( "Хотите перейти к выбору кнопок?: 1) да 2) нет, вернуться на прошлый шаг")
                                                        do_now = 0
                                                        while do_now not in range(1, 3):
                                                            do_now = int(input("Введите число: "))
                                                            if do_now == 1:
                                                                end = True
                                                            elif do_now == 2:
                                                                print()
                                                            else:
                                                                print("Введите правильное число: ")
                                                    elif do_now == 2:
                                                        print("Вы делаете подкоп и успешно выбираетесь из тюрьмы!!!!!!")
                                                        print("Хотите перейти к выбору кнопок?: 1) да 2) нет, вернуться на прошлый шаг")
                                                        do_now = 0
                                                        while do_now not in range(1, 3):
                                                            do_now = int(input("Введите число: "))
                                                            if do_now == 1:
                                                                end = True
                                                                win = True
                                                            elif do_now == 2:
                                                                print()
                                                            else:
                                                                print("Введите правильное число: ")

                                                    else:
                                                        print("Введите правильное число")

                                            else:
                                                print("Введите правильное число")

                                    else:
                                        print("Введите правильное число")


                            elif do_now == 2:
                                print("Вы поворачиваете направо но врезаетесь в стену")
                                print("Вас ловит полиция (FAILED)")
                                print("Хотите начать сначала: 1) да 2) нет, вернуться на прошлый шаг")
                                do_now = int(input("Введите число: "))
                                if do_now == 1:
                                    end = True
                                elif do_now == 2:
                                    print()
                                else:
                                    print("введите правильное число")
                            else:
                                print("Введите правильное число")



                case _:
                    print("Введите правильное число")
    elif do_now == 2 and valible_ending >= 1:
        print(endings)
    elif do_now == 2:
        print("У вас еще нет открытых концовок")
    elif do_now == 3:
        print("Вы вышли из игры")
        break
    else:
        print("Вы ввели неправильное число")

if win:
    print("Поздравляю вы успешно сбежали из тюрьмы")
else:
    print("Вам не удалось сбежать с тюрьмы")