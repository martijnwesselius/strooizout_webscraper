import time
import schedule
import datetime as dt

import webscraper
import mailer

def run_webscraper():
    statistics = webscraper.scrape()
    webscraper.write_to_file(statistics)
    now = dt.datetime.now().strftime('%H:%M:%S')
    print(f'Succesfully scraped at {now}')

def run_mailer():
    mailer.send_mail()
    print('Succesfully sent mail to all contacts')
    return

if __name__ == "__main__":
    print('Scheduler activated')
    schedule.every(4).hour.do(run_webscraper)
    schedule.every().day.at("8:30").do(run_mailer)

    # loops and runs the scheduled job indefinitely 
    while True:  
        schedule.run_pending()
        time.sleep(1)