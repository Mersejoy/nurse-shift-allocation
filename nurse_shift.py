import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# Parameters
nurses = 60
departments = ["ICU-V", "ICU-NV", "General", "OPD", "Casualty"]
shifts = ["Morning", "Evening", "Night"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Department Details
patient_data = {
    "ICU-V": {"patients": 5, "ratio": 1, "rooms": 1},
    "ICU-NV": {"patients": 15, "ratio": 3, "rooms": 1},
    "General": {"patients": 40, "ratio": 6, "rooms": 2},
    "OPD": {"patients": 90, "ratio": 100, "rooms": 1},
    "Casualty": {"patients": 30, "ratio": 4, "rooms": 1},
}

# Nurse Data
random.seed(42)
nurse_ids = [f"Nurse {i}" for i in range(1, nurses + 1)]
ONWS_scores = {nurse: round(random.uniform(0, 1), 2) for nurse in nurse_ids}
weekly_offs = {nurse: random.sample(days, random.randint(1, 4)) for nurse in nurse_ids}

# Ensure only 2 nurses are on long vacation at a time
long_vacation_nurses = random.sample(nurse_ids, 2)
for nurse in long_vacation_nurses:
    weekly_offs[nurse] = days[:4]

# Calculate Loading Factors
loading_factors = {dept: int(np.ceil(data["patients"] / data["ratio"]) * data["rooms"])
                   for dept, data in patient_data.items()}

# Generate Roster
roster = {day: {nurse: "" for nurse in nurse_ids} for day in days}

for day in days:
    for dept, lf in loading_factors.items():
        for shift in shifts:
            allocated = 0
            available_nurses = [n for n in nurse_ids if day not in weekly_offs[n]]
            random.shuffle(available_nurses)
            for nurse in available_nurses:
                if allocated < lf and roster[day][nurse] == "":
                    roster[day][nurse] = f"{dept} ({shift})"
                    allocated += 1

# Convert Roster to DataFrame and Save
roster_df = pd.DataFrame(roster)
roster_df.index = nurse_ids
roster_df.to_csv("nurse_shift_roster.csv")

# Generate and Save Chart
plt.figure(figsize=(10, 6))
plt.bar(loading_factors.keys(), loading_factors.values(), color='skyblue')
plt.xlabel("Departments")
plt.ylabel("Nurses Required")
plt.title("Loading Factor (LF) Distribution Across Departments")
plt.xticks(rotation=45)
plt.savefig("workload_distribution.png")
plt.show()
