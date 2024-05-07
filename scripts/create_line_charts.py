import pandas as pd
import matplotlib.pyplot as plt

# Read the table CSV file
table_df = pd.read_csv("logs/perplexity_table.csv")

# Extract data for each model
baseline_ppl = table_df["Baseline"]
prenorm_ppl = table_df["Prenorm"]
postnorm_ppl = table_df["Postnorm"]
validation_ppl = table_df["Validation ppl"]

# Define colors for each model
baseline_color = "red"
prenorm_color = "green"
postnorm_color = "blue"

# Create line charts with distinct colors
plt.figure(figsize=(10, 6))

plt.plot(validation_ppl, baseline_ppl, label="Baseline", color=baseline_color, marker='o')
plt.plot(validation_ppl, prenorm_ppl, label="Prenorm", color=prenorm_color, marker='o')
plt.plot(validation_ppl, postnorm_ppl, label="Postnorm", color=postnorm_color, marker='o')

plt.title("Validation Perplexities")
plt.xlabel("Validation Steps")
plt.ylabel("Perplexity")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the line chart as an image
plt.savefig("logs/line_chart.png")

# Show the line chart
plt.show()