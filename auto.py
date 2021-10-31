#bad practise, but i could not figure out cron:/
import schedule
import time
import final
def task():
    print("Job Executing!")
    final.runnin()

schedule.every(6).hours.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
