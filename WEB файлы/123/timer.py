import schedule

count = 0
def job():
    global count
    count += 1
    print('Hello!')


schedule.every(2).seconds.do(job)
schedule.every().day.at('7:00').do(job)
while True:
    schedule.run_pending()
    if count > 10:
        break