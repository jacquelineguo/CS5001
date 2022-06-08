'''
Xuan Guo
CS5001, Fall 2020

This program helps user to get basic directions on the Seattle Link light rail
'''
LINK_STATIONS = ("University of Washington", "Capitol Hill", "Westlake",
                 "University Street", "Pioneer Square",
                 "International District/Chinatown", "Stadium", "SODO",
                 "Beacon Hill", "Mount Baker", "Columbia City", "Othello",
                 "Rainier Beach", "Tukwila International Boulevard",
                 "SeaTac/Airport", "Angle Lake")


def is_valid_station(station):
    '''
        Function -- is_valid_station
            Checks if a given string is a valid Seattle light rail station.
            Provided station must match a station name exactly. For example,
            "mount baker" would not be valid because the case doesn't match.
        Parameter:
            station -- The string to check
        Returns:
            True if a given string is a valid Seattle light rail station
            name, False otherwise.
    '''
    return station in LINK_STATIONS


def get_station_num(start, end):
    '''
        Function -- get_station_num
            Given start and end station names, find the station number sorted
            from 0 to 15
        Parameters:
            start -- The starting station name
            end -- The ending station name
        Returns:
            The station numbers of each point
    '''
    INVALID_INPUT = 0
    if is_valid_station(start) and is_valid_station(end):
        start_num = LINK_STATIONS.index(start)
        end_num = LINK_STATIONS.index(end)
        return start_num, end_num
    else:
        return INVALID_INPUT, INVALID_INPUT


def get_direction(start, end):
    '''
        Function -- get_direction
            Given start and end station names, determines if the direction is
            Northbound or Southbound.
        Parameters:
            start - The starting station name
            end - The ending station name.
        Returns:
            "Northbound" if the end station is north of the start station, or
            "Southbound" if the end station is south of the start station. If
            either station is invalid, or start and end stations are the same,
            return "No destination found".
    '''
    start_num, end_num = get_station_num(start, end)
    result = "No destination found"
    if is_valid_station(start) and is_valid_station(end):
        if start_num > end_num:
            result = "Northbound"
        elif start_num < end_num:
            result = "Southbound"
    return result


def get_num_stops(start, end):
    '''
        Function -- get_num_stops
            Calculates the number of stops from start to end.
        Parameters:
            start - The starting station name
            end - The ending station name.
        Returns:
            The number of stops from start to end. If either station is invalid
            or both stations are the same, return 0.
    '''
    start_num, end_num = get_station_num(start, end)
    return abs(start_num - end_num)
