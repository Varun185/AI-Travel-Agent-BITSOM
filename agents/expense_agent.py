import random
from datetime import datetime

class ExpenseAgent:

    def split_cost(self,total_cost,group_size):

        per_person=total_cost/group_size

        ledger={}

        for i in range(group_size):
            ledger[f"Member_{i+1}"]=per_person

        return ledger