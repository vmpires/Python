import instaloader

bot = instaloader.Instaloader()

username = "artesobscurae"

print(bot.download_profile(username, profile_pic_only=True))