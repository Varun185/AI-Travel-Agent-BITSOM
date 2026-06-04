class BookingAgent:

    DESTINATION_OPTIONS = {

        "Goa": [

            {
                "mode": "Flight",
                "provider": "IndiGo",
                "price": 5500,
                "duration": "1 hr 15 min"
            },

            {
                "mode": "Train",
                "provider": "Tejas Express",
                "price": 1800,
                "duration": "8 hrs"
            },

            {
                "mode": "Bus",
                "provider": "VRL Travels",
                "price": 1200,
                "duration": "10 hrs"
            }
        ],

        "Manali": [

            {
                "mode": "Flight",
                "provider": "Alliance Air",
                "price": 8500,
                "duration": "2 hrs"
            },

            {
                "mode": "Volvo Bus",
                "provider": "HRTC Volvo",
                "price": 1500,
                "duration": "11 hrs"
            }
        ],

        "Jaipur": [

            {
                "mode": "Flight",
                "provider": "IndiGo",
                "price": 6000,
                "duration": "1 hr 45 min"
            },

            {
                "mode": "Train",
                "provider": "Vande Bharat",
                "price": 1200,
                "duration": "4 hrs"
            }
        ],

        "Dubai": [

            {
                "mode": "Flight",
                "provider": "Emirates",
                "price": 22000,
                "duration": "3 hrs"
            },

            {
                "mode": "Flight",
                "provider": "Air India",
                "price": 20000,
                "duration": "3 hr 30 min"
            }
        ],

        "Bali": [

            {
                "mode": "Flight",
                "provider": "Singapore Airlines",
                "price": 35000,
                "duration": "9 hrs"
            },

            {
                "mode": "Flight",
                "provider": "Malaysia Airlines",
                "price": 32000,
                "duration": "10 hrs"
            }
        ]

    }

    CITY_MULTIPLIER = {

        "Mumbai": 1.00,
        "Delhi": 1.05,
        "Bangalore": 1.10,
        "Chennai": 1.08,
        "Hyderabad": 1.07,
        "Pune": 0.95
    }

    def recommend(self, source, destination):

        options = self.DESTINATION_OPTIONS.get(
            destination,
            []
        )

        multiplier = self.CITY_MULTIPLIER.get(
            source,
            1.0
        )

        recommendations = []

        for option in options:

            new_option = option.copy()

            new_option["price"] = int(
                option["price"] * multiplier
            )

            recommendations.append(
                new_option
            )

        return recommendations