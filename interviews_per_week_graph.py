import matplotlib.pyplot as plt
import numpy as np
import json



def data_file() -> str:
    return json.loads(open("settings.json", "r").read())['data_file']

weeks = np.arange(1, 40)


interviews_per_week = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i, e in enumerate(json.loads(open(data_file(), "r").read())):
    
    interviews_per_week[int(e[0])-1] = int(e[-1])

plt.figure(figsize=(10, 4))
plt.plot(weeks, interviews_per_week, marker='o', linestyle='-', color='b')

plt.xlabel("Weeks")
plt.ylabel("Number of Interviews")
plt.title("Interviews per Week")

plt.xticks(weeks)
plt.yticks(range(max(interviews_per_week)), range(max(interviews_per_week)))

for week, interviews in zip(weeks, interviews_per_week):
    plt.text(week, interviews, "", ha='center', va='bottom', fontsize=10, color='black')

plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
