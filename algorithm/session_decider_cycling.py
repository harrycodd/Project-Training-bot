
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
    def __init__(self, ideal_hours, current_fitness, current_fatigue, current_ftp_power, current_ftp_hr, current_week_type, avaliable_days, prev_day_type=0, days_since_rest=0, day_in_week=0, current_lt1_days=0, current_lt2_days=0, current_lt3_days=0):
        self.ideal_hours = ideal_hours
        self.current_fitness = current_fitness
        self.current_fatigue = current_fatigue
        self.current_ftp_power = current_ftp_power
        self.current_ftp_hr = current_ftp_hr
        self.current_week_type = current_week_type
        self.avaliable_days = avaliable_days
        self.prev_day_type = prev_day_type
        self.days_since_rest = days_since_rest
        self.day_in_week = day_in_week
        self.current_lt1_days = current_lt1_days
        self.current_lt2_days = current_lt2_days
        self.current_lt3_days = current_lt3_days

        self.current_tsb = self.current_fitness - self.current_fatigue

        self.make_next_day_prediction()
        

    
    def make_next_day_prediction(self):
        # Establish our maximum possible training level and therefore out maximum tss per week
        self.max_ctl = round(float(50 * self.ideal_hours) / 7)
        self.max_weekly_tss = round(self.max_ctl * 7)

        # Converts ideal week hours in to number of rest days
        prev_i = 99
        for i in hours_to_rest:
            if self.ideal_hours >= i and prev_i > self.ideal_hours:
                self.ideal_rest_days = hours_to_rest[i]
                break
            prev_i = i

        # Based upon current ftp + fitness we can calculate a good estimate of the tss build for the week
        self.ideal_weekly_tss_build = ((1 - 0.00184333 + (0.0000277333 * self.current_ftp_power))**7 * self.current_fitness)

        # Our maximum tss is derived from number of hours. If we are at our maximum hours we cannot train anymore
        if self.ideal_weekly_tss_build > self.max_weekly_tss:
            self.ideal_weekly_tss_build = self.max_weekly_tss

        # Works out the number of hours based upon this weeks tss
        self.this_weeks_hours = float(round(self.ideal_weekly_tss_build / 25)) / 2

        # Creates a 0 prediction for basing it off
        baseline_hours = [-1,-1,-1,-1,-1,-1,-1]
        baseline_focus = [-1,-1,-1,-1,-1,-1,-1]

        position = 0
        for i in self.avaliable_days:
            if i == 0:
                baseline_hours[position] = 0
            position += 1
        
        if self.this_weeks_hours >= 6:
            interval_day_two_hours = float(round( (0.13 * self.this_weeks_hours + 0.25 )* 4)) /4
        else:
            interval_day_two_hours = 0

        if self.this_weeks_hours >= 8:
            recovery_day_hours = float(round( (0.05 * self.this_weeks_hours + 0.5 )* 4)) /4
        else:
            recovery_day_hours = 0

        if self.this_weeks_hours >= 10:
            interval_day_three_hours = float(round( (0.16 * self.this_weeks_hours - 0.9 )* 4)) /4
        else:
            interval_day_three_hours = 0

        interval_day_one_hours = float(round( (0.23 * self.this_weeks_hours )* 4)) /4
        endurance_day_one_hours = float(round( (0.18 * self.this_weeks_hours + 1 )* 4)) /4
        endurance_day_two_hours = float(round( (0.18 * self.this_weeks_hours + 0.25 )* 4)) /4

        self.total_lt_days = []

        prev_i = 99
        for i in hours_to_ltr_conversion:
            if self.this_weeks_hours >= i and prev_i > self.this_weeks_hours:
                self.total_lt_days = hours_to_ltr_conversion[i]
                break
            prev_i = i

        if self.total_lt_days == []:
            return False

        self.total_lt_days = [round(i * (7-self.ideal_rest_days)) for i in self.total_lt_days]

        current_no_interval_days = 0
        current_no_endurance_days = 0

        for i in range(len(baseline_hours)):
            if baseline_hours[i] == 0:
                if baseline_hours[i + 1] == -1:
                    if self.total_lt_days[0] > 0:
                        if current_no_interval_days == 0:
                            baseline_hours[i + 1] = interval_day_one_hours
                        elif current_no_interval_days == 1:
                            baseline_hours[i + 1] = interval_day_two_hours
                        else:
                            baseline_hours[i + 1] = interval_day_three_hours
                        current_no_interval_days += 1
                        baseline_focus[i] = 3
                        self.total_lt_days[0] -= 1

                    if self.total_lt_days[1] > 0:
                        if current_no_interval_days == 0:
                            baseline_hours[i + 1] = interval_day_one_hours
                        elif current_no_interval_days == 1:
                            baseline_hours[i + 1] = interval_day_two_hours
                        else:
                            baseline_hours[i + 1] = interval_day_three_hours
                        current_no_interval_days += 1
                        baseline_focus[i] = 2
                        self.total_lt_days[1] -= 1
                    
                    if self.total_lt_days[2] > 0:
                        if current_no_endurance_days == 0:
                            baseline_hours[i + 1] = endurance_day_one_hours
                        elif current_no_endurance_days == 1:
                            baseline_hours[i + 1] = endurance_day_two_hours
                        else:
                            baseline_hours[i + 1] = recovery_day_hours
                        current_no_endurance_days += 1
                        baseline_focus[i] = 1
                        self.total_lt_days[2] -= 1

            elif baseline_hours[i] == -1:
                if self.total_lt_days[2] > 0:
                    if current_no_endurance_days == 0:
                        baseline_hours[i + 1] = endurance_day_one_hours
                    elif current_no_endurance_days == 1:
                        baseline_hours[i + 1] = endurance_day_two_hours
                    else:
                        baseline_hours[i + 1] = recovery_day_hours
                    current_no_endurance_days += 1
                    baseline_focus[i] = 1
                    self.total_lt_days[2] -= 1

        print(baseline_focus, baseline_hours, self.total_lt_days)

                    


def estimate_current_fitness(hours_weekly):
    return (hours_weekly * 50) / 7 < 20

def estimate_current_ftp_hr(age):
    return (220 - age) * 0.9

def estimate_current_fatigue(current_fitness):
    return 

"""
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

user = user_cycling_predictor(ideal_hours, current_fitness, current_fatigue, current_ftp_power, current_ftp_hr, current_week_type, avaliable_days)
"""

user = user_cycling_predictor(18, 60, 60, 330, 188, 1, [0,3,3,3,1,2,2] )
