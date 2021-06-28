import speedtest

test = speedtest.Speedtest()
down = test.download()
upload = test.upload()

print(f"Download Speed: {down:.2f} mb.")
print(f"Upload Speed: {upload:.2f} mb.")