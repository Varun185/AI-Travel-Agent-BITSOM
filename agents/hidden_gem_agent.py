import random
from datetime import datetime
from config.hidden_gems import HIDDEN_GEMS

class HiddenGemAgent:

    def recommend(self,destination):

        gems=HIDDEN_GEMS.get(destination,[])

        if len(gems)>0:
            return random.choice(gems)

        return "No hidden gems available"