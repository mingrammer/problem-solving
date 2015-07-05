import datetime
d, m = map(int, raw_input().split())
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print days[datetime.date(2009, m, d).weekday()]
