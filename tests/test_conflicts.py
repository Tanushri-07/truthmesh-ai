from services.graph_service import GraphService


def test_graph_service_connects():
    service = GraphService()

    facts = service.get_facts()

    assert isinstance(facts, list)


def test_conflict_query_returns_rows():
    service = GraphService()

    conflicts = service.get_conflicts()

    assert isinstance(conflicts, list)