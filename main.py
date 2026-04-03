import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_driver = pd.read_csv('Official Dataset 1-types of drivers.csv')
df_vehicle_wide = pd.read_csv('Official Dataset 2-type of vehicles.csv')
df_reason = pd.read_csv('in_safe_traffic.csv', keep_default_na=False)

## Data Preprocessing 

# Reshaping df_vehicle_wide
df_vehicle = df_vehicle_wide.melt(id_vars=["Type of Vehicle"], var_name="Metric", value_name="Count")
df_vehicle["Year"] = df_vehicle["Metric"].str.extract(r'(\d{4})')
df_vehicle["Crash Type"] = df_vehicle["Metric"].str.replace(r'\s\d{4}', '', regex=True)
df_vehicle = df_vehicle[["Year", "Type of Vehicle", "Crash Type", "Count"]]

# Checking null values
for c in df_driver.columns:
    print(f"{c} : {df_driver[c].isnull().sum()}")
for c in df_vehicle.columns:
    print(f"{c} : {df_vehicle[c].isnull().sum()}")
for c in df_reason.columns:
    print(f"{c} : {df_reason[c].isnull().sum()}")
# No null values found

# Checking duplicates
print(df_driver.duplicated().sum())
print(df_vehicle.duplicated().sum())
print(df_reason.duplicated().sum())
# No null values found


## Analysis of Data
df_driver

# Year vs Total Killed
df_driver['Year'] = df_driver['Year'].astype(str)

plt.figure()
plt.plot(df_driver['Year'], df_driver['Total Killed'], label='Total Killed')
# plt.plot(df_driver['Year'], df_driver['Total Injured'], label='Total Injured')
plt.xlabel("Year")
plt.ylabel("Count")
plt.title("Year vs Total Killed")
plt.legend()
plt.grid()
plt.show()

# Year vs Total Injured
plt.figure()
plt.plot(df_driver['Year'], df_driver['Total Injured'], label='Total Injured')
plt.xlabel("Year")
plt.ylabel("Count")
plt.title("Year vs Total Injured")
plt.legend()
plt.grid()
plt.show()

# Category wise Killed and Injured
categories = [
    ("Pedestrian", "Pedestrian Killed", "Pedestrian Injured"), 
    ("Cyclists", "Cyclists Killed", "Cyclists Injured"),
    ("Car", "Car Occupants Killed", "Car Occupants Injured"), 
    ('Scooter/Motorcycle Riders', 'Scooter/Motorcycle Riders Killed', 'Scooter/Motorcycle Riders Injured'),
    ('Bus Passengers', 'Bus Passengers Killed', 'Bus Passengers Injured'),
    ('Slow Moving Vehicles, Pullar and Passengers', 'Slow Moving Vehicles, Pullar and Passengers Killed', 'Slow Moving Vehicles, Pullar and Passengers Injured'),
    ('Drivers of Animal Driven Vehicles', 'Drivers of Animal Driven Vehicles Killed', 'Drivers of Animal Driven Vehicles Injured'),
    ('Other Drivers', 'Other Drivers Killed', 'Other Drivers Injured')
]

years = df_driver['Year']

for name, k_col, i_col in categories:
    killed = df_driver[k_col]
    injured = df_driver[i_col]
    total = killed + injured

    x = np.arange(len(years))

    plt.figure()
    plt.bar(x, killed, width=0.25, label="Killed")
    plt.bar(x + 0.25, injured, width=0.25, label="Injured")
    plt.bar(x + 0.50, total, width=0.25, label="Total")
    
    plt.xlabel("Year")
    plt.ylabel("Count")

    plt.xticks(x + 0.25, years)
    plt.title(f"{name}: Killed vs Injured vs Total")
    plt.legend()
    plt.show()


# Contribution of each category in the last year 
row = df_driver.iloc[-1]

values = [
    row['Pedestrian Killed'],
    row['Cyclists Killed'],
    row['Car Occupants Killed'],
    row['Scooter/Motorcycle Riders Killed'],
    row['Bus Passengers Killed'],
    row['Slow Moving Vehicles, Pullar and Passengers Killed'],
    row['Drivers of Animal Driven Vehicles Killed'],
    row['Other Drivers Killed'],
]

labels = ['Pedestrian', 'Cyclists', 'Car', 'Scooter/Motorcycle Riders', 'Bus Passengers', 'Slow Moving Vehicles, Pullar and Passengers',
        'Drivers of Animal Driven Vehicles', 'Other Drivers']

plt.figure()
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Fatality Distribution")
plt.show()


# df_vehicles

# Frequency of Various Crashes by Vehicle Type
grouped = df_vehicle.groupby(['Type of Vehicle', 'Crash Type'])['Count'].sum().reset_index()
pivot = grouped.pivot(index='Type of Vehicle', columns='Crash Type', values='Count')

pivot.plot(kind='bar', stacked=True)
plt.xlabel("Vehicle Type")
plt.ylabel("Count")
plt.title("Vehicle Type vs Crash Type")
plt.show()

# df_reason

# Main reason for accidents
counts = df_reason['safe_traffic_crash_cause_primary'].value_counts()

plt.figure()
plt.bar(counts.index, counts.values)
plt.ylabel('Count of Crashes')
plt.title("Distribution of Crash Cause")
plt.show()

# Impact of Weather on number of Crashes
counts = df_reason['safe_traffic_weather_condition_code'].value_counts()

plt.figure()
plt.bar(counts.index, counts.values)
plt.ylabel('Count of Crashes')
plt.title("Weather Condition vs Accidents")
plt.show()

# Impact of Lighting Condition on number of Crashes
counts = df_reason['safe_traffic_lighting_condition_code'].value_counts()

plt.figure()
plt.bar(counts.index, counts.values)
plt.ylabel('Count of Crashes')
plt.title("Lighting Condition vs Accidents")
plt.show()

# Frequency of SPeed on Fatalities
plt.figure()
plt.scatter(df_reason['safe_traffic_estimated_travel_speed_kmph'], df_reason['safe_traffic_fatality_count'])
plt.xlabel("Speed")
plt.ylabel("Fatalities")
plt.title("Speed vs Fatalities")
plt.show()

df_reason['safe_traffic_driver_impairment_flag'] = df_reason['safe_traffic_driver_impairment_flag'].map({
    'Y': 'Impaired',
    'N': 'Not Impaired'
})

# Driver Impairement vs Number of Crashes
counts = df_reason['safe_traffic_driver_impairment_flag'].value_counts()

plt.figure()
plt.bar(counts.index, counts.values)
plt.ylabel('Count of Crashes')
plt.title("Driver Impairment")
plt.show()

df_reason['safe_traffic_seatbelt_use_flag'] = df_reason['safe_traffic_seatbelt_use_flag'].map({
    'Y': 'Seatbelt Used',
    'N': 'Seatbelt Not Used'
})

# USage of Seatbelt vs Number of Crashes
counts = df_reason['safe_traffic_seatbelt_use_flag'].value_counts()

plt.figure()
plt.bar(counts.index, counts.values)
plt.ylabel('Count of Crashes')
plt.title("Seatbelt Usage")
plt.show()

# Post Crash Care Time Distribution
bins = [0, 30, 60, 90, 120, 150, 180, 210, np.inf]
labels = ["0-30", "30-60", "60-90", "90-120", "120-150", "150-180", "180-210", "210+"]

df_reason['care_range'] = pd.cut(
    df_reason['safe_traffic_post_crash_care_minutes'],
    bins=bins,
    labels=labels
)
counts = df_reason['care_range'].value_counts().sort_index()

plt.figure()
plt.bar(counts.index, counts.values)
plt.ylabel('Number of Crashes')
plt.xlabel('Post Crash Care Time (in minutes)')
plt.title("Post Crash Care Time (Ranges)")
plt.show()

# Frequncy of Accident by Hour of the Day
df_reason['hour'] = pd.to_datetime(
    df_reason['safe_traffic_crash_time'],
    format='%H:%M:%S'
).dt.hour
counts = df_reason['hour'].value_counts().sort_index()

plt.figure()
plt.plot(counts.index, counts.values)
plt.ylabel('Number of Crashes')
plt.xlabel('Hours (24 hour)')
plt.xticks(range(24))
plt.title("Accidents by Hour")
plt.show()
