from datetime import datetime as dt
import time

filePath = "./hosts"
website_list = ["www.facebook.com", "facebook.com", "www.twitter.com", "twitter.com"]
redirect_ip = "127.0.0.1"
# 9 to 16 working hours

while True:
    currentTime = dt.now()
    if dt(currentTime.year, currentTime.month, currentTime.day, 9) < currentTime < dt(currentTime.year, currentTime.month, currentTime.day, 15):
        print("Working hours...")
        with open(filePath, "r+") as f:
            content = f.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    f.write(redirect_ip+" "+website+"\n")
    else:
        print("Fun time")
        with open(filePath, "r+") as f:
            content = f.readlines()

            f.seek(0)

            for line in content:
                if not any(website in line for website in website_list):
                    f.write(line)

            f.truncate()

    time.sleep(5)