from collections import deque

END_COMMAND = 'END'
GREEN_COMMAND = 'green'

duration_green_light = int(input())
duration_free_window = int(input())

road = deque()
passed_cars_counter = 0
is_crashed = False
car = ''
hit_char = ''

while True:
    data = input()
    if data == END_COMMAND:
        print('Everyone is safe.')
        print(f'{passed_cars_counter} total cars passed the crossroads.')
        break

    if is_crashed:
        print('A crash happened!')
        print(f'{car} was hit at {hit_char}.')
        break

    if not data == GREEN_COMMAND:
        car = data
        road.append(car)
    else:
        green_time = duration_green_light
        free_time = duration_free_window
        while green_time > 0 and road:
            car = road.popleft()
            time_to_pass = len(car)
            # ако времето, което ще отнеме
            # на автомобила да премине е достатъчно
            # (т.е. по-малко) от оставащото време на зелен светофар
            if time_to_pass < green_time:
                passed_cars_counter += 1
                green_time -= time_to_pass
            else:
                # зеленото е свършило, проверка дали
                # ще има време да се изтегли от кръстовището
                remaining_time = time_to_pass - green_time
                if free_time >= remaining_time:
                    passed_cars_counter += 1
                    break
                else:
                    is_crashed = True
                    hit_char_pos = -(remaining_time - free_time)
                    hit_char = car[hit_char_pos]
