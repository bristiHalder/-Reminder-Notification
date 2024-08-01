import time #needed for time delay
from plyer import notification

if __name__ == "__main__":  
    while True:
        notification.notify(
            title="** Take Rest ** ",
            message= " This is a remainder",
            timeout= 5  #duration of notification
        )
        time.sleep(10) #after 10s notification will generate