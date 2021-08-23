import time
import csv

def log_it(id,message):
    
    with open('/home/pi/Desktop/mail_logs.txt', 'w') as f:
        writer = csv.writer()
        log_line = f"{time.ctime} - {id} {message}".format()
        writer.writerow(log_line)
        f.close()