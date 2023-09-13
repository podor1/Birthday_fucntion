from collections import defaultdict
from datetime import date, datetime, timedelta

users = [
    {'name' : 'Fred', 'birthday': datetime(1996, 9, 16)},
    {'name' :'Dane', 'birthday': datetime(2003, 9, 15)},
    {'name' :'Barbar', 'birthday': datetime(2000, 9, 10)},
    {'name' :'Pacifica', 'birthday': datetime(2000, 9, 9)},
    {'name' :'Eliz', 'birthday' : datetime(2001, 9, 17)},
    {'name' :'Klar', 'birthday': datetime(2013, 8, 8)},
    {'name' :'Mike', 'birthday': datetime(2003, 9, 13)},
    {'name' :'Victor', 'birthday': datetime(2013, 9, 11)},
    {'name' :'Bett', 'birthday': datetime(2003, 8, 2)},
    {'name' :'Summer', 'birthday': datetime(2001, 9, 16)}
]


def get_birthdays(users) :
    if not users :
        return {}
    point_date = date.today()
    while point_date.strftime('%A') != 'Saturday' :
        point_date = point_date - timedelta(1)
    week_end = point_date + timedelta(6)
    users_birthdays = defaultdict(list)
    for user in users :
        user['birthday'] = (user['birthday'].date()).replace(year=date.today().year)
        if user['birthday'] < point_date :
            user['birhtday'] = user['birthday'].replace(year=date.today().year+1)

    while point_date <= week_end :
        for user in users:
            if user['birthday'] == point_date :
                day = user['birthday'].strftime('%A')
                if day == "Saturday" or day == "Sunday" :
                    users_birthdays["Monday"].append(user['name'])
                else :
                    users_birthdays[day].append(user['name'])
        point_date = point_date + timedelta(1)

    return users_birthdays

def main() :
    result = get_birthdays(users)
    for day, names in result.items() :
        print(f'{day} : {", ".join(names)}')

if __name__ == '__main__' :
    main()







