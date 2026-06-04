from config.destination_data import DESTINATIONS
import random


class PackageAgent:

    def generate(self, user_request):

        destination = DESTINATIONS[
            user_request.destination
        ]

        arrival_activity = destination[
            "arrival_activity"
        ]

        departure_activity = destination[
            "departure_activity"
        ]

        activities = destination[
            "activities"
        ].copy()

        extra_experiences = destination.get(
            "extra_experiences",
            [
                "Local Food Tour",
                "Photography Walk",
                "Shopping District Visit",
                "Cultural Experience",
                "Leisure Day"
            ]
        )

        # Prevent duplicates

        if arrival_activity in activities:
            activities.remove(
                arrival_activity
            )

        if departure_activity in activities:
            activities.remove(
                departure_activity
            )

        middle_days = max(
            0,
            user_request.duration - 2
        )

        selected_activities = []

        available = activities.copy()

        while len(selected_activities) < middle_days:

            if len(available) > 0:

                activity = random.choice(
                    available
                )

                selected_activities.append(
                    activity
                )

                available.remove(
                    activity
                )

            else:

                fallback = random.choice(
                    extra_experiences
                )

                selected_activities.append(
                    fallback
                )

        itinerary = ""

        # Day 1

        itinerary += (
            f"Day 1: Arrival + "
            f"{arrival_activity}\n"
        )

        # Middle Days

        for idx, activity in enumerate(
            selected_activities,
            start=2
        ):

            itinerary += (
                f"Day {idx}: "
                f"{activity}\n"
            )

        # Last Day

        itinerary += (
            f"Day {user_request.duration}: "
            f"{departure_activity}"
            f" + Departure\n"
        )

        return itinerary