class AlarmClock:
    def __init__(self, current_time, alarm_time):
        self.current_time = current_time
        self.alarm_on = False
        self.alarm_time = alarm_time
    #Method 1
    def change_time(self):
        self.current_time  = input("Please set a new time: \n")
        print(f"The current time is no {self.current_time}")
    #Method 2
    def toggle_alarm(self):
        self.alarm_on = not self.alarm_on
    #Method 3
    def change_alarm_time(self):
        self.alarm_time = input("Please set a new alarm time: \n")
        print(f"The alarm is now changed to {self.alarm_time}")




        