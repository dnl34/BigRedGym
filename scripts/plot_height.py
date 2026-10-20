import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("height_tracking.csv")

plt.figure(figsize=(10, 5))

plt.plot(data["time_s"], data["commanded_height_m"],
         label="Commanded Height", linewidth=2)

plt.plot(data["time_s"], data["actual_height_m"],
         label="Actual Height", linewidth=1.5)

plt.xlabel("Time (s)")
plt.ylabel("Body Height (m)")
plt.title("Go2 Robot Height Tracking")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("height_tracking_plot.pdf")
plt.show()