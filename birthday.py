import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Configuration
BIRTHDAY_FILE = "/home/redcroc/Desktop/birthdays.txt"

def load_birthdays():
    birthdays = []
    with open(BIRTHDAY_FILE) as f:
        for line in f:
            line = line.strip()
            if line and '\t' in line:
                name, date = line.split('\t', 1)
                birthdays.append((name.strip(), date.strip()))
    return birthdays

def check_birthdays():
    #Check who has birthday today
    today = datetime.now().strftime("%m-%d")
    birthdays_today = []
    age = datetime.now().year
    for name, date in load_birthdays():
        try:
            birth_date = datetime.strptime(date, "%Y-%m-%d")
            if birth_date.strftime("%m-%d") == today:
                birthdays_today.append(f"{name}: {age - int(birth_date.strftime("%Y"))}")
        except ValueError:
            continue
    return birthdays_today

def show_notification():
    #Show birthday notification popup
    birthdays = check_birthdays()
    if birthdays:
        root = tk.Tk()
        root.withdraw()  # Hide main window
        
        message = "Today's birthdays:\n\n" + "\n".join(birthdays)
        messagebox.showinfo("Birthday Reminder", message)
    else:
        message = "Today are NO birthdays in your list!"
        messagebox.showinfo("Birthday Reminder", message)
if __name__ == "__main__":
    show_notification()
