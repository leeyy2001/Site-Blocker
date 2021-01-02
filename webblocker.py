import time
from datetime import datetime as dt

hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

website_list = ["abc.com"]

start_time = input("What time do you want the blocking to start?")
end_time = input("What time do want the blocking to end?")

start_hours = (int(start_time[0]) * 10) + int(start_time[1])
start_minutes = (int(start_time[2]) * 10) + int(start_time[3])
end_hours = (int(end_time[0]) * 10) + int(end_time[1])
end_minutes = (int(end_time[2]) * 10) + int(end_time[3])

#sets the date and time start and end of the blocking program.
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, hour=start_hours, minute=start_minutes) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, hour=end_hours, minute=end_minutes):
        print("Sorry access to the website is not allowed at this time.")
        with open(hostsPath, "r+") as file:
            content = file.read()
            #If the hosts file contains the website alr then nothing happens. If put the website into the hosts file
            for site in website_list:
                if site in content:
                    pass
                else:
                    #mapping website to your localhost IP address
                    file.write(redirect + " " + site + "\n")

    else:
        with open(hostsPath, "r+") as file:
            content = file.readlines()
            #starts reading the file from the very first letter and not from anywhere else in the file
            file.seek(0)
            for line in content:
                #this ensures that any website in the website_list is in the hosts file. If it isn't then it adds the file
                if not any(website in line for website in website_list):
                    file.write(line)
            #basically removes the website from the hosts file, since it i  s no longer within the time given    
            file.truncate()

        print("Access to the websites are now granted")
        break
    time.sleep(60)

    
