import pandas as pd
import plotly.express as px # type: ignore

# Load dataset (Replace with actual file path or dataset URL)
data = pd.read_csv("car_price_dataset.csv")

# Display basic information and statistics
print("Dataset Info:")
print(data.info())
print("\nDataset Summary:")
print(data.describe())

# Generate interactive visualizations
# Example: Scatter plot
fig = px.scatter(data, x="Model", y="Price", color="Transmission", title="Scatter Plot Example")
fig.show()

# Example: Bar chart
fig2 = px.bar(data, x="Model", y="Price", title="Bar Chart Example")
fig2.show()

# Example: Histogram
fig3 = px.histogram(data, x="Price", title="Histogram Example")
fig3.show()

# Example: Line chart
fig4 = px.line(data, x="Year", y="Price", title="Line Chart Example")
fig4.show()

# Save processed data to a new CSV file
data.to_csv("processed_data.csv", index=False)
print("Processed data saved to processed_data.csv")
