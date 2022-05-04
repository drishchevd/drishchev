def get_worker():
    
        name = input("Пункт назначения рейса? ")
        post = input("Тип самолета? ")
        year = int(input("Номер рейса? "))
        # Создать словарь.
        return {
            'name': name,
            'post': post,
            'year': year,
               }

def display_workers(staff):
        if staff:
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    "№",
                    "Пункт назначения",
                    "Тип самолета",
                    "Номер рейса"
                )
            )
            print(line)
            
            for idx, worker in enumerate(staff, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                        idx,
                        worker.get('name', ''),
                        worker.get('post', ''),
                        worker.get('year', 0)
                     )
                  )
            print(line)
        else:
            print("Не существует пунктов назначения")

def select_workers(staff, period):
        """
        Выбрать место назначения с определенным номером рейса.
        """
        today = date.today()
        result = []
        for employee in staff:
            if today.year - employee.get('year', today.year) >= period:
                result.append(employee)
        return result
