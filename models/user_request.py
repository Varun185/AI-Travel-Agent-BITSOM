from config.persona_data import PERSONAS


class UserRequest:

    def __init__(
        self,
        persona,
        source_city,
        destination,
        budget,
        duration,
        group_size,
        travel_date,
        refundable=False
    ):

        self.persona = persona
        self.source_city = source_city
        self.destination = destination
        self.budget = budget
        self.duration = duration
        self.group_size = group_size
        self.travel_date = travel_date
        self.refundable = refundable

        self.persona_profile = PERSONAS.get(
            persona,
            {}
        )

    def to_dict(self):

        return {

            "persona": self.persona,
            "source_city": self.source_city,
            "destination": self.destination,
            "budget": self.budget,
            "duration": self.duration,
            "group_size": self.group_size,
            "travel_date": self.travel_date,
            "refundable": self.refundable
        }

    def __str__(self):

        return (
            f"Persona={self.persona}, "
            f"Source={self.source_city}, "
            f"Destination={self.destination}, "
            f"Budget={self.budget}, "
            f"Duration={self.duration}, "
            f"Group Size={self.group_size}"
        )