# Get Window Notification
import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "Code And Code",
            timeout = 10
        )
        time.sleep(10)