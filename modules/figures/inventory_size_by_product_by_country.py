import plotly.express as px
import plotly.graph_objects as go


class inventorySizeByProductByCountryFig:
    """
    A class to create a Plotly figure displaying total inventory size by product and country, with options to switch 
    between bar and scatter plots and to filter by country.

    Methods
    -------
    makeFig(df):
        Creates a Plotly figure displaying total inventory size by product and country, with interactive buttons for 
        plot types and country selection.

    Attributes
    ----------
    None
    """


    def __init__(self) -> None:
        """
        Initializes an instance of the inventorySizeByProductByCountryFig class.
        """
        pass

    def makeFig(self,df):
        """
        Creates a Plotly figure displaying total inventory size by product and country, with interactive buttons for 
        plot types and country selection.

        Parameters
        ----------
        df : pandas.DataFrame
            DataFrame containing columns 'product_name', 'country', and 'total_quantity_available'.

        Returns
        -------
        plotly.graph_objs._figure.Figure
            A Plotly figure object representing the inventory size by product and country, with interactive buttons 
            for plot types and country selection.
        """
        # Create a figure
        fig = go.Figure()

        # List of unique countries
        countries = df['country'].unique()

        # Add traces for bar and scatter plots for each country
        for country in countries:
            country_data = df[df['country'] == country]
            fig.add_trace(go.Bar(x=country_data['product_name'], y=country_data['total_quantity_available'],
                                name=f"{country} (Bar)", visible=True))
            fig.add_trace(go.Scatter(x=country_data['product_name'], y=country_data['total_quantity_available'],
                                    mode='lines+markers', name=f"{country} (Scatter)", visible=False))

        # Create buttons for plot types
        plot_type_buttons = [
            {
                'label': 'Bar Plot',
                'method': 'update',
                'args': [{'visible': [True if i % 2 == 0 else False for i in range(len(fig.data))]},
                        {'title': 'Total Inventory by Product Name and Country (Bar Plot)'}]
            },
            {
                'label': 'Scatter Plot',
                'method': 'update',
                'args': [{'visible': [False if i % 2 == 0 else True for i in range(len(fig.data))]},
                        {'title': 'Total Inventory by Product Name and Country (Scatter Plot)'}]
            }
        ]

        # Create buttons for countries
        country_buttons = [
            {
                'label': 'All Countries',
                'method': 'update',
                'args': [{'visible': [True] * len(fig.data)},
                        {'title': 'Total Inventory by Product Name and Country'}]
            }
        ]

        for country in countries:
            visibility = []
            for i in range(len(countries)):
                if countries[i] == country:
                    visibility.append(True)
                    visibility.append(True)
                else:
                    visibility.append(False)
                    visibility.append(False)
            country_buttons.append(
                {
                    'label': country,
                    'method': 'update',
                    'args': [{'visible': visibility},
                            {'title': f'Total Inventory by Product Name for {country}'}]
                }
            )

        # Update layout with dropdown menus
        fig.update_layout(
            title='Total Inventory by Product Name and Country',
            xaxis_title='Product Name',
            yaxis_title='Total Quantity Available',
            updatemenus=[
                {
                    'buttons': plot_type_buttons,
                    'direction': 'down',
                    'showactive': True,
                    'x': 0.17,
                    'xanchor': 'left',
                    'y': 1.15,
                    'yanchor': 'top'
                },
                {
                    'buttons': country_buttons,
                    'direction': 'down',
                    'showactive': True,
                    'x': 0.01,
                    'xanchor': 'left',
                    'y': 1.15,
                    'yanchor': 'top'
                }
            ]
        )

        return fig