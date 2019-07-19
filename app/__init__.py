from flask import Flask
from config import *
import threading
import datetime

# App instance
app = Flask(__name__, instance_relative_config=True)

# Configuration
app.config.from_object(DevelopmentConfig)

# Ensure instance path exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass


# the logic
# Create a program killed Exception
class ProgramKilled(Exception):
    pass


# Method to track device data
def task():
    # Task to be executed
    now = datetime.datetime.utcnow()
    print(now)


def signal_handler(signum, frame):
    raise ProgramKilled


class Job(threading.Thread):
    def __init__(self, interval, execute, *args, **kwargs):
        threading.Thread.__init__(self)
        self.daemon = False
        self.stopped = threading.Event()
        self.interval = interval
        self.execute = execute
        self.args = args
        self.kwargs = kwargs

    def stop(self):
        self.stopped.set()
        self.join()

    def run(self):
        while not self.stopped.wait(self.interval.total_seconds()):
            self.execute(*self.args, **self.kwargs)
