import numpy
from sklearn.cluster import KMeans


class Clustering:
    def __init__(self, k=5):
        self.k = k
        self.k_means = KMeans(n_clusters=self.k)

    def reshape_array(self, input_data):
        data = numpy.asarray(input_data)
        n_samples, nx, ny = data.shape
        print(n_samples, nx, ny)
        return data.reshape(n_samples, nx * ny)

    def train(self, input_data):
        data = self.reshape_array(input_data)
        self.k_means.fit(data)
        print('Training Labels : ', self.k_means.labels_)

    def predict(self, input_data, replays):
        i = 0
        data = self.reshape_array(input_data)
        prediction = self.k_means.predict(data)
        build_dict = []

        for p in prediction:
            build_dict.append((p, replays[i]))
            i += 1
        return build_dict
