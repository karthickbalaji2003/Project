import random
import time
import datetime

# Simulate sensor readings (REPLACE with actual sensor integration)
def get_flow_rate(location):
    base_flow = 100
    variation = random.uniform(-10, 10)
    flow = base_flow + variation

    if random.random() < 0.05:  # Simulate events (for demonstration)
        event_type = random.choice(["leak", "unauthorized_connection", "siphoning"])
        if event_type == "leak":
            flow += random.uniform(20, 50)
        elif event_type == "unauthorized_connection":
            flow += random.uniform(15, 30)
        elif event_type == "siphoning":
            flow -= random.uniform(10, 25)

    return flow

def get_pressure(location):
    base_pressure = 50
    variation = random.uniform(-5, 5)
    pressure = base_pressure + variation

    if location == "tail_end":
        pressure -= random.uniform(5, 15)

    return pressure

# Basic anomaly detection (IMPROVE with ML)
def detect_anomaly(flow_rate, pressure, location):
    if flow_rate > 150:
        print(f"Possible leak/unauthorized connection at {location}: Flow = {flow_rate}")
    elif flow_rate < 80:
        print(f"Possible siphoning at {location}: Flow = {flow_rate}")
    elif location == "tail_end" and pressure < 35:
        print(f"Low pressure at tail end: Pressure = {pressure}")

# Main monitoring loop
locations = ["main_pipeline_1", "main_pipeline_2", "tail_end"]
while True:
    for location in locations:
        flow = get_flow_rate(location)
        pressure = get_pressure(location)
        print(f"Time: {datetime.datetime.now()}, Loc: {location}, Flow: {flow:.2f}, Pressure: {pressure:.2f}")
        detect_anomaly(flow, pressure, location)

    time.sleep(5)  # Check every 5 seconds
