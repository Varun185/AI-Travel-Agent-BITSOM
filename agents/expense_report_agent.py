import random
from datetime import datetime

class ExpenseReportAgent:

    def export(self,trip):

        report=f"""
        ===== Expense Report =====
        Destination: {trip['destination']}
        Total Cost: ₹{trip['price']}
        Risk Level: {trip['risk_band']}
        """

        return report