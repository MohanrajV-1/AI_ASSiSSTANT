import time
import datetime
import ctypes
import sys
from pydoc import safeimport

if __name__=='__main__':
    import time
    import datetime
    import ctypes,sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
if is_admin():
    current_time = datetime.datetime.now().strftime("%H:%M")
    Stop_time = input("Enter time example:-[10:10]:-")
    a = current_time.replace(":",".")
    a = float(a)
    b = Stop_time.replace(":",".")
    b = float(b)
    Focus_Time = b-a
    Focus_Time = round(Focus_Time,3)
    host_path ='C:\\Windows\\System32\\drivers\\drivers\\etc\\hosts'
    redirect = '127.0.0.1'

    print(current_time)
    time.sleep(2)
    website_list = ["wwww.facebook.com","facebook.com","www.instagram.com","instagram.com"]
    
    if (current_time < Stop_time):
        with open(host_path,"r+") as file: #r+ is writing+ reading
            content = file.read()
            time.sleep(2)
            for website in website_list:
                if website in content:
                    pass
            else:
                file.write(f"{redirect}{website}\n")
                print("DONE")
                time.sleep(1)
                print("FOCUS MODE TURNED ON !!!!")

        while True:
            current_time = datetime.datetime.now().strftime("%H:%M")
            website_list = ["www.facebook.com","facebook.com","www.instagram.com","instagram.com","youtube.com","www.youtube.com"]
            if(current_time >= Stop_time):
                with open(host_path,"r+") as file:
                    content = file.readlines()
                    file.seek(0)
                    for line in content:
                        if not any(website in line for website in website_list):
                            file.write(line)

                    file.truncate()

                print("Website are unblocked !!")
                file = open("focus.txt","a")
                file.write(f",{Focus_Time}")
                file.close()
                break

    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas",sys.executable," ".join(sys.argv), None, 1)
        
