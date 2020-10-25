import numpy as np

from basic import basic
from two_pass import two_pass

from sklearn.cluster import KMeans


def write_cluster_to_file(file_name: str, cluster):
    with open(file_name, 'w') as f:
        f.writelines('\n'.join(map(lambda elem: str(elem), cluster)))


def get_collection_from_file(file_name: str):
    with open(file_name, 'r') as f:
        collection = []
        for line in f.readlines():
            # line == '5.1,3.5,1.4,0.2,Iris-setosa\n'
            line = line.replace('\n', '')
            line_list = line.split(',')
            values = tuple([float(v) for v in line_list[:-1]])
            elem = (line_list[-1], values)
            collection.append(elem)
    return collection


def main():
    collection = get_collection_from_file('txts/iris.txt')

    clusters_basic = basic(collection, 3, 1.5)
    clusters_two_pass = two_pass(collection, 3, 1.5)

    X = np.array(list(map(lambda y: y[1], collection)))
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

    kmeans_01 = []
    kmeans_02 = []
    kmeans_03 = []

    for i, x in enumerate(kmeans.labels_):
        if x == 0:
            kmeans_01.append(collection[i])
        elif x == 1:
            kmeans_02.append(collection[i])
        else:
            kmeans_03.append(collection[i])

    write_cluster_to_file('txts/basic_cluster_01.txt', clusters_basic[0])
    write_cluster_to_file('txts/basic_cluster_02.txt', clusters_basic[1])
    write_cluster_to_file('txts/basic_cluster_03.txt', clusters_basic[2])

    write_cluster_to_file('txts/two_pass_cluster_01.txt', clusters_two_pass[0])
    write_cluster_to_file('txts/two_pass_cluster_02.txt', clusters_two_pass[1])
    write_cluster_to_file('txts/two_pass_cluster_03.txt', clusters_two_pass[2])

    write_cluster_to_file('txts/kmeans_cluster_01.txt', kmeans_01)
    write_cluster_to_file('txts/kmeans_cluster_02.txt', kmeans_02)
    write_cluster_to_file('txts/kmeans_cluster_03.txt', kmeans_03)


if __name__ == '__main__':
    main()
