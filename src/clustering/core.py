from .cluster import Cluster


class Core(object):
    def __init__(self, number_of_clusters):
        self.number_of_clusters = int(number_of_clusters)
        self._cluster_id_incrementor = 0
        self.clusters = []

    def run(self):
        for _ in range(self.number_of_clusters):
            self.clusters.append(Cluster(self._get_new_cluster_id()))

    def info(self):
        print 'NUMBER OF CLUSTERS: %d' % self.number_of_clusters
        for i in range(len(self.clusters)):
            self.clusters[i].info()

    def _get_new_cluster_id(self):
        self._cluster_id_incrementor += 1
        return self._cluster_id_incrementor
