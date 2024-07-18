import plotly.express as px
import plotly.graph_objects as go

class totalSalesByDistributorFig:
    """
    A class to create a Plotly bar chart displaying total sales per distributor.

    Methods
    -------
    makeFig(df):
        Creates a Plotly bar chart displaying total sales per distributor.

    Attributes
    ----------
    None
    """

    def __init__(self) -> None:
        """
        Initializes an instance of the totalSalesByDistributorFig class.
        """
        pass

    def makeFig(self,df):
        """
        Creates a Plotly bar chart displaying total sales per distributor.

        Parameters
        ----------
        df : pandas.DataFrame
            DataFrame containing columns 'distributor_name' and 'total_sales'.

        Returns
        -------
        plotly.graph_objs._figure.Figure
            A Plotly figure object representing the total sales per distributor as a bar chart.
        """
        fig = px.bar(df, x='distributor_name', y='total_sales', title='Total Sales Per Distributor')
        return fig