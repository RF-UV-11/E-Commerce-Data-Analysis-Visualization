import plotly.express as px
import plotly.graph_objects as go
import networkx as nx


class databaseClassDiagramFig:
    """
    A class to create a database schema diagram with relationship types using Plotly.

    Methods
    -------
    makeFig(relationship_info):
        Creates a database schema diagram based on the provided relationship information.

    Attributes
    ----------
    None
    """

    def __init__(self) -> None:
        """
        Initializes an instance of the databaseClassDiagramFig class.
        """
        pass

    def makeFig(self,relationship_info):
        """
        Creates a database schema diagram with relationship types using Plotly.

        Parameters
        ----------
        relationship_info : list
            List containing tuples of relationship information extracted from the database.
            Each tuple should contain (table_name, column_name, foreign_table_name, foreign_column_name, constraint_type).

        Returns
        -------
        plotly.graph_objs._figure.Figure
            A Plotly figure object representing the database schema diagram with relationship types.
        """
        # Create a directed graph
        G = nx.DiGraph()

        # Add nodes (tables)
        for table, _, _, _, _ in relationship_info:
            if not table.startswith('pg_'):  # Exclude nodes starting with 'pg'
                G.add_node(table)

        # Add edges (relationships)
        for table, _, foreign_table, _, constraint_type in relationship_info:
            if not table.startswith('pg_') and not foreign_table.startswith('pg_'):  # Exclude edges involving 'pg' tables
                if constraint_type == 'FOREIGN KEY':
                    # Determine relationship type
                    relationship_type = ''
                    if G.has_edge(foreign_table, table):
                        relationship_type = 'Many-to-Many'
                    else:
                        G.add_edge(table, foreign_table)
                        if len(list(G.predecessors(foreign_table))) > 1:
                            relationship_type = 'Many-to-One'
                        else:
                            relationship_type = 'One-to-One'

                    # Store relationship type as an edge attribute
                    G.edges[table, foreign_table]['relationship_type'] = relationship_type

        # Initialize nodes and edges positions using spring layout
        pos = nx.spring_layout(G, seed=42)

        # Create edge traces for Plotly
        edge_traces = []
        for edge in G.edges(data=True):
            src, dst, attr = edge
            edge_style = 'solid' if attr['relationship_type'] in ['One-to-One', 'Many-to-One'] else 'dash'
            edge_traces.append(go.Scatter(x=[pos[src][0], pos[dst][0]], y=[pos[src][1], pos[dst][1]],
                                        mode='lines',
                                        line=dict(width=2, dash=edge_style),
                                        hoverinfo='text',
                                        text=f"{src} to {dst}: {attr['relationship_type']}",
                                        showlegend=False))

        # Add annotations for edge labels
        edge_annotations = []
        for edge in G.edges(data=True):
            src, dst, attr = edge
            edge_label = f"{attr['relationship_type']}"
            edge_annotations.append(go.layout.Annotation(
                x=(pos[src][0] + pos[dst][0]) / 2,
                y=(pos[src][1] + pos[dst][1]) / 2,
                text=edge_label,
                showarrow=False,
                font=dict(size=10, color="black"),
                xref="x",
                yref="y"
            ))

        # Create node traces for Plotly
        node_traces = go.Scatter(x=[pos[node][0] for node in G.nodes()],
                                y=[pos[node][1] for node in G.nodes()],
                                mode='markers+text',
                                text=list(G.nodes()),
                                hoverinfo='text',
                                marker=dict(symbol='square', size=40, color='lightblue', line=dict(color='black', width=2)),
                                textposition='bottom center')

        # Create figure
        fig = go.Figure(data=edge_traces + [node_traces])

        # Update layout with edge annotations
        fig.update_layout(
            title='Database Schema Diagram with Relationship Types',
            title_x=0.5,
            title_font_size=24,
            hovermode='closest',
            showlegend=False,
            width=1200,
            height=800,
            margin=dict(l=20, r=20, t=60, b=20),
            xaxis=dict(visible=False, range=[-1.2, 1.2]),
            yaxis=dict(visible=False, range=[-1.2, 1.2]),
            annotations=edge_annotations  # Add edge annotations
        )

        return fig
