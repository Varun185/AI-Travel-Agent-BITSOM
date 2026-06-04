from agents.demand_agent import DemandAgent
from agents.risk_agent import RiskAgent
from agents.pricing_agent import PricingAgent
from agents.package_agent import PackageAgent
from agents.booking_agent import BookingAgent
from agents.hidden_gem_agent import HiddenGemAgent
from agents.expense_agent import ExpenseAgent
from agents.amenity_agent import AmenityAgent
from agents.calendar_agent import CalendarAgent
from agents.expense_report_agent import ExpenseReportAgent


class PlannerAgent:

    def __init__(self):

        self.demand_agent = DemandAgent()
        self.risk_agent = RiskAgent()
        self.pricing_agent = PricingAgent()
        self.package_agent = PackageAgent()
        self.booking_agent = BookingAgent()
        self.hidden_gem_agent = HiddenGemAgent()
        self.expense_agent = ExpenseAgent()
        self.amenity_agent = AmenityAgent()
        self.calendar_agent = CalendarAgent()
        self.expense_report_agent = ExpenseReportAgent()

    def plan_trip(self, user_request):

        demand_data = self.demand_agent.evaluate(
            user_request
        )

        risk_data = self.risk_agent.evaluate(
            user_request,
            demand_data
        )

        pricing_data = self.pricing_agent.optimize(
            user_request,
            demand_data,
            risk_data
        )

        itinerary = self.package_agent.generate(
            user_request
        )
        
        booking_options = self.booking_agent.recommend(
            user_request.source_city,
            user_request.destination
        )
        
        persona_features = {}

        if user_request.persona == "Solo":

            persona_features["hidden_gem"] = (
                self.hidden_gem_agent.recommend(
                    user_request.destination
                )
            )

        elif user_request.persona == "Group":

            persona_features["expense_split"] = (
                self.expense_agent.split_cost(
                    pricing_data["optimized_price"],
                    user_request.group_size
                )
            )

        elif user_request.persona == "Family":

            persona_features["family_hotels"] = (
                self.amenity_agent.filter_family_hotels(
                    user_request.destination
                )
            )

        elif user_request.persona == "Business":

            persona_features["calendar"] = (
                self.calendar_agent.sync(
                    user_request.travel_date
                )
            )

        trip = {

            "destination":
                user_request.destination,

            "persona":
                user_request.persona,

            "price":
                pricing_data["optimized_price"],

            "risk_band":
                risk_data["risk_band"],

            "risk_score":
                risk_data["risk_score"],

            "demand_score":
                demand_data["demand_score"],

            "itinerary":
                itinerary,

            "persona_features":
                persona_features,
            
            "booking_options":
                booking_options
        }

        if user_request.persona == "Business":

            trip["expense_report"] = (
                self.expense_report_agent.export(
                    trip
                )
            )

        return trip