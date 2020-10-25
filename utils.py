import statistics

from math import sqrt
from typing import Tuple, List


def find_distance(x: Tuple[float], cluster: List[Tuple[str, tuple]]) -> float:
    x_val = x[1]
    euclidean_distances = []

    for iris, values in cluster:
        euclidean_distance = sqrt(
            (x_val[0] - values[0]) ** 2 +
            (x_val[1] - values[1]) ** 2 +
            (x_val[2] - values[2]) ** 2 +
            (x_val[3] - values[3]) ** 2
        )
        euclidean_distances.append(round(euclidean_distance, 4))

    mode = statistics.mode(euclidean_distances)

    return mode


def arg_min(elem, clusters):
    distances = [(index, find_distance(elem, cluster)) for index, cluster in enumerate(clusters)]

    index = None
    distance = float('inf')

    for i, dist in distances:
        if dist < distance:
            distance = dist
            index = i

    return index
