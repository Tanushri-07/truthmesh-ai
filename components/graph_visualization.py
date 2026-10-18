import networkx as nx
import plotly.graph_objects as go


def create_graph_figure(facts):
    graph = nx.Graph()

    for fact in facts:
        document = str(fact[0])
        date = str(fact[1])
        event = str(fact[2])

        fact_node = f"Fact: {date}"

        graph.add_node(document, category="Document")
        graph.add_node(fact_node, category="Fact")
        graph.add_node(event, category="Event")

        graph.add_edge(document, fact_node)
        graph.add_edge(fact_node, event)

    if graph.number_of_nodes() == 0:
        return None

    positions = nx.spring_layout(
        graph,
        seed=42,
        k=1.2,
        iterations=100
    )

    edge_x = []
    edge_y = []

    for source, target in graph.edges():
        x0, y0 = positions[source]
        x1, y1 = positions[target]

        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edges = go.Scatter(
        x=edge_x,
        y=edge_y,
        mode="lines",
        line=dict(width=1.5, color="#777777"),
        hoverinfo="none"
    )

    colors = {
        "Document": "#A78BFA",
        "Fact": "#F9A8D4",
        "Event": "#67E8F9"
    }

    node_x = []
    node_y = []
    node_text = []
    node_colors = []

    for node, attributes in graph.nodes(data=True):
        x, y = positions[node]

        node_x.append(x)
        node_y.append(y)
        node_text.append(node)
        node_colors.append(
            colors.get(attributes["category"], "#FFFFFF")
        )

    nodes = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",
        text=node_text,
        textposition="top center",
        hovertext=node_text,
        hoverinfo="text",
        marker=dict(
            size=22,
            color=node_colors,
            line=dict(width=1, color="#FFFFFF")
        )
    )

    figure = go.Figure(data=[edges, nodes])

    figure.update_layout(
        template="plotly_dark",
        showlegend=False,
        margin=dict(l=20, r=20, t=20, b=20),
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        height=550
    )

    return figure