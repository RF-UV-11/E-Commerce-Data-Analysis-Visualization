import plotly.express as px
import plotly.graph_objects as go

class distributorCountByCountryFig:
    """
    A class to create a choropleth map representing the number of distributors by country using Plotly Express.

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
        Initializes an instance of the distributorCountByCountryFig class.
        """
        pass

    def makeFig(self,df):
        """
        Creates a choropleth map representing the number of distributors by country using Plotly Express.

        Parameters
        ----------
        df : pandas.DataFrame
            DataFrame containing columns 'country' and 'distributor_count' for each country.

        Returns
        -------
        plotly.graph_objs._figure.Figure
            A Plotly figure object representing the choropleth map of distributor counts by country.
        """
        fig = px.choropleth(df, locations='country', locationmode='country names', color='distributor_count', hover_name='country', color_continuous_scale='viridis')
        fig.update_layout(title='Number of Distributors by Country')
        return fig

