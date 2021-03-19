import datetime

now = datetime.datetime.now()
weekday = now.strftime("%a")

print("Hoje é " + (now.strftime("%a, %b %d, %Y")))

if weekday == "Sat" or weekday == "Sun":
   print("Bom final de semana!")