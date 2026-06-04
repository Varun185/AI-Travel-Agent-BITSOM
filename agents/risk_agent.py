import random
from datetime import datetime

class RiskAgent:

    def evaluate(self,user_request,demand_data):

        risk_score=0
        reasons=[]

        if not user_request.refundable:
            risk_score += 25
            reasons.append("Non refundable booking")

        if demand_data["crowd_level"]=="High":
            risk_score += 20
            reasons.append("Peak season")

        if user_request.group_size>4:
            risk_score += 10
            reasons.append("Large group coordination")

        persona=user_request.persona_profile

        if persona["risk_tolerance"]=="low":
           risk_score += 10
           reasons.append(
               "Risk-sensitive traveller"
           )
           
        if persona["risk_tolerance"]=="very_low":
            risk_score += 15
            reasons.append(
               "Very risk-sensitive traveller"
           )
            
        if risk_score >= 60:
            band="High"
        elif risk_score >= 30:
            band="Medium"
        else:
            band="Low"

        return {"risk_score":risk_score,"risk_band":band,"reasons":reasons}