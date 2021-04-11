import datetime
# from datetime import datetime
import time

class EpochTime():
    def __init__(self,
                 t=None,
                 unit=None,
                 human_date=True,
                 divide_by=None
                 ) -> None:
        self.t = t
        self.raw_time = t or time.time()
        self.nearest_minute = self.set_minute()
        self.nearest_second = self.set_second()
        if human_date:
            self.human_date = self.convert_to_human_text(time=self.raw_time, unit=unit)
        if divide_by:
            self.raw_time_divided = self.raw_time / divide_by

    def divide_by(self, quotient=None, number=None):
        return quotient / number

    def convert_to_human_text(self, time=None, unit=None):
        if unit == 'milliseconds_since_epoch':
            date = datetime.fromtimestamp(time / 1e3)
        else:
            date = datetime.fromtimestamp(time)
        return date.strftime('%Y-%m-%d %H:%M:%S.%f')

    def set_second(self):
        '''
        return the second of the milliseconds passed
        '''
        return self.t / 10000

    def set_minute(self):
        '''
        return the minute of the milliseconds passed
        '''
        return self.t / 60000

    def __str__(self) -> str:
        return str(self.__dict__)


# print(EpochTime(t=1605679892756, unit='milliseconds_since_epoch', divide_by=1000))
# newtime = EpochTime(t=1605679892756, unit='milliseconds_since_epoch', divide_by=1000)
# print(newtime.nearest_second)
# print(newtime.nearest_minute)

def round_time(dt=None, date_delta=datetime.timedelta(minutes=1), to='average'):
    """
    Round a datetime object to a multiple of a timedelta
    dt : datetime.datetime object, default now.
    dateDelta : timedelta object, we round to a multiple of this, default 1 minute.
    from:  http://stackoverflow.com/questions/3463930/how-to-round-the-minute-of-a-datetime-object-python
    """
    round_to = date_delta.total_seconds()
    # print("round_to: " + str(round_to))
    if dt is None:
        dt = datetime.now()
    seconds = (dt - dt.min).seconds
    # print("seconds: " + str(seconds))

    # print("if: seconds _percent_ round_to == 0" + str(seconds % round_to))
    # print("if: dt.microseconds == 0: " + str(dt.microsecond))
    if seconds % round_to == 0 and dt.microsecond == 0:
        rounding = (seconds + round_to / 2) // round_to * round_to
    else:
        if to == 'up':
            # // is a floor division, not a comment on following line (like in javascript):
            rounding = (seconds + dt.microsecond/1000000 + round_to) // round_to * round_to
        elif to == 'down':
            rounding = seconds // round_to * round_to
        else:
            rounding = (seconds + round_to / 2) // round_to * round_to

    return dt + datetime.timedelta(0, rounding - seconds, - dt.microsecond)

s0 = 1614218399298
s1 = 1614218399298 / 1000.0
s2 = 1612918857568 / 1000.0

t_utc = datetime.datetime.utcfromtimestamp(float(s0)/1000.)
print(t_utc.strftime("%Y-%m-%d %H:%M:%S.%f"))

print(time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(s0/1000.)))
s0tot0 = time.gmtime(s0/1000.0)
datetime_t0 = datetime.datetime
print(str(datetime.timedelta(minutes=1)))
print("time1: " + str(datetime.datetime.fromtimestamp(s1)))
print("time2: " + str(datetime.datetime.fromtimestamp(s2)))
print("s1 time is: " + datetime.datetime.fromtimestamp(s1).strftime('%Y-%m-%d %H:%M:%S.%f'))
# test data
print("s2 time is: " + datetime.datetime.fromtimestamp(s2).strftime('%Y-%m-%d %H:%M:%S.%f'))
round_time(datetime.datetime.fromtimestamp(s2), date_delta=datetime.timedelta(minutes=1), to='down')
print(round_time(datetime.datetime.fromtimestamp(s1), date_delta=datetime.timedelta(minutes=1), to='down'))
print(round_time(datetime.datetime(2019,11,2,14,39,00,1), date_delta=datetime.timedelta(seconds=60), to='down'))
# print(round_time(datetime.datetime(2019,11,3,14,39,00,776980), date_delta=datetime.timedelta(seconds=30), to='up'))
print(round_time(datetime.datetime(2019,11,4,14,39,29,776980), date_delta=datetime.timedelta(seconds=60), to='down'))
print(round_time(datetime.datetime(2019,11,4,14,39,55,776980), date_delta=datetime.timedelta(seconds=60), to='down'))
print(round_time(datetime.datetime(2018,11,5,14,39,00,776980), date_delta=datetime.timedelta(seconds=30), to='down'))
print(round_time(datetime.datetime(2018,11,6,14,38,59,776980), date_delta=datetime.timedelta(seconds=30), to='down'))
print(round_time(datetime.datetime(2017,11,7,14,39,15), date_delta=datetime.timedelta(seconds=30), to='average'))
print(round_time(datetime.datetime(2017,11,8,14,39,14,999999), date_delta=datetime.timedelta(seconds=30), to='average'))
print(round_time(datetime.datetime(2019,11,9,14,39,14,999999), date_delta=datetime.timedelta(seconds=30), to='up'))
print(round_time(datetime.datetime(2012,12,10,23,44,59,7769),to='average'))
print(round_time(datetime.datetime(2012,12,11,23,44,59,7769),to='up'))
print(round_time(datetime.datetime(2010,12,12,23,44,59,7769),to='down',date_delta=datetime.timedelta(seconds=1)))
print(round_time(datetime.datetime(2011,12,13,23,44,59,7769),to='up',date_delta=datetime.timedelta(seconds=1)))
print(round_time(datetime.datetime(2012,12,14,23,44,59),date_delta=datetime.timedelta(hours=1),to='down'))
print(round_time(datetime.datetime(2012,12,15,23,44,59),date_delta=datetime.timedelta(hours=1),to='up'))
print(round_time(datetime.datetime(2012,12,16,23,44,59),date_delta=datetime.timedelta(hours=1)))
print(round_time(datetime.datetime(2012,12,17,23,00,00),date_delta=datetime.timedelta(hours=1),to='down'))
print(round_time(datetime.datetime(2012,12,18,23,00,00),date_delta=datetime.timedelta(hours=1),to='up'))
print(round_time(datetime.datetime(2012,12,19,23,00,00),date_delta=datetime.timedelta(hours=1)))
