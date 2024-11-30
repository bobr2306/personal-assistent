
def menu_calculator():
    print('Простейший калькулятор')
    print(' 1. Вычислить выражение \n 2. Вернуться в главное меню')
    choice = input('Введите: ')
    if choice == '1':
        calc = input('Введите ваш простое выражение для вычисления:')
        try: 
            answer = eval(calc)
        except:
            print('Ошибка в выражении')
        else:
            print(answer)
        menu_calculator()
    elif choice == '2':
        exit
    else:
        print('Введите корректное значение: ')
        menu_calculator()