import plotly.express as px
import pandas as pd

csv = pd.read_csv("./components/info_gustos_series.csv")
df = pd.DataFrame(csv)

df2 = df.pivot_table(index = ['Genre'], aggfunc ='size').to_frame(name="Count")
print(df2)

df["GenreCount"] = df["Genre"].map(df2["Count"])

def popularity():
  fig = px.scatter(df2, y="Count", x=df2.index, color="Count", symbol="Count")
  fig.update_traces(marker_size=12)
  fig.update_layout(coloraxis_colorbar=dict(x=1.1))  
  fig.show()

fig = px.scatter(df, x="Edad", y="Genre",
	        size="GenreCount", color="Carrera",
          hover_name="Genre", log_x=True, size_max=60)
fig.show()