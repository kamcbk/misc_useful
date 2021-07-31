#Author: Kevin Marroquin
import time
from threading import Timer
from datetime import datetime
from pytz import timezone

#####README#######
#This script uses unix time to set a time on when to run a function, i.e. a timer. 
#For convenience, conversions from PST to unix and vice versa are included. Your 
#console will continue running until the time set to run is up, where it will
#then run the function

#Instructions: Have a time (in PST) you want to run a function. Convert it to Unix
#time. Plug in the time to set_timer along with the function you want to run. Add
#additional arguments as needed.

#This code originally came out of collecting astronomical data at 3am (Measuring
#the Moon and the Sun). I got tired of waking up early so I searched and wrote a
#timer function. Seeing how running programs late at night (or for extended 
#periods of time) is somehow becoming more of a common thing for me, I decided to 
#make an actual script that makes this process more formal.
#####README#######



###PST to Unix
def PST_to_unix(yr, mon, day, hr = 0, minute = 0,sec = 0):
    '''
    Convert PST to unix. Input time according to variables. Time will be produced
    based on your computer's internal clock settings; this function assumes your
    computer's clock is set to PST.
    
    return: time in unix time
    '''
    return int(time.mktime(time.strptime(
        str(yr) +'-'+str(mon)+'-'+str(day)+' '+str(hr)+':'+str(minute)+':'+str(sec), 
        '%Y-%m-%d %H:%M:%S')))

###Unix to PST
def unix_to_PST(uni, fmt = '%Y-%m-%d %H:%M:%S %Z%z'):
    '''
    Converts unix time to PST
    
    uni: integer, unix time
    fmt: str, format you would like to display your results (see datetime documentation
    for details)
    
    return: time in PST.
    '''
    return datetime.fromtimestamp(uni).astimezone(
        timezone('US/Pacific')).strftime(fmt)


def set_timer(unix_t, func, *args):
    '''
    Set a time to run a function 
    
    NOTE: PLEASE READ THE ARGS LINE A COUPLE OF LINES BELOW. Inputting
    arguments into your function has unusual syntax.
    
    Arguments:
        unix_t: float, unix time when you want function to run
        func: func, function you want to run at unix_t
        args: tuple, arguments for your function. Must have a comma
        after your last argument
    
    
    Example1:
    set_timer(time.time() + 1, sum, (np.arange(4),) )
    returns 6
    
    set_timer(time.time() + 2, lambda x,y: 7 + x, (6,'maybe?',))
    returns 13
    
     
    Prints returned value in your function arguments. Also runs anything
    inside your function like np.save or additional print statements inside
    your function.
    
    If you would like to run a series of commands, a way around the func
    argument is to create an entirely new func that takes in no arguments
    but runs everything in your commmand.
    
    Example2:
    
    def tester():
        print('This is a test')
        return sum(np.arange(10))
    set_timer(time.time() + 2, tester)
    
    Output:
    This is a test
    45
    
    If you accidently made unix_t < time.time(), use variable.is_alive() 
    to see if Timer is still running and variable.cancel to cancel the Timer
    
    Returns:
        Your function call after a certain time (hopefully)
    '''

    current_time = time.time()
    sec_till = unix_t - current_time
    variable = CustomTimer(sec_till, func, *args)
    variable.start()
    print(variable.join())

    
    
class CustomTimer(Timer):
    '''
    Creates a custom Timer from the threading package. Works the same way as Timer
    but has an additional join function
    
    '''
    def __init__(self, interval, function, args=[], kwargs={}):
        self._original_function = function
        super(CustomTimer, self).__init__(
            interval, self._do_execute, args, kwargs)

    def _do_execute(self, *a, **kw):
        self.result = self._original_function(*a, **kw)

    def join(self):
        super(CustomTimer, self).join()
        return self.result


#Examples
import numpy as np

def tester():
    print('This is a test')
    return sum(np.arange(10))

set_timer(time.time() + 10, tester) #Wait 10 seconds 

def average_test(n):
	'''
	Average of an array of consecutive values with length n
	'''
	return np.mean(np.arange(n))

set_timer(time.time() + 5, average_test, (4,)) #Wait 5 seconds
