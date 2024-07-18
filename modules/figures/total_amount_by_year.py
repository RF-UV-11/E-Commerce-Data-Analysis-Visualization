import plotly.express as px
import plotly.graph_objects as go

class totalAmountByYearFig:
    """
    A class to create a Plotly bar chart displaying total sales over time by year.

    Methods
    -------
    makeFig(df):
        Creates a Plotly bar chart displaying total sales over time by year.

    Attributes
    ----------
    None
    """

    def __init__(self) -> None:
        """
        Initializes an instance of the totalAmountByYearFig class.
        """
        pass

    def makeFig(self,df):
        """
        Creates a Plotly bar chart displaying total sales over time by year.

        Parameters
        ----------
        df : pandas.DataFrame
            DataFrame containing columns 'order_year' and 'total_amount'.

        Returns
        -------
        plotly.graph_objs._figure.Figure
            A Plotly figure object representing the total sales over time as a bar chart.
        """
        fig = px.bar(df, x='order_year', y='total_amount', title='Total Sales Over Time')
        return fig

