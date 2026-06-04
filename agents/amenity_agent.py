import random
from datetime import datetime
from config.hotels import HOTELS

class AmenityAgent:

    def filter_family_hotels(self,destination):

        results=[]

        for hotel in HOTELS:

            if hotel["destination"]==destination and hotel["family_friendly"]:
                results.append(hotel["name"])

        return results