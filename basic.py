from typing import Tuple, List

from utils import find_distance, arg_min


def basic(collection, k, threshold):
    clusters: List[List[Tuple[str, tuple]]] = [[collection[0]]]

    for x in collection[1:]:
        arg_min_index = arg_min(x, clusters)

        if find_distance(x, clusters[arg_min_index]) > threshold and len(clusters) < k:
            clusters.append([x])
        else:
            clusters[arg_min_index].append(x)

    return clusters
