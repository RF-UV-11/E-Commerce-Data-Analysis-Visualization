import plotly.express as px
import plotly.graph_objects as go

class totalAmountByProductCategoryFig:
    """
    A class to create a Plotly bar chart displaying total sales per product category.

    Methods
    -------
    makeFig(df):
        Creates a Plotly bar chart displaying total sales per product category.

    Attributes
    ----------
    None
    """

    def __init__(self) -> None:
        """
        Initializes an instance of the totalAmountByProductCategoryFig class.
        """
        pass

    def makeFig(self,df):
        """
        Creates a Plotly bar chart displaying total sales per product category.

        Parameters
        ----------
        df : pandas.DataFrame
            DataFrame containing columns 'category' and 'total_amount'.

        Returns
        -------
        plotly.graph_objs._figure.Figure
            A Plotly figure object representing the total sales per product category as a bar chart.
        """
        fig = px.bar(df, x='category', y='total_amount', title='Total Sales Per Product Category')
        return fig