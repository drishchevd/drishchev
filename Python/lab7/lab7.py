from mp import defpac


def main():
        """
        Главная функция программы.
        """
        workers = []
        while True:
            command = input(">>> ").lower()
            if command == 'exit':
                break
            elif command == 'add':
                worker = defpac.get_worker()
                workers.append(worker)
                if len(workers) > 1:
                    workers.sort(key=lambda item: item.get('name', ''))
            elif command == 'list':
                defpac.display_workers(workers)
            elif command.startswith('select '):
                parts = command.split(' ', maxsplit=1)
                period = int(parts[1])
                selected = defpac.select_workers(workers, period)
                defpac.display_workers(selected)
            elif command == 'help':
                print("Список команд:\n")
                print("add - Добавить рейс;")
                print("list - Вывести все рейсы;")
                print("select <стаж> - запросить пункт назначения с определенным номером рейса;")
                print("help - отобразить справку;")
                print("exit - завершить работу с программой.")
            else:
                print(f"Неизвестная команда {command}", file=defpac.sys.stderr)

if __name__ == '__main__':
    main()