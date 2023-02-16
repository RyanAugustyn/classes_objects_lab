from alarm_clock import AlarmClock
from person import Person


clock = AlarmClock("12:00 PM", "7:00 PM")
clock.change_alarm_time()

person1 = Person("Peter", 100)
person2 = Person("Paul", 5000)

person1.remove_money(100)
person2.add_money(100, "Peter")
