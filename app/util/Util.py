from datetime import datetime

class Util:

    @staticmethod
    def get_datetime_string(datetime: datetime):
        year = "{}".format(datetime.year)
        month = "{}".format(datetime.month).zfill(2)
        day = "{}".format(datetime.day).zfill(2)
        hour = "{}".format(datetime.hour).zfill(2)
        minite = "{}".format(datetime.minute).zfill(2)
        sec = "{}".format(datetime.second).zfill(2)

        return "{}{}{}{}{}{}".format(year, month, day, hour, minite, sec)