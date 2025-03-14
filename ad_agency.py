import datetime

class Brand:
    def __init__(self, name, daily_budget, monthly_budget):
        self.name = name
        self.daily_budget = daily_budget
        self.monthly_budget = monthly_budget
        self.daily_spend = 0.0
        self.monthly_spend = 0.0
        self.campaigns = []
        self.is_active = True

    def add_spend(self, amount):
        self.daily_spend += amount
        self.monthly_spend += amount

    def check_budgets(self):
        if (self.daily_spend >= self.daily_budget or 
            self.monthly_spend >= self.monthly_budget):
            self.is_active = False
            for campaign in self.campaigns:
                campaign.is_active = False
        else:
            self.is_active = True

    def reset_daily(self):
        self.daily_spend = 0.0
        self.check_budgets()

    def reset_monthly(self):
        self.monthly_spend = 0.0
        self.daily_spend = 0.0
        self.check_budgets()

class Campaign:
    def __init__(self, brand, name, hourly_spend, dayparting):
        self.brand = brand
        self.name = name
        self.hourly_spend = hourly_spend
        self.dayparting = dayparting
        self.is_active = False

    def update_status(self, current_hour):
        if self.brand.is_active and current_hour in self.dayparting:
            self.is_active = True
        else:
            self.is_active = False

class Simulation:
    def __init__(self, brands):
        self.brands = brands
        # Set fixed start time for testing (8 AM)
        self.current_time = datetime.datetime(2024, 1, 1, 8, 0)

    def advance_time(self, hours=1):
        new_time = self.current_time + datetime.timedelta(hours=hours)
        
        # Check for day change
        if new_time.date() != self.current_time.date():
            for brand in self.brands:
                brand.reset_daily()
        
        # Check for month change
        if new_time.month != self.current_time.month:
            for brand in self.brands:
                brand.reset_monthly()
        
        self.current_time = new_time

    def simulate_hour(self):
        # Process current hour first
        current_hour = self.current_time.hour
        
        # Update campaigns and accumulate spend
        for brand in self.brands:
            for campaign in brand.campaigns:
                campaign.update_status(current_hour)
                if campaign.is_active:
                    brand.add_spend(campaign.hourly_spend)
            brand.check_budgets()
        
        # Advance time after processing
        self.advance_time(1) 