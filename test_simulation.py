from ad_agency import Brand, Campaign, Simulation
import datetime

# Create brand with $100 daily budget
brand = Brand("ExampleCo", daily_budget=100, monthly_budget=3000)

# 8-hour schedule (9AM-5PM) with $12.5/hour spend
campaign = Campaign(brand, "Summer Sale", 12.5, dayparting=range(9, 17))
brand.campaigns.append(campaign)

# Initialize simulation
sim = Simulation([brand])

# Simulate 48 hours (2 days)
for _ in range(48):
    sim.simulate_hour()
    # Display the hour that just finished processing
    previous_hour = (sim.current_time - datetime.timedelta(hours=1)).hour
    print(f"Hour {previous_hour:02d}: Campaign active? {campaign.is_active} | Daily spend: {brand.daily_spend}") 