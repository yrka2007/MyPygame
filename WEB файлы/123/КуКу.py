import datetime
import schedule


def kuku():
    current_time = datetime.datetime.now()
    print("-".join(["Ку"] * int(str(current_time).split()[1].split(':')[0])))


schedule.every().hour.at(':00').do(kuku)

while True:
    schedule.run_pending()
