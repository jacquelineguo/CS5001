from lightrail import is_valid_station, get_direction, get_num_stops,\
       get_station_num


def test_is_valid_station():
    assert(is_valid_station("Angle Lake"))
    assert(not is_valid_station("Bellingham"))
    assert(is_valid_station("SeaTac/Airport"))


def test_get_station_num():
    assert(get_station_num("University of Washington", "Stadium") == (0, 6))
    assert(get_station_num("Angle Lake", "Mount Baker") == (15, 9))
    assert(get_station_num("Tacoma", "Mount Baker") == (0, 0))


def test_get_direction():
    assert(get_direction("University of Washington", "Angle Lake")
           == "Southbound")
    assert(get_direction("Angle Lake", "University of Washington")
           == "Northbound")
    assert(get_direction("University Street", "University Street")
           == "No destination found")


def test_get_num_stops():
    assert(get_num_stops("University of Washington", "Angle Lake") == 15)
    assert(get_num_stops("Angle Lake", "University of Washington") == 15)
    assert(get_num_stops("University Street", "University Street") == 0)
    assert(get_num_stops("University Street", "Tacoma") == 0)
