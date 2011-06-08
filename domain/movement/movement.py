from datetime import datetime
from should_dsl import should
from domain.base.decorable import Decorable
from domain.node.node import Node
from domain.supportive.association_error import AssociationError


class Movement(Decorable):

    def __init__(self, name=None):
        self.name = name

    def set_source(self, source):
        try:
            source |should| be_instance_of(Node)
        except:
            raise AssociationError('Source: Node instance expected, instead %s passed' % type(source))
        self.source = source

    def set_destination(self, destination):
        try:
            destination |should| be_instance_of(Node)
        except:
            raise AssociationError('Destination: Node instance expected, instead %s passed' % type(destination))
        self.destination = destination

    def store_execution_arguments(self, *arguments):
        self.execution_arguments = []
        for argument in arguments:
            self.execution_arguments.append(argument)

