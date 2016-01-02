class Cluster(object):
    def __init__(self, cluster_id):
        self.id = cluster_id

    def info(self):
        print 'Cluster[%d]: %s' % (self.id, self)
