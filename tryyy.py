import schedule
import time
import new_n
def task():
    print("Job Executing!")
    new_n.runnin()

schedule.every(6).hours.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
