import psutil
from plyer import notification
from win10toast import ToastNotifier
import time

toaster = ToastNotifier()

while True:
    battery = psutil.sensors_battery()
    percent = battery.percent

    if percent >= 95:
        # notification.notify(
        #     title="Battery Full",
        #     message="Your laptop battery is 95% charged!",
        #     app_name="Battery Percentage Monitor"
        # )
        toaster.show_toast("Battery Protection", f"Battery is {percent} charged", duration=10)


    if percent <= 20:
        # notification.notify(
        #     title="Battery Low",
        #     message="Your laptop battery is running low. Please connect your charger.",
        #     app_name="Battery Percentage Monitor"
        # )
        toaster.show_toast("Battery Protection", f"Battery is {percent} charged", duration=10)

    time.sleep(60)  # check battery percentage every 60 seconds
