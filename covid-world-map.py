# Mac doesnt like the default TkAgg backend

import geopandas as geopandas
import mapclassify as mapclassify
import pandas as pd
import geoplot


def main():
    df_covid = pd.read_csv("owid-covid-data.csv")
    # Select only the columns we need
    df_covid = df_covid[['location', 'date', 'total_cases_per_million']]

    # Group by most recent date for each country
    df_covid = df_covid.sort_values('date').groupby('location').tail(1)

    # Get a world dataframe with mapping info
    df_world = geopandas.read_file(
        geopandas.datasets.get_path('naturalearth_lowres')
    )
    geoplot.polyplot(df_world, figsize=(8, 4))

    # Add covid cases to the world df
    df_world_with_covid = df_world.merge(df_covid, left_on='name', right_on='location')

    plot_world_map(df_world_with_covid)


def plot_world_map(df):
    """ Plot a world map from a data frame """

    cases_per_million = df['total_cases_per_million']
    scheme = mapclassify.Quantiles(cases_per_million, k=7)

    geoplot.choropleth(df,
                       hue=cases_per_million,
                       scheme=scheme,
                       cmap='Greens',
                       figsize=(8, 4)
                       )


if __name__ == "__main__":
    main()
