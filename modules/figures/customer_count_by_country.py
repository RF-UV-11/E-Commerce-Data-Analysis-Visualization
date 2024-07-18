import plotly.express as px
import plotly.graph_objects as go

class customerCountByCountryFig:
    """
    A class to create a choropleth map using Plotly Express, visualizing the number of customers by country.

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
        Initializes an instance of the customerCountByCountryFig class.
        """
        pass

    def makeFig(self,df):
        """
        Creates a choropleth map using Plotly Express based on the provided DataFrame.

        Parameters
        ----------
        df : pandas.DataFrame
            DataFrame containing country names ('country'), and customer counts ('customer_count').

        Returns
        -------
        plotly.graph_objs._figure.Figure
            A Plotly figure object representing the choropleth map of number of customers by country.
        """
        fig = px.choropleth(df, locations='country', locationmode='country names', color='customer_count', hover_name='country', color_continuous_scale='viridis')
        fig.update_layout(title='Number of Customers by Country')
        return fig