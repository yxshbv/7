#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Список .
    train = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break
        elif command == 'add':
            # Запросить данные .
            race = input("Название пункта выезда ")
            race1 = input("Название пункта прибытия ")
            number = input("Номер маршрута ")
            
            # Создать словарь.
            trains = {
                'race': race,
                'number': number,
                'race1': race1,
            }
            # Добавить словарь в список.
            train.append(trains)
            # Отсортировать список в случае необходимости.
            if len(train) > 1:
                train.sort(key=lambda item: item.get('race', ''))
        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                    "No",
                    "Пункт выезда",
                    "Пункт прибытия",
                    "Номер"
                    
                )
            )
            print(line)
            # Вывести данные о всех рейсах.
            for idx, trains in enumerate(train, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                        idx,
                        trains.get('race', ''),
                        trains.get('race1', ''),
                        trains.get('number', '')
                        
                    )
                )
            print(line)
        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)
            sel = (parts[1])
            count = 0
            for trains in train:
                if trains.get('race') == sel:
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, trains.get('race', ''))
                    )
                    print('Номер маршрута:', trains.get('number', ''))
                    
            # Если счетчик равен 0, то рейсы не найдены.
            if count == 0:
                print("Маршрут не найден.")
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить маршрут;")
            print("list - вывести список маршрутов;")
            print("select <товар> - информация о маршруте;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print("Неизвестная команда {command}", file=sys.stderr)
