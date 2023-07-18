from datetime import datetime as dt
def settimer(hour = 8, minute = 0, second = 0):
    return dt.now().replace(hour=hour, minute=minute, second=second)
