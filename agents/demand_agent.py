import random
from datetime import datetime

class DemandAgent:

    HIGH_THRESHOLD = 0.75
    MEDIUM_THRESHOLD = 0.50

    SEASONALITY_TABLE = {

        "Goa": {
            1:0.8,2:0.7,3:0.6,4:0.5,5:0.4,6:0.6,
            7:0.7,8:0.6,9:0.5,10:0.7,11:0.9,12:0.95
        },

        "Manali": {
            1:0.9,2:0.8,3:0.6,4:0.5,5:0.7,6:0.8,
            7:0.6,8:0.5,9:0.4,10:0.6,11:0.7,12:0.9
        }

    }

    def evaluate(self, user_request):

        try:

            month = datetime.strptime(
                user_request.travel_date,
                "%Y-%m-%d"
            ).month

        except Exception:

            month = 6

        score = self.SEASONALITY_TABLE.get(
            user_request.destination,
            {}
        ).get(month, 0.5)

        if score > self.HIGH_THRESHOLD:
            crowd = "High"

        elif score > self.MEDIUM_THRESHOLD:
            crowd = "Medium"

        else:
            crowd = "Low"

        return {
            "demand_score": round(score, 2),
            "crowd_level": crowd
        }