import threading

def fim():
    print('Acabou o tempo! Passaram-se 3 segundos.')

timer = threading.Timer(3.0, fim)

timer.start()