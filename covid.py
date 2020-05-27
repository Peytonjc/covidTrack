import requests
import csv
import plotly.io as pio
import time
import json

state = []
infected = []

covidURL = "https://covidtracking.com/api/states"

covidInfo = requests.get(covidURL)

for i in range(51):
    state.append(covidInfo.json()[i]["state"])
    infected.append(covidInfo.json()[i]["positive"])

fig = dict({
    "data": [{"type": "bar",
              "x": state,
              "y": infected}],
    "layout": {"title": {"text": "Covid Infections by State"}}
})

pio.show(fig)
