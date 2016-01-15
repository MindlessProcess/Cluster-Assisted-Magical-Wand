from abc import ABCMeta, abstractmethod


class BaseNeuron(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        self.weights = []

    @abstractmethod
    def transfert(self, inputs):
        raise NotImplementedError()

    @abstractmethod
    def activate(self, inputs):
        raise NotImplementedError()

    @abstractmethod
    def learn(self, inputs, expected):
        raise NotImplementedError()
