import geopandas as geopandas
import mapclassify as mapclassify
import pandas as pd
import geoplot as gplt
# Mac doesnt like the default TkAgg backend
import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt


def main():
    df_covid = pd.read_csv("owid-covid-data.csv")
    # Select only the columns we need
    df_covid = df_covid[['location', 'date', 'total_cases_per_million', 'iso_code']]

    # Group by most recent date for each country
    # df_covid = df_covid.sort_values('date').groupby('location').tail(1)

    # Select a certain date
    date_filter = df_covid['date'] == '2020-07-04'
    df_covid = df_covid[date_filter]

    # Get a world dataframe with mapping info
    df_world = geopandas.read_file(
        geopandas.datasets.get_path('naturalearth_lowres')
    )

    gplt.polyplot(df_world, figsize=(8, 4))

    # Add covid cases to the world df
    df_world_with_covid = df_world.merge(df_covid, left_on='iso_a3', right_on='iso_code')

    plot_world_map(df_world_with_covid)


def plot_world_map(df):
    """ Plot a world map from a data frame """

    cases_per_million = df['total_cases_per_million']
    scheme = mapclassify.Quantiles(cases_per_million, k=7)

    gplt.choropleth(df,
                    hue=cases_per_million,
                    scheme=scheme,
                    cmap='Greens',
                    legend=True,
                    figsize=(8, 4)
                    )

    plt.title("Total Confirmed COVID-19 Cases as of 07-04-2020")

    # Without this, the world map doesnt load???
    plt.show()


if __name__ == "__main__":
    main()
