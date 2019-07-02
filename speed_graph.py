from plotly.offline import plot
import plotly.graph_objs as go

# creating our lists to provide data to the graph
# upload speed data

up_speed = []
with open('up_speed_results.txt', 'r+') as infile:
	for line in infile:
		up_speed.append(line.strip('\n').split('|')[0])
infile.close()

# download speed data with timestamp

timestamp = []
down_speed = []
with open('down_speed_results.txt', 'r+') as infile:
	for line in infile:
		timestamp.append(line.strip('\n').split('|')[1])
		down_speed.append(line.strip('\n').split('|')[0])
infile.close()

# make the graph
# create traces

trace0 = go.Scatter(
    x = timestamp,
    y = down_speed,
    mode = 'lines',
    name = 'download speed'
)

trace1 = go.Scatter(
    x = timestamp,
    y = up_speed,
    mode = 'lines+markers',
    name = 'upload speed'
)

data = [trace0, trace1]

plot(data)