from datetime import datetime, timedelta

users = [
    {
        "name": "Aleksandra", "birthday": "2000-01-26"
    },
    {
        "name": "Helen", "birthday": "1975-07-13"
    },
    {
        "name": "Georgiy", "birthday": "1999-05-30"
    },
    {
        "name": "Viktoria", "birthday": "2000-05-21"
    },
    {
        "name": "Anna", "birthday": "1981-05-20"
    },
    {"name": "Zoya", "birthday": "1975-05-23"}
]


def get_birthdays_per_week(users: list) -> dict:
    result = {}
    mon = []
    tue = []
    wed = []
    thu = []
    fri = []
    date_now = datetime.now()
    for i in users:
        birthday = i.get("birthday")
        birt = datetime.strptime(birthday, '%Y-%m-%d')
        other_birt = birt.replace(year=date_now.year)
        difference = other_birt.date() - date_now.date()
        if timedelta(-1) <= difference <= timedelta(7):
            d = datetime.weekday(other_birt)
            if d == 0 or d == 5 or d == 6:
                mon.append(i['name'])
            if d == 1:
                tue.append(i['name'])
            if d == 2:
                wed.append(i['name'])
            if d == 3:
                thu.append(i['name'])
            if d == 4:
                fri.append(i['name'])

            result.update({'Monday': mon, 'Tuesday': tue,
                           'Wednesday': wed, 'Thursday': thu, 'Friday': fri})

    for k, v in result.items():
        if len(v) != 0:
            print(k + ': ' + ', '.join(v))


get_birthdays_per_week(users)
