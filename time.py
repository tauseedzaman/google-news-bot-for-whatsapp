from apscheduler.schedulers.blocking import BlockingScheduler
from main import send_love_message

sched = BlockingScheduler()

sched.add_job(send_love_message,'interval',seconds=21600)

sched.start()