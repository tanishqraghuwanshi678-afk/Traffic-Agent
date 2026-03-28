import pandas as pd


# Simulated traffic data
data = pd.DataFrame({
    'time': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
    'vehicles': [120, 200, 250, 300, 280, 260, 270, 290, 320, 350, 400, 420, 380, 300, 200]
})

# Initial signal timing (seconds)
green_time = 30

# Learning memory
history = []


def adjust_signal(vehicles, current_time):
    global green_time

    # Decision making
    if vehicles > 300:
        green_time += 10
        traffic = "HIGH"
    elif vehicles < 200:
        green_time -= 5
        traffic = "LOW"
    else:
        traffic = "MEDIUM"

    # Limit signal time
    green_time = max(20, min(green_time, 90))

    # 🎯 REWARD SYSTEM (ADD HERE)
    if traffic == "HIGH" and green_time >= 40:
        reward = +2  # good decision
    elif traffic == "LOW" and green_time <= 30:
        reward = +2  # good decision
    else:
        reward = -1  # bad decision

    # Store learning
    history.append((current_time, vehicles, green_time, traffic, reward))

    return green_time, traffic, reward

# Simulation
for i in range(len(data)):
    time = data['time'][i]
    vehicles = data['vehicles'][i]

    new_time, traffic, reward = adjust_signal(vehicles, time)

    print(f"Time: {time}:00 | Vehicles: {vehicles} | Traffic: {traffic} | Signal: {new_time}s | Reward: {reward}")

# Analysis
print("\n--- Traffic Analysis ---")

high = [h for h in history if h[3] == "HIGH"]
low = [h for h in history if h[3] == "LOW"]

print("Peak Traffic Times:", [h[0] for h in high])
print("Low Traffic Times:", [h[0] for h in low])

# Total reward
total_reward = sum([h[4] for h in history])
print("Total Reward:", total_reward)
import matplotlib.pyplot as plt

times = [h[0] for h in history]
signals = [h[2] for h in history]

plt.plot(times, signals)
plt.title("Signal Timing Adaptation")
plt.xlabel("Time")
plt.ylabel("Green Signal Time")
plt.show()
