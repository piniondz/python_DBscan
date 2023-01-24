from dbscan import DBscan
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import unittest


class TestDBscan(unittest.TestCase):
    def test_circles(self):
        min_points = 7
        eps = 0.3
        x, y = cluster(circles(), eps=eps, min_samples=min_points)
        for c in range(0, len(x)):
            self.assertEqual(x[c], y[c])

    def test_blobs(self):
        min_points = 7
        eps = 0.3
        x, y = cluster(blobs(), eps=eps, min_samples=min_points)
        for c in range(0, len(x)):
            self.assertEqual(x[c], y[c])


def circles():
    dset, true_labels = datasets.make_circles(n_samples=500, factor=0.4, noise=0.05)
    data = StandardScaler().fit_transform(dset)
    return data


def blobs():
    centers = [[1, 1], [-1, -1], [1, -1]]
    dset, true_labels = datasets.make_blobs(n_samples=750, centers=centers, cluster_std=0.4, random_state=0)
    data = StandardScaler().fit_transform(dset)
    return data


def cluster(data, eps, min_samples):
    db = DBSCAN(eps=eps, min_samples=min_samples).fit(data)
    my_db = DBscan(data, min_samples, eps).dbscan()
    return db.labels_, my_db[1]


def plot():
    eps = 0.3
    minimal = 10
    data = blobs()
    labels, s_labels = cluster(data=data, eps=eps, min_samples=minimal)
    plt.scatter(data[:, 0], data[:, 1], c=labels)
    plt.show()
    return


if __name__ == '__main__':
    # plot()
    unittest.main()
