from helpers import cd_to_datetime, datetime_to_str

class NearEarthObject:
    _all_objects = dict()
    _counter = 0

    def __init__(self, designation, name, diameter, hazardous):
        self.designation = designation
        if name:
            self.name = name
        else:
            self.name = None
        
        if diameter:
            self.diameter = float(diameter)
        else:
            self.diameter = float('nan')
            
        if hazardous:
            if hazardous == 'Y':
                self.hazardous = True
            elif hazardous == 'N':
                self.hazardous = False
            else:
                self.hazardous = False
        else:
            self.hazardous = False

        self.approaches = list()
        
        # private attributes to define obj_id
        self._object_id = NearEarthObject._counter
        
        # Increment so the next object has an incremented ID  
        NearEarthObject._counter += 1
        # create a class list for all instances of NEO
        NearEarthObject._all_objects[self._object_id] = self
                
    # let's make it an iterable class 
    def __getitem__(self, index):
        return self[index]  
    
    def __next__(self):
        try:
            result = self._all_objects[self._object_id]
        except IndexError:
            raise StopIteration
        self._object_id += 1
        return result
    
    def append(self, item):
        if type(item) == CloseApproach:
            self.approaches.append(item)
    
    @property
    def object_id(self):
        return self._object_id
    
    # return full name of the NEO
    @property
    def fullname(self):
        # if name is not empty return long fullname else short
        if self.name:
            return f"{self.designation} ({self.name})"
        else:
            return f"{self.designation}"

# return the string representation of the NEO
    def __str__(self):
        return (f"NearEarthObject(designation={self.designation}, name={self.name}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous}, "
                f"approaches={self.approaches}")

# return repr representation of the NEO
    def __repr__(self):
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")
        

class CloseApproach:
    def __init__(self, designation, time, distance, velocity, neo=None):
        self._designation = designation
        if type(time) == str:
            self.time = cd_to_datetime(time)
            
        if type(distance) == float:
            self.distance = distance
        else:
            self.distance = float(distance)
        
        if type(velocity) == float:
            self.velocity = velocity
        else:
            self.velocity = float(velocity)
        
        if neo:
            self.neo = neo
        else:
            self.neo = None

    @property 
    def designation(self):
        return self._designation
    
    @property
    def time_str(self):
        return datetime_to_str(self.time) 


    def attach(self, neo):
        if type(neo) == NearEarthObject:
            self.neo = neo

    def __str__(self):
        return f"At {self.time_str}, '{self.designation}' approaches Earth at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s."

    def __repr__(self):
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")
