import pandas as pd
import plotly.express as px

# Reading queries clicks data from the CSV file
df = pd.read_csv('./downloaded_data.csv')

# Manipulating the clicks data
df.sort_values(by='Url Clicks', ascending=False, inplace=True)
df['Cumulative clicks'] = df[['Url Clicks']].cumsum()
df['Cumulative clicks percentage'] = df['Cumulative clicks'] / df['Url Clicks'].sum()

df.reset_index(drop=True, inplace=True)

# First fig
fig1 = px.ecdf(df, x="Cumulative clicks", ecdfnorm=None,
               title=f"1. Cumulative clicks distribution ({df.index.values[-1]} queries)",
               width=600, height=600, hover_data=["Cumulative clicks percentage"])
fig1.update_yaxes(title_text="Num of queries ('count' on hover)")
fig1.show()

# Second fig
# "hover_data_1" on hover refers to "Num of queries"
fig2 = px.ecdf(df, x="Cumulative clicks percentage", ecdfmode="standard",
               title=f"2. Cumulative clicks percentage distribution ({df.index.values[-1]} queries)",
               width=600, height=600, hover_data=["Cumulative clicks", df.index.values])
fig2.update_xaxes(tickformat=".0%")
fig2.update_yaxes(
    title_text="Percentage of queries ('probability' on hover)", tickformat=".0%")
fig2.show()
