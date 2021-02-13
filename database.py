"""
NEODatabase 
An Object that holds all neos and approaches sorted by designation to create the object fast
"""

class NEODatabase:
    def __init__(self, neos, approaches):
    # init method to initialize the NEODatabase
        neos = sorted(neos, key=lambda x: x.designation)
        approaches = sorted(approaches, key=lambda x: x.designation)
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
    # for each approach we have to check the filters
        for approach in self._approaches:
            # mapped returns something like [True, False, True] for filters
            mapped = map(lambda x: x(approach), filters)
            # if all flags are True like [True, True, True]
            if all(flag == True for flag in mapped):
                # we can yield that approach, because it matches all filter criteriums
                yield approach
