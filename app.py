import streamlit as st
import pandas as pd
import plotly.express as px

from config.hotels import HOTELS
from planner_agent import PlannerAgent
from models.user_request import UserRequest

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="SmartTrip",
    page_icon="✈️",
    layout="wide"
)

planner = PlannerAgent()

# =====================================
# SIDEBAR
# =====================================

st.sidebar.header("Travel Preferences")

persona = st.sidebar.selectbox(
    "Traveller Type",
    ["Solo", "Family", "Group", "Business"]
)

source_city = st.sidebar.selectbox(
    "Departure City",
    [
        "Mumbai",
        "Delhi",
        "Bangalore",
        "Chennai",
        "Hyderabad",
        "Pune"
    ]
)

destination = st.sidebar.selectbox(
    "Destination",
    [
        "Goa",
        "Manali",
        "Jaipur",
        "Dubai",
        "Bali"
    ]
)

budget = st.sidebar.number_input(
    "Budget",
    min_value=5000,
    value=50000
)

duration = st.sidebar.slider(
    "Trip Duration (Days)",
    2,
    10,
    5
)

group_size = st.sidebar.slider(
    "Group Size",
    1,
    10,
    4
)

travel_date = st.sidebar.date_input(
    "Travel Date"
)

refundable = st.sidebar.checkbox(
    "Refundable Booking",
    value=False
)

generate = st.sidebar.button(
    "Generate Smart Plan"
)

# =====================================
# GENERATE PLAN
# =====================================

if generate:

    request = UserRequest(

        persona=persona,

        source_city=source_city,

        destination=destination,

        budget=budget,

        duration=duration,

        group_size=group_size,

        travel_date=str(travel_date),

        refundable=refundable
    )

    trip = planner.plan_trip(request)

    st.success("Trip Generated Successfully!")

    # =====================================
    # KPI CARDS
    # =====================================

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Demand Score",
            trip["demand_score"]
        )

    with c2:
        st.metric(
            "Risk Band",
            trip["risk_band"]
        )

    with c3:
        st.metric(
            "Estimated Cost",
            f"₹{trip['price']:,}"
        )

    st.divider()

    # =====================================
    # COST BREAKDOWN
    # =====================================

    st.subheader("💰 Cost Breakdown")

    cost_df = pd.DataFrame({

        "Category": [
            "Flights",
            "Hotel",
            "Activities",
            "Food"
        ],

        "Cost": [
            trip["price"] * 0.30,
            trip["price"] * 0.40,
            trip["price"] * 0.20,
            trip["price"] * 0.10
        ]

    })

    fig = px.pie(
        cost_df,
        names="Category",
        values="Cost",
        hole=0.5,
        title="Trip Cost Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # =====================================
    # TRANSPORT OPTIONS
    # =====================================

    st.subheader(
        "✈🚆 Recommended Transport Options"
    )

    for option in trip["booking_options"]:

        st.info(
            f"""
Mode: {option['mode']}

Provider: {option['provider']}

Price: ₹{option['price']}

Duration: {option['duration']}
"""
        )

    st.divider()

    # =====================================
    # HOTEL RECOMMENDATIONS
    # =====================================

    st.subheader(
        "🏨 Recommended Hotels"
    )

    for hotel in HOTELS:

        if hotel["destination"] == destination:

            st.success(
                hotel["name"]
            )

    st.divider()

    # =====================================
    # ITINERARY
    # =====================================

    st.subheader("📅 Smart Itinerary")

    st.code(
        trip["itinerary"]
    )

    st.divider()

    # =====================================
    # RISK ANALYSIS
    # =====================================

    st.subheader("⚠ Risk Analysis")

    st.write(
        f"Risk Score: {trip['risk_score']}"
    )

    st.write(
        f"Risk Band: {trip['risk_band']}"
    )

    st.divider()

    # =====================================
    # RAW OUTPUT
    # =====================================

    with st.expander(
        "View Complete Agent Output"
    ):
        st.json(trip)