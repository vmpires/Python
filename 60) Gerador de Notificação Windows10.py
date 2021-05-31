from win10toast import ToastNotifier

# Carrega o pacote
toaster = ToastNotifier()

# Pede um corpo para a notificação
notificacao = input('Insira o corpo da notificação: ')

# Passa parâmetros da notificação e a exibe
toaster.show_toast(
    "Notificação",
    notificacao,
    threaded=True,
    icon_path = None, # uma imagem pode ser incluída na notificação
    duration = 3 # quantos segundos fica na tela
)