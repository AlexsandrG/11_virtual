from datetime import datetime


class SuperDate(datetime):
    def get_season(self):
        month = self.month
        if month in [3, 4, 5]:
            return 'Spring'
        elif month in [6, 7, 8]:
            return 'Summer'
        elif month in [9, 10, 11]:
            return 'Autumn'
        else:
            return 'Winter'

    def get_time_of_day(self):
        hour = self.hour
        if 6 <= hour < 12:
            return 'Morning'
        elif 12 <= hour < 18:
            return 'Day'
        elif 18 <= hour < 0:
            return 'Evening'
        else:
            return 'Night'


date = SuperDate(2024, 2, 22, 12)
print(date.get_season())
print(date.get_time_of_day())