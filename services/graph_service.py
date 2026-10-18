from falkordb import FalkorDB


class GraphService:
    """Manage TruthMesh AI's FalkorDB connection and queries."""

    def __init__(
        self,
        host="localhost",
        port=6379,
        graph_name="truthmesh",
    ):
        self.db = FalkorDB(host=host, port=port)
        self.graph = self.db.select_graph(graph_name)

    def query(self, cypher):
        """Execute a Cypher query and return the result rows."""
        result = self.graph.query(cypher)
        return result.result_set

    def get_facts(self):
        """Retrieve facts and their source documents."""
        cypher = """
        MATCH
            (d:Document)-[:CONTAINS]->(f:Fact)-[:REFERS_TO]->(e:Event)
        RETURN
            d.name AS document,
            f.date AS date,
            e.name AS event
        """

        return self.query(cypher)

    def get_conflicts(self):
        """Find differing dates connected to the same event."""
        cypher = """
        MATCH
            (d1:Document)-[:CONTAINS]->(f1:Fact)-[:REFERS_TO]->(e:Event),
            (d2:Document)-[:CONTAINS]->(f2:Fact)-[:REFERS_TO]->(e)
        WHERE
            id(d1) < id(d2)
            AND f1.date <> f2.date
        RETURN
            e.name AS event,
            d1.name AS document1,
            f1.date AS date1,
            d2.name AS document2,
            f2.date AS date2
        """

        return self.query(cypher)

    def get_graph_data(self):
        """Retrieve the connected facts for graph visualization."""
        cypher = """
        MATCH
            (d:Document)-[:CONTAINS]->(f:Fact)-[:REFERS_TO]->(e:Event)
        RETURN
            d.name AS document,
            f.date AS date,
            e.name AS event
        """

        return self.query(cypher)