# GREEN API DOCS - https://green-api.com/en/docs/ 
# main website - https://console.green-api.com

import openpyxl
from rich import print
from whatsapp_api_client_python import API
from datetime import datetime, date
import time

# Initializeing global variables
names = []
dobs = []
contact = []
even = [1, 3, 5, 7, 8, 10, 12]
feb = 2
odd = [4, 6, 9, 11]
year = (date.today()).year
leap_year = True if(year%4==0 and year%100!=0 or year%400==0) else False
now = datetime.now()
current_time = now.strftime('%I:%M:%S %p')
date_and_time = f"{now.day}-{now.month}-{now.year}  {current_time}"
path = ""
green_id = ""
green_token = ""
phone_number = ""
check = []

#Getting data from file
with open("./values.txt") as f:
    data = f.readlines()
    path = data[0].strip()
    green_id, green_token = data[1].split(":")[0], data[1].split(":")[1].strip()
    phone_number = data[2].strip()

# Getting data of message already sent or not?
with open("./check.txt") as f:
    check = f.readline().strip().split(":")


def fetch_data(path):
    """
    This function fetches data from the excel sheet.
    """

    # Load the workbook
    wb = openpyxl.load_workbook(path, data_only=True)

    # Select the active worksheet
    ws = wb.active

    # Access the values of cells in the worksheet
    state = False
    for row in ws.iter_rows():
        if not state:
            state = True
            continue
        names.append(row[0].value)
        contact.append(row[1].value)
        dobs.append(row[2].value)


def today_date_month():
    """
    Function to get today's date and month for checking our text file..
    """
    d = datetime.now()
    datetime_list = str(d.date()).split("-")
    return datetime_list[2], datetime_list[1]

date1, month = tuple(map(int, today_date_month()))

def birthday_today(list):
    """
    This function check today's birthday..
    """
    date1, month = today_date_month()
    birthdayboys = []
    for index, element in enumerate(list):
        content = element.split("-")
        
        if int(content[0]) == int(date1) and int(content[1]) == int(month):
            t_birthday = names[index]
            birthdayboys.append(f"{t_birthday} - {dobs[index]}")

    return birthdayboys

def birthday_tomorrow(list):
    """
    This function check tomorrow's birthdays..
    """
    even = [1, 3, 5, 7, 8, 10, 12]
    feb = 2
    odd = [4, 6, 9, 11]
    year = (date.today()).year
    leap_year = True if(year%4==0 and year%100!=0 or year%400==0) else False

    date1, month = tuple(map(int, today_date_month()))
    birthdayboys = []

    for index, element in enumerate(list):
        content = element.split("-")
        if month == feb and date1 > 26:
            if not leap_year and date1 == 28 and int(content[0]) == 1 and int(content[1]) == month+1:
                t_birthbday = names[index]
                birthdayboys.append(f"{t_birthday} - {dobs[index]}")
                continue
            if leap_year and date1 == 29 and int(content[0]) == 1 and int(content[1]) == 3:
                t_birthbday = names[index]
                birthdayboys.append(f"{t_birthday} - {dobs[index]}")
                continue
            
        if month in even and date1 == 31:
            if int(content[0]) == 1 and int(content[1]) == (month+1 if month != 12 else 1):
                t_birthday = names[index]
                birthdayboys.append(f"{t_birthday} - {dobs[index]}")
                continue
        
        if month in odd and date1 == 30:
            if int(content[0]) == 1 and int(content[1]) == month+1:
                t_birthday = names[index]
                birthdayboys.append(f"{t_birthday} - {dobs[index]}")
                continue

        if int(content[0]) == date1 + 1 and int(content[1]) == month:
            t_birthday = names[index]
            birthdayboys.append(f"{t_birthday} - {dobs[index]}")
            continue

    return birthdayboys

def birthday_day_after_tomorrow(list):
    """
    This function check day after tomorrow's birthdays..
    """

    birthdayboys = []

    for index, element in enumerate(list):
        content = element.split("-")
        if month == feb and date1 > 26:
            if not leap_year and date1 in [27, 28]:
                if int(content[0]) == [1 if date1 == 27 else 2] and int(content[1]) == month+1:
                    t_birthbday = names[index]
                    birthdayboys.append(f"{t_birthday} - {dobs[index]}")
                    continue

            if leap_year and date1 in [28, 29]:
                if int(content[0]) == (1 if 28 else 2) and int(content[1]) == 3:
                    t_birthbday = names[index]
                    birthdayboys.append(f"{t_birthday} - {dobs[index]}")
                    continue
            
        if month in even and date1 in [30, 31]:
            if int(content[0]) == (2 if date1 == 31 else 1) and int(content[1]) == (month+1 if month != 12 else 1):
                t_birthday = names[index]
                birthdayboys.append(f"{t_birthday} - {dobs[index]}")
                continue

        if month in odd and date1 == 29:
            if int(content[0]) == (1 if date1 == 29 else 2) and int(content[1]) == month+1:
                t_birthday = names[index]
                birthdayboys.append(f"{t_birthday} - {dobs[index]}")
                continue

        if int(content[0]) == date1 + 2 and int(content[1]) == month:
            t_birthday = names[index]
            birthdayboys.append(f"{t_birthday} - {dobs[index]}")
            continue

    return birthdayboys

def send_message(number, api_key, api_id, aaj, kal, parso):
    """
    This functions send birthday updates on whatsapp to given number
    """
    
    greenAPI = API.GreenAPI(
        api_id, api_key
    )
    aaj1 = aaj if aaj != "" else ""
    kal1 = kal if kal != "" else ""
    parso1 = parso if parso != "" else ""
    message = ""
    if kal == "":
        message = f"{kal1}\n{aaj1}\n{parso1}"
    else:
        message = f"{aaj1}\n{kal1}\n{parso1}"
    
    if len(message) != 2:
        response = greenAPI.sending.sendMessage(f"{number}@c.us", f"Birthday list 🎂🎂\n{message.strip()}")
        
        # Updating status to "message sent" to True.
        res = response.code
        if res != 200:
            with open("./log.txt", "a") as f:
                f.write(f"{res}:{date_and_time}\n")
        else:
            with open("./check.txt", "w") as f:
                f.write(f"{now.day}:{now.month}:True")

    if len(message) == 2:
        with open("./check.txt", "w") as f:
                f.write(f"{now.day}:{now.month}:True")


def main():

    # checking if message is already sent today.
    if int(check[0]) != int(now.day) or int(check[1]) != int(now.month):
        fetch_data(path)
    else:
        print("Exit ho gya")
        exit()

    aaj = f"Today - {birthday_today(dobs)}" if len(birthday_today(dobs)) != 0 else ""
    kal = f"Tomorrow = {birthday_tomorrow(dobs)}" if len(birthday_tomorrow(dobs)) != 0 else ""
    parso = f"Day after tomorrow = {birthday_day_after_tomorrow(dobs)}" if len(birthday_day_after_tomorrow(dobs)) != 0 else ""
    send_message(number=phone_number, api_key=green_token, api_id=green_id, aaj=aaj, kal=kal, parso=parso)


main()