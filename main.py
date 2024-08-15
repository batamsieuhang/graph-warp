import pandas as pd
import matplotlib.pyplot as plt
from sys import argv

# Read the data from the TSV file

file_name = argv[1]

data = pd.read_csv(file_name, delimiter='\t')

# Convert 'start' column to datetime and remove timezone info
data['start'] = pd.to_datetime(data['start']).dt.tz_localize(None)

# Convert 'duration_ns' column to numeric
data['duration_ns'] = pd.to_numeric(data['duration_ns'])

# Calculate throughput in MiB/s
data['throughput_kb_s'] = (data['bytes'] / (1024*1024)) / (data['duration_ns'] / 1e9)  # Convert ns to seconds

# Plot
plt.figure(figsize=(24, 12))
plt.plot(data['start'], data['throughput_kb_s'], marker='o', linestyle='-', color='b')
plt.xlabel('Start Time')
plt.ylabel('Throughput (KB/s)')
plt.title('PUT Operation Throughput Over Time')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('throughput_plot.png', format='png')

plt.show()
