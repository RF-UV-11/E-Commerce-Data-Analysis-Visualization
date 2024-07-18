import plotly.express as px
import plotly.graph_objects as go

class customerRegistrationByCountryFig:
    """
    A class to create a bar chart using Plotly Graph Objects, visualizing customer registration by year and country.

    Methods
    -------
    makeFig(df):
        Creates a bar chart based on the provided DataFrame.

    Attributes
    ----------
    None
    """

    def __init__(self) -> None:
        """
        Initializes an instance of the customerRegistrationByCountryFig class.
        """
        pass

    def makeFig(self,df):
        """
        Creates a bar chart using Plotly Graph Objects based on the provided DataFrame.

        Parameters
        ----------
        df : pandas.DataFrame
            DataFrame containing registration year ('registration_year'), country names ('country'), 
            and number of customers registered ('num_customers_registered').

        Returns
        -------
        plotly.graph_objs._figure.Figure
            A Plotly figure object representing the bar chart of customer registration analysis by country.
        """
        # Create a figure
        fig = go.Figure()

        # List of unique countries
        countries = df['country'].unique()

        # Add traces for each country
        for country in countries:
            country_data = df[df['country'] == country]
            fig.add_trace(go.Bar(x=country_data['registration_year'], y=country_data['num_customers_registered'],
                                name=country))

        # Update layout with dropdown menu
        fig.update_layout(
            title='Customer Registration Analysis by Country',
            xaxis_title='Registration Year',
            yaxis_title='Number of Customers Registered',
            updatemenus=[
                {
                    'buttons': [
                        {
                            'label': 'All Countries',
                            'method': 'update',
                            'args': [{'visible': [True] * len(countries)},
                                    {'title': 'Customer Registration Analysis by Country'}]
                        }
                    ] + [
                        {
                            'label': country,
                            'method': 'update',
                            'args': [{'visible': [country == c for c in countries]},
                                    {'title': f'Customer Registration Analysis for {country}'}]
                        }
                        for country in countries
                    ],
                    'direction': 'down',
                    'showactive': True,
                }
            ]
        )

        return fig