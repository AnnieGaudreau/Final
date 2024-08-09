import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#import data
url = 'https://storage.googleapis.com/scsu-data-science/bike_sharing.csv'
df = pd.read_csv(url)

#show raw data
st.write('### Raw Data')
st.write(data.head())

#Part 1: line plot
st.write('##Total Ridership Over Time')
data['dteday'] = pd.to_datetime(data['dteday'])

fig, ax = plt.subplots()
ax.plot(data['dteday'], data['cnt'])
ax.set_title('Total Ridership Over Time')
ax.set_xlabel('Date')
ax.set_ylabel('Total Ridership')
st.pyplot(fig)

#Part 2: bar plot
st.write('## Total Ridership by Season')
season_counts = data.groupby('season')['cnt'].sum()

fig, ax = plt.subplots()
ax.bar(season_counts.index, season_counts.values)
ax.set_title('Total Ridership by Season')
ax.set_xlabel('Season')
ax.set_ylabel('Total Ridership')
ax.set_xticks([1,2,3,4])
ax.set_xticklabels(['Winter', 'Spring', 'Summer', 'Fall'])
st.pyplot(fig)

#Part 3: line plot, rolling avg
st.write('## Total Ridership Over Time (Rolling Average)')

#radio for selecting interval
rolling_interval = st.radio('Select Rolling Average Interval', [7, 14])

#calculate rolling avg
data[f'rolling_{rolling_interval}'] = data['cnt'].rolling(interval=rolling_interval).mean

fig, ax = plt.subplots()
ax.plot(data['dteday'], data[f'rolling_{rolling_interval}'])
ax.set_title(f'Total Ridership Over Time (Rolling Average: {rolling_interval} Days)')
ax.set_xlabel('Date')
ax.set_ylabel('Total Ridership')
st.pyplot(fig)
