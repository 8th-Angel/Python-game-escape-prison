# Дополнительно
fail_count = 0
valible_ending = 0
endings = set()
password_for_box = [1, 2, 3, 5]
win = False
# Экипировка для каждого уровня
spisok_ulik = {
    1 : "Схема банка",
    2 : "Мешок для денег",
    3 : "Лопата",
    4 : "Неизвестное устройство",
    5 : "Компас",
    6 : "Записка от врача",
}
start_equipment = ("1: Напильник", "2: Супер Энергетик", "3: Телепорт", "4: Рокетница", "5: Телефон", "6: Бур", "7: Кваратный ключ")
basement_equipment = ("1: Неизвестный переключатель", "2: Монтировка")
sides = ("1: Лево", "2: Право")
side_2 = ("1: Налево", "2: По стене")
krisha_equipment = ("1: Гарпун","2: Вантуз","3: Парашют ","4: Реактивный ранец")
store_room = ("1: Стул", "2: Ремень со связкой гранат")
side_pipe = ("1: Налево", "2: Направо")

# Главное меню
print("Добро пожаловать в игру Escape prison")
while True:
    end = False
    print("Что вы хотите открыть: 1: Начать игру, 2: Посмотреть открытые концовки, 3: Посмотреть количество смертей 4: Выход")
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
                                                fail_count += 1
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
                                                    print("Вы выбираете на крышу и перед вами есть 4 предмета")
                                                    print(krisha_equipment)
                                                    do_now = int(input("Что вы выберете: "))
                                                    if do_now == 1:
                                                        print("Вы скатываетесь по верёвке прямо на обочину дороги\nНо внезапно вас сбивает машина (FAILED)")
                                                        fail_count += 1
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
                                                        endings.add("Вы сбегаете через грыщу с помощью присосок")
                                                        valible_ending += 1
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
                                                        fail_count += 1
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
                                                        fail_count += 1
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
                                    fail_count += 1
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
                            fail_count += 1
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
                    fail_count += 1
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
                    fail_count += 1
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
                    fail_count += 1
                    print("Хотите начать сначала: 1) да 2) нет, вернуться на прошлый шаг")
                    do_now = int(input("Введите число: "))
                    if do_now == 1:
                        end = True
                    elif do_now == 2:
                        print()
                    else:
                        print("введите правильное число")
                case 5:
                    while True:
                        if end == True:
                            break
                        print("Вы звоните Адвокату, и он обещает вам помочь")
                        print("В день суда у обвеняемого обнаружили улики")
                        print(spisok_ulik)
                        do_now = int(input("Введите число: "))
                        if do_now == 1:
                            print(f"Вы выбрали {spisok_ulik[do_now]}")
                            print("Эта схема доказывает что вы действительно грабили банк в день преступления \nВас обратно посадили (FAILED)")
                            fail_count += 1
                            print("Хотите начать сначала: 1) да 2) нет, вернуться на прошлый шаг")
                            do_now = int(input("Введите число: "))
                            if do_now == 1:
                                end = True
                            elif do_now == 2:
                                print()
                            else:
                                print("введите правильное число")
                        elif do_now == 2:
                            print(f"Вы выбрали {spisok_ulik[do_now]}")
                            print("Этот мешок доказывает что вы действительно грабили банк в день преступления \nВас обратно посадили (FAILED)")
                            fail_count += 1
                            print("Хотите начать сначала: 1) да 2) нет, вернуться на прошлый шаг")
                            do_now = int(input("Введите число: "))
                            if do_now == 1:
                                end = True
                            elif do_now == 2:
                                print()
                            else:
                                print("введите правильное число")
                        elif do_now == 3:
                            print(f"Вы выбрали {spisok_ulik[do_now]}")
                            print("Этот лопата доказывает что вы сделали подкоп и ограбили банк в день преступления \nВас обратно посадили (FAILED)")
                            fail_count += 1
                            print("Хотите начать сначала: 1) да 2) нет, вернуться на прошлый шаг")
                            do_now = int(input("Введите число: "))
                            if do_now == 1:
                                end = True
                            elif do_now == 2:
                                print()
                            else:
                                print("введите правильное число")
                        elif do_now == 4:
                            print(f"Вы выбрали {spisok_ulik[do_now]}")
                            print("Это оказался телефон в котором нашли твои фото с друзьями на рыбалке в день преступления")
                            print("Вас оправдали!!!!!!!")
                            win = True
                            print("Хотите начать сначала: 1) да 2) нет, вернуться на прошлый шаг")
                            do_now = int(input("Введите число: "))
                            if do_now == 1:
                                end = True
                            elif do_now == 2:
                                print()
                            else:
                                print("введите правильное число")
                        elif do_now == 5:
                            print(f"Вы выбрали {spisok_ulik[do_now]}")
                            print("Этот компас  доказывает что в сбежали благодаря нему в день преступления \nВас обратно посадили (FAILED)")
                            fail_count += 1
                            print("Хотите начать сначала: 1) да 2) нет, вернуться на прошлый шаг")
                            do_now = int(input("Введите число: "))
                            if do_now == 1:
                                end = True
                            elif do_now == 2:
                                print()
                            else:
                                print("введите правильное число")
                        elif do_now == 6:
                            print(f"Вы выбрали {spisok_ulik[do_now]}")
                            print("Эта бумажка от врача доказывает что в день преступления вы были на сеансе")
                            print("Вас освободили!!!!!!!!")
                            win = True
                            print("Хотите начать сначала: 1) да 2) нет, вернуться на прошлый шаг")
                            do_now = int(input("Введите число: "))
                            if do_now == 1:
                                end = True
                            elif do_now == 2:
                                print()
                            else:
                                print("введите правильное число")
                        else:
                            print("Введите верное число")

# Это БУР тут ничего не трогать!!!!!!
                case 6:
                    print("Вы бурите пол и попадаете в подвал")
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
                    while True:
                        if end:
                            break
                        print(f"В коробке лежат несколько инструментов {basement_equipment}")
                        do_now = int(input("Введите порядковый номер инструмента: "))
                        match do_now:
                            case 1:
                                print("Этот пульт сделал вас призраком теперь вы летите к центру земли (FAILED)")
                                fail_count += 1
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
                                                fail_count += 1
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
                                                            fail_count += 1
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
                case 7:
                    print("Разве не очевидно что квадратный ключ не к чему не подойдёт? (FAILED)")
                    fail_count += 1
                    print("Хотите начать сначала: 1) да 2) нет, вернуться на прошлый шаг")
                    do_now = int(input("Введите число: "))
                    if do_now == 1:
                        end = True
                    elif do_now == 2:
                        print()
                    else:
                        print("введите правильное число")
                case _:
                    print("Введите правильное число")
# Тут бур заканчивается
    elif do_now == 2 and valible_ending >= 1:
        print(endings)
    elif do_now == 2:
        print("У вас еще нет открытых концовок")
    elif do_now == 3:
        print(fail_count)

    elif do_now == 4:
        print("Вы вышли из игры")
        break
    else:
        print("Вы ввели неправильное число")
if win:
    print("Поздравляю вы успешно сбежали из тюрьмы")
else:
    print("Вам не удалось сбежать с тюрьмы")
