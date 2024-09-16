
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

class user_week_predictor:
    def __init__(self, ideal_hours, current_fitness, current_fatigue, current_ftp_power, current_ftp_hr, current_week_type):
        # Set current levels 
        self.ideal_hours = ideal_hours
        self.current_fitness = current_fitness
        self.current_fatigue = current_fatigue
        self.current_ftp_power = current_ftp_power
        self.current_ftp_hr = current_ftp_hr
        self.current_week_type = current_week_type

        self.current_tsb = self.current_fitness - self.current_fatigue
        
    

user = user_data

def estimate_current_fitness(hours_weekly):
    return (hours_weekly * 50) / 7 < 20

def estimate_current_ftp_hr(age):
    # (220 - age) * 0.9 - to workout estimated ftp
    pass

def estimate_current_fatigue():
    # Same as current fitness
    pass

self.estimate_current_fitness(hours_weekly)