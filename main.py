import psutil
from plyer import notification
import time

while True:
    battery = psutil.sensors_battery()
    percent = battery.percent

    if percent >= 95:
        notification.notify(
            title="Battery Full",
            message="Your laptop battery is 95% charged!",
            app_name="Battery Percentage Monitor"
        )

    if percent <= 20:
        notification.notify(
            title="Battery Low",
            message="Your laptop battery is running low. Please connect your charger.",
            app_name="Battery Percentage Monitor"
        )

    time.sleep(60)  # check battery percentage every 60 seconds
