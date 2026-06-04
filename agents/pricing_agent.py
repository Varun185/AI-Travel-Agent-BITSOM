import random
from datetime import datetime

class PricingAgent:

    BASE_PRICES={"Goa":15000,"Manali":12000}

    def optimize(self,user_request,demand_data,risk_data):

        base=self.BASE_PRICES.get(user_request.destination,10000)

        total=base*user_request.duration*user_request.group_size

        if demand_data["crowd_level"]=="High":
            total*=1.1

        if risk_data["risk_band"]=="High":
            total*=1.05

        return {"optimized_price":int(total)}