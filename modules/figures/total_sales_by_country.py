import plotly.express as px
import plotly.graph_objects as go

class totalSalesByCountryFig:
    """
    A class to create a Plotly choropleth map displaying total sales amount by country.

    Methods
    -------
    makeFig(df):
        Creates a Plotly choropleth map displaying total sales amount by country.

    Attributes
    ----------
    None
    """

    def __init__(self) -> None:
        """
        Initializes an instance of the totalSalesByCountryFig class.
        """
        pass

    def makeFig(self,df):
        """
        Creates a Plotly choropleth map displaying total sales amount by country.

        Parameters
        ----------
        df : pandas.DataFrame
            DataFrame containing columns 'country' and 'total_sales_amount'.

        Returns
        -------
        plotly.graph_objs._figure.Figure
            A Plotly figure object representing the total sales amount by country as a choropleth map.
        """
        fig = px.choropleth(df, locations='country', locationmode='country names', color='total_sales_amount', hover_name='country', color_continuous_scale='viridis')
        fig.update_layout(title='Total Sales Amount by Country')
        return fig

