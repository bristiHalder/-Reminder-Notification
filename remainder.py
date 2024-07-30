import time
from plyer import notification
import threading

# Dictionary to store reminders
reminders = {}

def display_menu():
    print("\nReminder Application Menu:")
    print("1. Add a New Reminder")
    print("2. View All Reminders")
    print("3. Exit")

def add_reminder():
    reminder_time = input("Enter the time for the reminder (in HH:MM format): ")
    reminder_message = input("Enter the reminder message: ")
    reminders[reminder_time] = reminder_message
    print(f"Reminder set for {reminder_time}.")

def view_reminders():
    if reminders:
        print("\nReminders:")
        for time, message in reminders.items():
            print(f"Time: {time}, Message: {message}")
    else:
        print("No reminders set.")

def send_notification(message):
    notification.notify(
        title='Reminder',
        message=message,
        timeout=10
    )

def check_reminders():
    while True:
        current_time = time.strftime("%H:%M")
        if current_time in reminders:
            send_notification(reminders[current_time])
            del reminders[current_time]
        time.sleep(60)  # Check every minute

def main():
    reminder_thread = threading.Thread(target=check_reminders)
    reminder_thread.daemon = True
    reminder_thread.start()

    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_reminder()
        elif choice == '2':
            view_reminders()
        elif choice == '3':
            print("Exiting the Reminder Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
