import pytest

from code_challenges.graph.graph import Graph, Vertex, Edge


def test_add_node_returns_vertex():

    graph = Graph()

    vertex = graph.add_node("spam")

    assert isinstance(vertex, Vertex)


def test_add_node_return_has_correct_value():

    graph = Graph()

    expected = "spam"  # a vertex's value that comes back

    actual = graph.add_node("spam").value

    assert actual == expected


def test_add_edge_sunny():

    graph = Graph()

    start = graph.add_node("start")

    end = graph.add_node("end")

    graph.add_edge(start, end)

    # no fail means a pass

    # can be more explicit if you like

    try:
        graph.add_edge(start, end)
    except KeyError:
        pytest.fail("KeyError should not be thrown")


def test_add_edge_with_weight():

    graph = Graph()

    start = graph.add_node("start")

    end = graph.add_node("end")

    weight = 10

    graph.add_edge(start, end, weight)


def test_add_edge_interloper_start():

    graph = Graph()

    start = Vertex("start")

    end = graph.add_node("end")

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_interloper_end():

    graph = Graph()

    end = Vertex("end")

    start = graph.add_node("start")

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_get_nodes():

    graph = Graph()

    graph.add_node("banana")

    graph.add_node("apple")

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected


def test_get_neighbors_none():

    graph = Graph()

    banana = graph.add_node("banana")

    neighbors = graph.get_neighbors(banana)

    assert len(neighbors) == 0


def test_get_neighbors_returns_edges():

    graph = Graph()

    banana = graph.add_node("banana")

    apple = graph.add_node("apple")

    graph.add_edge(apple, banana)

    neighbors = graph.get_neighbors(apple)

    assert len(neighbors) == 1

    neighbor = neighbors[0]

    assert isinstance(neighbor, Edge)

    assert neighbor.vertex.value == 'banana'


def test_get_neighbors_returns_edges_with_default_weight():

    graph = Graph()

    banana = graph.add_node("banana")

    apple = graph.add_node("apple")

    graph.add_edge(apple, banana)

    neighbors = graph.get_neighbors(apple)

    actual = neighbors[0].weight

    expected = 0

    assert actual == expected


def test_get_neighbors_returns_edges_with_custom_weight():

    graph = Graph()

    banana = graph.add_node("banana")

    apple = graph.add_node("apple")

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neighbors(apple)

    neighbor_edge = neighbors[0]

    assert neighbor_edge.weight == 44


def test_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected


def test_size_one():

    graph = Graph()

    graph.add_node("spam")

    expected = 1

    actual = graph.size()

    assert actual == expected


def test_size_two():

    graph = Graph()

    graph.add_node("spam")

    graph.add_node("bacon")

    expected = 2

    actual = graph.size()

    assert actual == expected


def test_breadth_first():

    g = Graph()

    pandora = g.add_node("Pandora")

    arendelle = g.add_node("Arendelle")

    metroville = g.add_node("Metroville")

    monstropolis = g.add_node("Monstropolis")

    narnia = g.add_node("Narnia")

    naboo = g.add_node("Naboo")

    g.add_edge(pandora, arendelle)
    g.add_edge(arendelle, pandora)

    g.add_edge(arendelle, metroville)
    g.add_edge(metroville, arendelle)

    g.add_edge(arendelle, monstropolis)
    g.add_edge(monstropolis, arendelle)

    g.add_edge(metroville, monstropolis)
    g.add_edge(monstropolis, metroville)

    g.add_edge(metroville, narnia)
    g.add_edge(narnia, metroville)

    g.add_edge(metroville, naboo)
    g.add_edge(naboo, metroville)

    g.add_edge(narnia, naboo)
    g.add_edge(naboo, narnia)

    # stretch make more flexible vs. always returning list of vertices

    vertices = g.breadth_first(pandora)

    # convert vertices into values for easier testing
    values = [vertex.value for vertex in vertices]

    assert values == ["Pandora", "Arendelle", "Metroville", "Monstropolis", "Narnia", "Naboo"]


def test_connected():
    g = Graph()

    pandora = g.add_node("Pandora")
    arendelle = g.add_node("Arendelle")

    g.add_edge(pandora, arendelle)
    g.add_edge(arendelle, pandora)

    assert g.connected(pandora, arendelle) is True
    assert g.connected(arendelle, pandora) is True


def test_not_connected():
    g = Graph()

    pandora = g.add_node("Pandora")
    arendelle = g.add_node("Arendelle")

    assert g.connected(pandora, arendelle) is False
    assert g.connected(arendelle, pandora) is False


def test_one_way_connected():
    g = Graph()

    pandora = g.add_node("Pandora")
    arendelle = g.add_node("Arendelle")

    g.add_edge(pandora, arendelle)

    assert g.connected(pandora, arendelle) is True
    assert g.connected(arendelle, pandora) is False


def test_fixture(flights_fixture):
    flights = flights_fixture

    pandora = flights.get_node("Pandora")
    metroville = flights.get_node("Metroville")

    assert flights.connected(pandora, metroville) is True
    assert flights.connected(metroville, pandora) is True


def test_add_edge_between_two(flights_fixture):
    pandora = flights_fixture.get_node("Pandora")
    metroville = flights_fixture.get_node("Metroville")

    actual = flights_fixture.get_edges([pandora, metroville])
    expect = True, 82

    assert actual == expect


def test_add_edge_between_three(flights_fixture):
    arendelle = flights_fixture.get_node("Arendelle")
    monstropolis = flights_fixture.get_node("Monstropolis")
    naboo = flights_fixture.get_node("Naboo")

    actual = flights_fixture.get_edges([arendelle, monstropolis, naboo])
    expect = True, 115

    assert actual == expect


def test_add_edge_between_two_disconnected(flights_fixture):
    naboo = flights_fixture.get_node("Naboo")
    pandora = flights_fixture.get_node("Pandora")

    actual = flights_fixture.get_edges([naboo, pandora])
    expect = False, 0

    assert actual == expect


@pytest.fixture
def flights_fixture():
    flights = Graph()

    pandora      = flights.add_node("Pandora")
    arendelle    = flights.add_node("Arendelle")
    metroville   = flights.add_node("Metroville")
    narnia       = flights.add_node("Narnia")
    naboo        = flights.add_node("Naboo")
    monstropolis = flights.add_node("Monstropolis")

    flights.add_edge(pandora, arendelle, 150)
    flights.add_edge(pandora, metroville, 82)
    flights.add_edge(arendelle, metroville, 99)
    flights.add_edge(arendelle, monstropolis, 42)
    flights.add_edge(metroville, narnia, 37)
    flights.add_edge(metroville, naboo, 26)
    flights.add_edge(metroville, monstropolis, 105)
    flights.add_edge(monstropolis, naboo, 73)
    flights.add_edge(narnia, naboo, 250)

    flights.add_edge(arendelle, pandora, 150)
    flights.add_edge(metroville, pandora, 82)
    flights.add_edge(metroville, arendelle, 99)
    flights.add_edge(monstropolis, arendelle, 42)
    flights.add_edge(narnia, metroville, 37)
    flights.add_edge(naboo, metroville, 26)
    flights.add_edge(monstropolis, metroville, 105)
    flights.add_edge(naboo, monstropolis, 73)
    flights.add_edge(naboo, narnia, 250)

    return flights
