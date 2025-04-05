import datetime

now = datetime.datetime.now().strftime('%Y-%m-%d')
print(now)

timestamp = 1743277332
utc_time = datetime.datetime.fromtimestamp(timestamp, tz=datetime.UTC)
print(utc_time)
today = datetime.date.today()

print(f"Its", today)


def player(name):
    print(f"Hello it's, {name.upper()}")
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    
player("frank")

