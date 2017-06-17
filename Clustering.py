import numpy
from sklearn.cluster import KMeans


class Clustering:
    def __init__(self, k=5):
        self.k = k
        self.k_means = KMeans(n_clusters=self.k)

    def reshape_array(self, input_data):
        data = numpy.asarray(input_data)
        n_samples, nx, ny = data.shape
        return data.reshape(n_samples, nx * ny)

    def train(self, input_data):
        X = self.reshape_array(input_data)
        self.k_means.fit(X)
        print('labels : ', self.k_means.labels_)

    def predict(self, input_data):
        X = self.reshape_array(input_data)
        print(self.k_means.predict(X))
