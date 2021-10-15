import psutil

# Instancia o sensor da bateria #
battery = psutil.sensors_battery()

# Pega o percentual da bateria #
percent = str(battery.percent)

# Exibição do resultado #
print(f"Bateria atual do dispositivo: {percent}%.")