from app import app, functions
from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler(daemon = True)
sched.add_job(functions.recordatorio, 'cron', hour = 8, minute = 0)

if __name__ == "__main__":      
    app.run(debug = True)