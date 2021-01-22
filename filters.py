import operator
from itertools import islice

class UnsupportedCriterionError(NotImplementedError):
    """A filter criterion is unsupported."""


class AttributeFilter:
    def __init__(self, op, value):
        self.op = op
        self.value = value

    def __call__(self, approach):
        return self.op(self.get(approach), self.value)

    @classmethod
    def get(cls, approach):
        raise UnsupportedCriterionError

    def __repr__(self):
        return f"{self.__class__.__name__}(op=operator.{self.op.__name__}, value={self.value})"


def create_filters(date=None, start_date=None, end_date=None,
                   distance_min=None, distance_max=None,
                   velocity_min=None, velocity_max=None,
                   diameter_min=None, diameter_max=None,
                   hazardous=None):
    
    list_of_filters = list()
    if (date):
        list_of_filters.append(DateFilter(operator.eq, date))
    if (start_date):
        list_of_filters.append(DateFilter(operator.ge, start_date))
    if (end_date):
        list_of_filters.append(DateFilter(operator.le, end_date))
    if (distance_min):
        list_of_filters.append(DistanceFilter(operator.ge, distance_min))
    if (distance_max):
        list_of_filters.append(DistanceFilter(operator.le, distance_max))
    if (distance_max):
        list_of_filters.append(DistanceFilter(operator.le, distance_max))
    if (velocity_min):
        list_of_filters.append(VelocityFilter(operator.ge, velocity_min))
    if (velocity_max):
        list_of_filters.append(VelocityFilter(operator.le, velocity_max))
    if (diameter_min):
        list_of_filters.append(DiameterFilter(operator.ge, diameter_min))
    if (diameter_max):
        list_of_filters.append(DiameterFilter(operator.le, diameter_max))
    if (not hazardous):
        list_of_filters.append(HazardousFilter(operator.eq, hazardous))
    
    return list_of_filters


class DistanceFilter(AttributeFilter):
    @classmethod
    def get(cls, approach):
        return approach.distance


class VelocityFilter(AttributeFilter):
    @classmethod
    def get(cls, approach):
        return approach.velocity


class DateFilter(AttributeFilter):
    @classmethod
    def get(cls, approach):
        return approach.time.date()


class DiameterFilter(AttributeFilter):
    @classmethod
    def get(cls, approach):
        return approach.neo.diameter


class HazardousFilter(AttributeFilter):
    @classmethod
    def get(cls, approach):
        return approach.neo.hazardous


def limit(iterator, n):
    """Produce a limited stream of values from an iterator.

    If `n` is 0 or None, don't limit the iterator at all.

    :param iterator: An iterator of values.
    :param n: The maximum number of values to produce.
    :yield: The first (at most) `n` values from the iterator.
    """
    # TODO: Produce at most `n` values from the given iterator.
    
    if n == 0 or n is None:
        n = None
        
    return islice(iterator, n)
