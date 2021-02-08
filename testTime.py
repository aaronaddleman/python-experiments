from datetime import datetime
import time

class EpochTime():
    def __init__(self, t=None,
                 unit=None,
                 human_date=True,
                 divide_by=None
                 ) -> None:
        self.raw_time = t or time.time()
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

    def __str__(self) -> str:
        return str(self.__dict__)

print(EpochTime(t=1605679892756, unit='milliseconds_since_epoch', divide_by=1000))
