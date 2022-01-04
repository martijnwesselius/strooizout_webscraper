import yagmail
import csv
import pandas as pd
import matplotlib.pyplot as plt


# ------------ FETCHING -----------------------------------------------------------------------------------------------

def fetch_last_observation():
    df = pd.read_csv('strooizout.csv')    
    return df.iloc[-1]

def create_plot():

    df = pd.read_csv('strooizout.csv')   
    df['time'] =  pd.to_datetime(df['time'], format='%d-%m-%Y %H:%M:%S')
    ts_diff = df.set_index('time').diff()

    x = ts_diff.index[-15:]
    y = ts_diff['seasonalSaltUsed'][-15:]
    print(x)

    fig = plt.plot(x, y)
    plt.xlabel('datum en tijd')  
    plt.ylabel('gestrooid zout (kg)')  
    plt.ylim(bottom=-1)
    plt.title('hoeveelheid strooizout afgelopen week')  
    plt.show()
    
    # fig.savefig(f'alpha_convergence_{n_states}.png')

    # return fig

create_plot()


# ------------ EMAILING -----------------------------------------------------------------------------------------------

yag = yagmail.SMTP("strooizout.python@gmail.com")

def send_mail():

    title = 'Test'
    body = '''
    Beste {name},

    Sinds gisteravond 19:00 heeft Rijkswaterstaat {daily_salt} kg zout gestrooid over een afstand van {daily_distance} km. 
    Voor het laatst is er gestrooid op {last_day}; hierbij ging het om {last_day_salt} kg over {last_day_distance} km.

    Happy motoring!

    <3 PythonBot
    '''

    observation = fetch_last_observation()

    with open("contacts.csv") as file:
        reader = csv.reader(file)
        next(reader)  # skip header row
        for name, receiver_email in reader:
            yag.send(to=receiver_email, 
                    subject=title, 
                    contents=body.format(name=name, daily_salt=observation['dailyDistance'], daily_distance=observation['dailySaltUsed'],
                                        last_day='27-12-2021', last_day_salt='25000', last_day_distance='40000'
                    ),
                    attachments=['strooizout.csv']
            )
        
