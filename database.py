"""
NEODatabase 
An Object that holds all neos and approaches sorted by designation to create the object fast
"""

class NEODatabase:
    def __init__(self, neos, approaches):
    # init method to initialize the NEODatabase
        neos.sort(key=lambda x: x.designation)
        approaches.sort(key=lambda x: x.designation)
        self._neos = neos
        self._approaches = approaches

        i = 0
        j = 0
        
        while i < len(neos) and j < len(approaches):
            neo = neos[i] 
            approach = approaches[j]   
            if neo.designation == approach.designation:     
                neo.append(approach)
                approach.attach(neo)
                j += 1
            else:
                i += 1

       
    def neoAt(self, index):
    # helper method to locate a neo at index
        return self._neos[index]
    
    def approachAt(self, index):
    # helper method to locate an approach by index
        return self._approaches[index]

    def __getitem__(self, index):
    # to make it an iterable, returns a neo (which has all informations)
        return self._neos[index]
    
    def get_neo_by_designation(self, designation):
    # return a neo by designation or None
        for neo in self._neos:
            if neo.designation == designation:
                return neo
        return None

    def get_neo_by_name(self, name):
    # return a neo by name or None
        for neo in self._neos:
            if neo.neo_name == name:
                return neo
        return None

    def query(self, filters=()):
        """Query close approaches to generate those that match a collection of filters.
        This generates a stream of `CloseApproach` objects that match all of the
        provided filters.
        If no arguments are provided, generate all known close approaches.
        The `CloseApproach` objects are generated in internal order, which isn't
        guaranteed to be sorted meaninfully, although is often sorted by time.
        :param filters: A collection of filters capturing user-specified criteria.
        :return: A stream of matching `CloseApproach` objects.
        """
        for approach in self._approaches:
            yield approach
