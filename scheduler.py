from apscheduler.schedulers.blocking import BlockingScheduler
from bot import monitor_workflow

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', minutes=10)
def scheduled_check():
    monitor_workflow()

if __name__ == "__main__":
    scheduler.start()
