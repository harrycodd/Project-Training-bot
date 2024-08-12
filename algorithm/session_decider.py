"""
Intense = 0
Steady = 1
Rest = 2
"""

type_of_rider_lookup = {
    0: "Climber",
    1: "TT Specialist",
    2: "All-Rounder",
    3: "Sprinter"
}

class person_training:
    def __init__(self):
        self.upcoming_week_hrs = [0,1,2,1,1,1,3]
        self.last_day_type = 1
        self.type_of_rider = 0
        self.target_hours = 8
        self.calculate_i_s_days()

    def calculate_i_s_days(self):
        prev_day = self.last_day_type
        week_s_i_days = []
        for day in self.upcoming_week_hrs:
            if day == 0:
                prev_day = 2
                week_s_i_days.append(2)
            else:
                if prev_day == 2 or prev_day == 1:
                    prev_day = 0
                    week_s_i_days.append(0)
                else: 
                    prev_day = 1
                    week_s_i_days.append(1)

        self.week_si_days = week_s_i_days
        self.calculate_actual_hrs()

    def calculate_actual_hrs(self):
        average_ideal_week_hours = self.target_hours/sum([1 for x in self.upcoming_week_hrs if x > 0])
        print(average_ideal_week_hours)


person_training()