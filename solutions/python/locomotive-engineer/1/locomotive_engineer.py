
"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagon numbers."""
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons."""
    each_wagons_id.remove(1)

    return (
        [1]
        + missing_wagons
        + each_wagons_id[2:]
        + each_wagons_id[:2]
    )


def add_missing_stops(route, **stops):
    """Add missing stops to route dict."""
    route["stops"] = list(stops.values())
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information."""
    route.update(more_route_information)
    return route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons."""
    return [list(row) for row in zip(*wagons_rows)]
