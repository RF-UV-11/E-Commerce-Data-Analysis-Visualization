import plotly.express as px
import plotly.graph_objects as go

class averagePriceRateByCountryFig:
    """
    A class to create a choropleth map using Plotly Express, visualizing average product prices by country.

    Methods
    -------
    makeFig(df):
        Creates a choropleth map based on the provided DataFrame.

    Attributes
    ----------
    None
    """

    def __init__(self) -> None:
        """
        Initializes an instance of the averagePriceRateByCountryFig class.
        """
        pass

    def makeFig(self,df):
        """
        Creates a choropleth map using Plotly Express based on the provided DataFrame.

        Parameters
        ----------
        df : pandas.DataFrame
            DataFrame containing country names ('country'), and average prices ('avg_price').

        Returns
        -------
        plotly.graph_objs._figure.Figure
            A Plotly figure object representing the choropleth map of average product prices by country.
        """
        # Create a choropleth map using Plotly
        fig = px.choropleth(df, 
                            locations='country', 
                            locationmode='country names',
                            color='avg_price',
                            hover_name='country',
                            title='Average Product Prices by Country',
                            color_continuous_scale=px.colors.sequential.Plasma)

        return fig