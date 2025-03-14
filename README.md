# Ad Campaign Budget Management System

A Python implementation for managing advertising campaigns with daily/monthly budgets and operational hours.

## Getting Started

### Prerequisites
- Python 3.6 or newer
- Basic terminal/command line knowledge

### Installation
1. **Copy Files**  
   Place these in an empty directory:
   - `ad_agency.py` (core system)
   - `test_simulation.py` (sample simulation)

2. **Verify Python**  
   ```bash
   python3 --version
   ```

##  Running the Sample

```bash
python3 test_simulation.py
```

**What This Does**:
- Creates a brand with $100 daily budget
- Sets up a campaign running 9AM-5PM
- Simulates 48 hours of activity
- Shows hourly status updates

## Sample Output
```
Hour 08: Campaign active? False | Daily spend: 0.0
Hour 09: Campaign active? True  | Daily spend: 12.5
Hour 10: Campaign active? True  | Daily spend: 25.0
...
Hour 16: Campaign active? True  | Daily spend: 100.0 (Budget reached)
Hour 17: Campaign active? False | Daily spend: 100.0
...
Hour 00: Campaign active? False | Daily spend: 0.0 (Daily reset)
```

##  Configuration Guide

### 1. Create a Brand
```python
from ad_agency import Brand

# Daily budget: $150, Monthly budget: $4500
my_brand = Brand("CoolSneakers", 150, 4500)
```

### 2. Add Campaigns
```python
from ad_agency import Campaign

# Runs 8AM-8PM (20:00) with $10/hour spend
campaign = Campaign(
    my_brand,
    "Summer Sale",
    hourly_spend=10,
    dayparting=range(8, 20)
)
```

### 3. Run Simulation
```python
from ad_agency import Simulation

sim = Simulation([my_brand])  # Add all brands here

# Simulate 1 week (168 hours)
for _ in range(168):
    sim.simulate_hour()
```

## ⚙️ System Behavior

### Key Features
- **Automatic Shutoff**  
  Campaigns disable immediately when hitting budget limits

- **Smart Reactivation**  
  Campaigns re-enable at midnight/dayparting hours if budget allows

- **Time-Aware**  
  - Daily resets at midnight
  - Monthly resets on 1st of month
  - 24-hour time format

### Budget Priority
1. Monthly budget
2. Daily budget
3. Dayparting schedule


