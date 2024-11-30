import pandas as pd
import json
import datetime
import os
import csv
import notes
from notes import *
from tasks import *
from contacts import *
from financial_records import *
from calculator import *

def main_menu():    
    print('Добро пожаловать в Персональный помощник!)')
    while True:
        print('Выберите действие: \n 1. Управление заметками \n 2. Управление задачами \n 3. Управление контактами \n 4. Управление финансовыми записями \n 5. Калькулятор \n 6. Выход')
        choise = input('Выберите номер действия:')
        if choise == '1':
            menu_notes()
        elif choise == '2':
            menu_tasks()
        elif choise == '3':
            menu_contacts()
        elif choise == '4':
            menu_financial_records()
        elif choise == '5':
            menu_calculator()
        elif choise == '6':
            exit()
        else:
            print('Введите корректное значение:')
            main_menu()
    
if __name__ == '__main__':
    main_menu()