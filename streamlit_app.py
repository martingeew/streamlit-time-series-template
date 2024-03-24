import streamlit as st
import pandas as pd

# Function to create a label for each unique combination
def create_label(row):
    return f"{row['Direction']}, {row['Citizenship']}"

def load_data():
    df = pd.read_pickle("df_citizenship_direction_202312.pkl")
    return df


# Main title for the dashboard
st.title("New Zealand Migration Trends")

@st.cache_data  # Use Streamlit's cache to load the data only once
df = load_data()

directions = st.multiselect(
            "Select directions:",
            df["Direction"].unique(),
            default=df["Direction"].unique()[0],
        )
citizenship = st.multiselect(
    "Select Citizenship:",
    df["Citizenship"].unique(),
    default=df["Citizenship"].unique()[0],
)
filtered_df = df[
    (df["Direction"].isin(directions)) & (df["Citizenship"].isin(citizenship))
]

# Apply the function to create a new column 'Label' for plotting
filtered_df["Label"] = filtered_df.apply(create_label, axis=1)
plot_title = "Permanent and long term migration by Citizenship"

# Plotting with Plotly
fig = px.line(
    filtered_df,
    x="Month",
    y="Count",
    color="Label",
    title=plot_title,
    markers=True,
)  # Adding a horizontal line at y=0
fig.add_hline(y=0, line_dash="dash", line_color="grey")
fig.update_traces(marker=dict(size=4))
fig.update_layout(hovermode="closest")
fig.update_layout(
    legend=dict(
        orientation="h",  # Horizontal orientation
        yanchor="bottom",
        y=-0.5,  # Adjust this value to move the legend up or down relative to the bottom
        xanchor="center",
        x=0.5,  # Centers the legend horizontally
    )
)

st.plotly_chart(fig, use_container_width=True)
