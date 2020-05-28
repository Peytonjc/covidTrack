import requests
import csv
import plotly.io as pio
import plotly.graph_objects as go
import time
import json

state = []
infected = []
recovered = []
okDate = []
okInfected = []
nyNum = []
nyDate = []
nyInfected = []
okNum = []
txNum = []
txDate = []
txInfected = []
count = 0

covidURL = "https://covidtracking.com/api/states"
dailyURL = "https://covidtracking.com/api/states/daily"

covidInfo = requests.get(covidURL)
dailyInfo = requests.get(dailyURL)

for i in range(51):
    state.append(covidInfo.json()[i]["state"])
    infected.append(covidInfo.json()[i]["positive"])
    recovered.append(covidInfo.json()[i]["recovered"])

print(len(dailyInfo.json()))

for i in range(1 + len(dailyInfo.json())):
    j = (len(dailyInfo.json())) - 1 - i
    if dailyInfo.json()[j]["state"] == "OK":
        count += 1
        okDate.append(str(dailyInfo.json()[j]["date"])[4:6] + "/" + str(dailyInfo.json()[j]["date"])[6:8])
        print(str(dailyInfo.json()[j]["date"]))
        okInfected.append(dailyInfo.json()[j]["positive"])
        okNum.append(count)
    if dailyInfo.json()[j]["state"] == "NY":
        nyDate.append(str(dailyInfo.json()[j]["date"])[4:6] + "/" + str(dailyInfo.json()[j]["date"])[6:8])
        nyInfected.append(dailyInfo.json()[j]["positive"])
    if dailyInfo.json()[j]["state"] == "TX":
        txDate.append(str(dailyInfo.json()[j]["date"])[4:6] + "/" + str(dailyInfo.json()[j]["date"])[6:8])
        txInfected.append(dailyInfo.json()[j]["positive"])


data = dict({
    "data": [{"type": "bar",
              "name": "Infected",
              "x": state,
              "y": infected},
             {"type": "bar",
              "name": "Recovered",
              "x": state,
              "y": recovered}],
    "layout": {"title": {"text": "Covid Infections by State"}}
})

data2 = dict({
    "data": [{"type": "scatter",
              "name": "OK",
              "x": okDate,
              "y": okInfected},
             {"type": "scatter",
              "name": "NY",
              "x": nyDate,
              "y": nyInfected},
             {"type": "scatter",
              "name": "TX",
              "x": txDate,
              "y": txInfected}
             ],
    "layout": {"title": {"text": "Daily COVID Infections"}}
})

fig = go.Figure(data)
fig2 = go.Figure(data2)

fig.update_layout(barmode='stack')
fig.show()
fig2.show()
