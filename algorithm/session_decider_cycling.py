
# Conversition dictionary to polarised/hit workout distributions based upon hours training
# x hours : [lt3, lt2, lt1]
hours_to_ltr_conversion = {
    7: [0.25,0.1,0.65],
    5: [0.35, 0.1, 0.55],
    3: [0.4,0.1,0.5],
    2: [0.4,0.2,0.4],
    1: [0.6,0.2,0.2]
}

# Convertion dictionary to rest days based upon hours training
hours_to_rest = {
    10 : 1,
    7 : 2,
    5 : 3,
    3 : 4,
    2 : 5,
    1 : 6
}

hr_zones = {
    0 : 0,
    1 : 80,
    2 : 89,
    3 : 93,
    4 : 99,
    5 : 102,
    6 : 105,
    7 : 200
}

pr_zones = {
    0 : 0,
    1 : 55,
    2 : 75,
    3 : 90,
    4 : 105,
    5 : 120,
    6 : 150,
    7 : 10000
}

# Additional zones for easier and better analysis
# Sweet spot - Long threshold efforts
# Endurance - Ideal power for top end of LT1  
#   - This varies but it is the power you can hold just at the limit of breathing through your nose.
# Recovery - Ideal power for active recovery
# "ADDITIONIAL ZONE" : [lowerpr, upperpr]
ideal_zones_pr_zones = {
    "ss" : [84, 97],
    "endurance" : [55, 75],
    "recovery" : [0, 50]
}

class user_cycling_predictor:
    def __init__(self, ideal_hours, current_fitness, current_fatigue, current_ftp_power, current_ftp_hr, current_week_type, prev_day_type=0, days_since_rest=0, day_in_week=0, current_lt1_days=0, current_lt2_days=0, current_lt3_days=0):
        self.ideal_hours = ideal_hours
        self.current_fitness = current_fitness
        self.current_fatigue = current_fatigue
        self.current_ftp_power = current_ftp_power
        self.current_ftp_hr = current_ftp_hr
        self.current_week_type = current_week_type
        self.prev_day_type = prev_day_type
        self.days_since_rest = days_since_rest
        self.day_in_week = day_in_week
        self.current_lt1_days = current_lt1_days
        self.current_lt2_days = current_lt2_days
        self.current_lt3_days = current_lt3_days

        self.current_tsb = self.current_fitness - self.current_fatigue
        
    def make_next_day_prediction(self):
        pass
    


def estimate_current_fitness(hours_weekly):
    return (hours_weekly * 50) / 7 < 20

def estimate_current_ftp_hr(age):
    return (220 - age) * 0.9

def estimate_current_fatigue(current_fitness):
    return 

while True:
    new_rider = input("Are you completely new to any sort of fitness? y/n")
    if new_rider == "y":
        while True:
            ideal_hours_inputted = input("What is you ideal hours?")
            try:
                ideal_hours_rounded = float(round(float(ideal_hours) * 2)) / 2
                if ideal_hours_rounded <= 24 and ideal_hours_rounded >= 3:
                    ideal_hours = ideal_hours_rounded
                    current_fitness = 0
                    current_fatigue = 0

                    weight = input("Weight in kg?")
                    current_ftp_power = round(2 * weight)

                    age = input("Age?")
                    current_ftp_hr = round((220 - age) * 0.9)
                    break
            except:
                pass
            print("Invalid input")
        break

    elif new_rider == "n":
        break

    print("Invalid input")

user = user_cycling_predictor(ideal_hours, current_fitness, current_fatigue, current_ftp_power, current_ftp_hr, current_week_type)