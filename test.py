from extract import load_neos, load_approaches
from database import NEODatabase
import time

start = time.time()
neos = load_neos("data/neos.csv")
end = time.time()
print("Loading neos.csv takes " + str(end - start) + " seconds.")

start = time.time()
approaches = load_approaches("data/cad.json")
end = time.time()
print("Loading cad.json takes " + str(end - start) + " seconds.")

start = time.time()
neodb = NEODatabase(neos, approaches)
end = time.time()
print("Loading NEODatabase takes " + str(end - start) + " seconds.")

neo = neodb.get_neo_by_name("Halley")
print(neo)
neo.show_approaches()

neo = neodb.get_neo_by_designation("100004")
print(neo)
neo.show_approaches(limit=3)


