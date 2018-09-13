''' 
-------------------------------------------------------------------------------------------------------------
|   This script is used to conduct POMODORO technique automatically                                         |
|   Author: congvm                                                                                          |
|                                                                                                           |
|   Why POMODORO?                                                                                           |
|   Click this link: https://lifehacker.com/productivity-101-a-primer-to-the-pomodoro-technique-1598992730  |
-------------------------------------------------------------------------------------------------------------
'''
print(__doc__)
import webbrowser as wb
import time
import datetime


# POMODORO CONFIGURATION
SET_WORKING_TIMER = 45 # min
SET_RELAXING_TIMER = 5 # min
FAVOURITE_MUSIC_LINK = 'https://www.youtube.com/watch?v=jXC9tuumjiA' # Canon in D


# START
print('Start Pomodoro')
curr_time = time.asctime().split()[3]
print('Now is {}'.format(curr_time))
print('You should WORK in {} minute(s) and RELAX in {} minute(s)'.format(SET_WORKING_TIMER, SET_RELAXING_TIMER))
t = datetime.datetime.now()

while True:
    # Working phase
    print('-------------------------------------------------------------------')
    t += datetime.timedelta(seconds=SET_WORKING_TIMER*60)
    working_period = str(t).split()[1].split(':')
    print('Work until {}:{}:{:02d}'.format(working_period[0], working_period[1], int(float(working_period[2])//10)))

    time.sleep(SET_WORKING_TIMER*60) # Second

    # Open link
    wb.open(FAVOURITE_MUSIC_LINK)
    print('Open {}'.format(FAVOURITE_MUSIC_LINK))
    print('Pause Working')

    # Relax phase
    print('-------------------------------------------------------------------')
    # Compute breaking time
    t += datetime.timedelta(seconds=SET_RELAXING_TIMER*60)
    relaxing_period = str(t).split()[1].split(':')
    print('Relax until {}:{}:{:02d}'.format(relaxing_period[0], relaxing_period[1], int(float(relaxing_period[2])//10)))

    time.sleep(SET_RELAXING_TIMER*60) # Second
    print('End Relaxing')

print('Stop PORODOMO')