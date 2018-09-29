# encoding: utf-8
# module zope.interface._zope_interface_coptimizations
# from C:\Users\sebyg\PycharmProjects\proyecto prueba\venv\lib\site-packages\zope\interface\_zope_interface_coptimizations.cp36-win_amd64.pyd
# by generator 1.145
""" C optimizations for zope.interface """

# imports
import _interface_coptimizations as ___interface_coptimizations
import _zope_interface_coptimizations as ___zope_interface_coptimizations


# functions

def getObjectSpecification(*args, **kwargs): # real signature unknown
    """ Get an object's interfaces (internal api) """
    pass

def implementedBy(*args, **kwargs): # real signature unknown
    """
    Interfaces implemented by a class or factory.
    Raises TypeError if argument is neither a class nor a callable.
    """
    pass

def providedBy(*args, **kwargs): # real signature unknown
    """ Get an object's interfaces """
    pass

# classes

class SpecificationBase(object):
    """ Base type for Specification objects """
    def implementedBy(self, *args, **kwargs): # real signature unknown
        """
        Test whether the specification is implemented by a class or factory.
        Raise TypeError if argument is neither a class nor a callable.
        """
        pass

    def isOrExtends(self, *args, **kwargs): # real signature unknown
        """ Test whether a specification is or extends another """
        pass

    def providedBy(self, *args, **kwargs): # real signature unknown
        """ Test whether an interface is implemented by the specification """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class ClassProvidesBase(___interface_coptimizations.SpecificationBase):
    """ C Base class for ClassProvides """
    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class InterfaceBase(object):
    """ Interface base type providing __call__ and __adapt__ """
    def __adapt__(self, *args, **kwargs): # real signature unknown
        """ Adapt an object to the reciever """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class LookupBase(object):
    # no doc
    def adapter_hook(self, *args, **kwargs): # real signature unknown
        pass

    def changed(self, *args, **kwargs): # real signature unknown
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        pass

    def lookup1(self, *args, **kwargs): # real signature unknown
        pass

    def lookupAll(self, *args, **kwargs): # real signature unknown
        pass

    def queryAdapter(self, *args, **kwargs): # real signature unknown
        pass

    def subscriptions(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class ObjectSpecificationDescriptor(object):
    """ Object Specification Descriptor """
    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class VerifyingBase(___zope_interface_coptimizations.LookupBase):
    # no doc
    def adapter_hook(self, *args, **kwargs): # real signature unknown
        pass

    def changed(self, *args, **kwargs): # real signature unknown
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        pass

    def lookup1(self, *args, **kwargs): # real signature unknown
        pass

    def lookupAll(self, *args, **kwargs): # real signature unknown
        pass

    def queryAdapter(self, *args, **kwargs): # real signature unknown
        pass

    def subscriptions(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

adapter_hooks = []

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

