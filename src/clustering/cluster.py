import logging

from .. import get_debug

DEBUG = get_debug()
LOGGER = logging.getLogger(__name__)


class Cluster(object):
    def __init__(self, cluster_id):
        self.id = cluster_id

    def info(self):
        LOGGER.info('Cluster[%d]: %s' % (self.id, self))
