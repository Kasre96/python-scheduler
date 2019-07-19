from app import app
from app import ProgramKilled, task, signal_handler, Job
import datetime
import time
import signal


WAIT_TIME_SECONDS = 10

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    job = Job(interval=datetime.timedelta(seconds=WAIT_TIME_SECONDS), execute=task)
    job.start()

    while True:
        try:
            time.sleep(2)
        except ProgramKilled:
            print("Program killed: running cleanup code")
            job.stop()
            break
