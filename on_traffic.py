import pandas as pd
import datawrappergraphics

CHART_ID = "EXyNt"

raw = pd.read_json("https://511on.ca/api/v2/get/event")

data = raw[raw["EventType"] == "closures"]
data = data[["Description", "LanesAffected", "Latitude", "Longitude"]]
data.columns = ["tooltip", "LanesAffected", "latitude", "longitude"]

data["icon"] = "roadblock"
data["scale"] = 1.2
data["type"] = "point"
data["markerColor"] = "#C42127"

roadmap = (datawrappergraphics.Map(CHART_ID)
            .data(data, append="./assets/shapes/shapes-ontarioflooding.json")
            .head(f"Northern Ontario road closures")
            .deck(f"Tap or hover over a red icon to read more about the closure.")
            .footer(source="Ontario 511", byline= False, timestamp= False)
            .publish()
            )