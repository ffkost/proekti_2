from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Define full moon dates and names for 2024
full_moon_info = {
    datetime(2024, 1, 25): "Wolf Moon",
    datetime(2024, 2, 24): "Snow Moon",
    datetime(2024, 3, 25): "Worm Moon",
    datetime(2024, 4, 23): "Pink Moon",
    datetime(2024, 5, 23): "Flower Moon",
    datetime(2024, 6, 21): "Strawberry Moon",
    datetime(2024, 7, 21): "Buck Moon",
    datetime(2024, 8, 19): "Sturgeon Moon",
    datetime(2024, 9, 18): "Corn Moon",
    datetime(2024, 10, 17): "Hunter's Moon",
    datetime(2024, 11, 15): "Beaver Moon",
    datetime(2024, 12, 15): "Cold Moon"
}

# Load the formatted CSV file
path = Path('Macedonia_2024_Formatted.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)  # Read the header row

# Extract dates, temperatures, sunrise, and sunset times.
dates, highs, lows = [], [], []
sunrises, sunsets = [], []
for row in reader:
    current_date = datetime.strptime(row[0], '%Y-%m-%d')  # Parse the date
    try:
        high = float(row[1])  # Parse as float for temperature
        low = float(row[2])   # Parse as float for temperature
        sunrise_time = datetime.strptime(row[3], '%Y-%m-%dT%H:%M:%S')  # Parse sunrise time
        sunset_time = datetime.strptime(row[4], '%Y-%m-%dT%H:%M:%S')    # Parse sunset time
    except ValueError:
        print(f"Missing data for {current_date}")  # Handle missing or invalid data
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        # Convert sunrise and sunset times to fractional hours
        sunrises.append(sunrise_time.hour + sunrise_time.minute / 60.0)
        sunsets.append(sunset_time.hour + sunset_time.minute / 60.0)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')  # Use a seaborn style for the plot

# Temperature Plot
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5, label='Highs')  # Plot highs
ax.plot(dates, lows, color='blue', alpha=0.5, label='Lows')  # Plot lows
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)  # Fill the area between highs and lows

# Highlight full moon dates on the temperature plot without a legend
for full_moon in full_moon_info:
    if full_moon in dates:
        idx = dates.index(full_moon)
        ax.scatter(dates[idx], highs[idx], color='purple', s=200, zorder=5)  # Purple dots for moon phases
        ax.scatter(dates[idx], lows[idx], color='purple', s=200, zorder=5)

# Format the temperature plot.
ax.set_title("Daily High and Low Temperatures, 2024\nMacedonia", fontsize=20)
ax.set_ylabel("Temperature (°C)", fontsize=16)  # Update the unit to °C
ax.legend()
fig.autofmt_xdate()
plt.gcf().autofmt_xdate(rotation=45, ha='right')  # Explicitly format date labels
plt.xticks(color='black')  # Ensure date labels are in black

# Sunrise and Sunset Plot
fig2, ax2 = plt.subplots()
ax2.plot(dates, sunrises, color='orange', alpha=0.7, label='Sunrise')  # Plot sunrise times
ax2.plot(dates, sunsets, color='purple', alpha=0.7, label='Sunset')    # Plot sunset times

# Highlight full moon dates on the sunrise/sunset plot with moon names and dates
for full_moon, moon_name in full_moon_info.items():
    if full_moon in dates:
        idx = dates.index(full_moon)
        ax2.scatter(dates[idx], sunrises[idx], color='purple', s=200, zorder=5)  # Purple dots
        ax2.scatter(dates[idx], sunsets[idx], color='purple', s=200, zorder=5)  # Purple dots
        # Annotate with the full moon name above the dot
        ax2.annotate(moon_name, (dates[idx], sunsets[idx]), textcoords="offset points",
                     xytext=(0, 10), ha='center', fontsize=10, color='black')  # Text in black
        # Annotate with the date below the dot
        ax2.annotate(full_moon.strftime('%d.%m'), (dates[idx], sunsets[idx]), textcoords="offset points",
                     xytext=(0, -15), ha='center', fontsize=8, color='black')  # Small date text below the dot

# Format the sunrise and sunset plot.
ax2.set_title("Daily Sunrise and Sunset Times, 2024\nMacedonia", fontsize=20)
ax2.set_ylabel("Time (Hours)", fontsize=16)  # Label y-axis as fractional hours
ax2.legend()  # Keep the legend only for sunrise and sunset lines
plt.gcf().autofmt_xdate(rotation=45, ha='right')  # Explicitly format date labels
plt.xticks(color='black')  # Ensure date labels are in black

# Show both plots
plt.show()
