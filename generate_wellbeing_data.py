"""Digital Wellbeing & Productivity Data Generator
Generates synthetic data correlating sleep, screen time, productivity, weather, and caffeine intake
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

def generate_wellbeing_data(days=90):
    """Generate 90 days of digital wellbeing and productivity data"""
    
    start_date = datetime(2024, 9, 1)
    dates = [start_date + timedelta(days=i) for i in range(days)]
    
    data = []
    
    for date in dates:
        # Sleep patterns (4-10 hours)
        sleep_hours = round(np.random.normal(7, 1.2), 2)
        sleep_hours = np.clip(sleep_hours, 4, 10)
        
        # Sleep quality (1-10 scale, correlated with hours)
        sleep_quality = round(np.random.normal(sleep_hours, 1.5), 1)
        sleep_quality = np.clip(sleep_quality, 1, 10)
        
        # Weather conditions
        weather_conditions = random.choices(
            ['Sunny', 'Cloudy', 'Rainy', 'Stormy'],
            weights=[0.4, 0.3, 0.2, 0.1]
        )[0]
        
        # Temperature (Celsius)
        if weather_conditions == 'Sunny':
            temp = round(np.random.normal(25, 3), 1)
        elif weather_conditions == 'Cloudy':
            temp = round(np.random.normal(20, 2), 1)
        elif weather_conditions == 'Rainy':
            temp = round(np.random.normal(17, 2), 1)
        else:  # Stormy
            temp = round(np.random.normal(15, 3), 1)
        
        # Caffeine intake (cups of coffee)
        caffeine_cups = np.random.choice([0, 1, 2, 3, 4, 5], p=[0.05, 0.15, 0.35, 0.25, 0.15, 0.05])
        
        # Screen time (hours per category)
        social_media_hours = round(np.random.exponential(2), 2)
        work_app_hours = round(np.random.normal(5, 2), 2)
        work_app_hours = max(0, work_app_hours)
        entertainment_hours = round(np.random.gamma(2, 1.5), 2)
        
        total_screen_time = round(social_media_hours + work_app_hours + entertainment_hours, 2)
        
        # Productivity metrics (influenced by sleep and caffeine)
        base_productivity = (sleep_hours * 10) + (caffeine_cups * 5) - (social_media_hours * 3)
        tasks_completed = int(max(0, np.random.poisson(base_productivity / 10)))
        
        focus_time_minutes = int(max(0, np.random.normal(
            (sleep_quality * 30) + (caffeine_cups * 15) - (entertainment_hours * 10),
            45
        )))
        
        # Productivity score (0-100)
        productivity_score = round((
            (sleep_quality * 5) +
            (caffeine_cups * 3) +
            (focus_time_minutes / 5) -
            (social_media_hours * 5) -
            (10 if weather_conditions in ['Rainy', 'Stormy'] else 0)
        ), 1)
        productivity_score = np.clip(productivity_score, 0, 100)
        
        # Mood score (1-10, influenced by multiple factors)
        mood_score = round((
            (sleep_quality * 0.4) +
            (5 if weather_conditions == 'Sunny' else 2 if weather_conditions == 'Cloudy' else 1) +
            (productivity_score / 20) +
            np.random.normal(0, 1)
        ), 1)
        mood_score = np.clip(mood_score, 1, 10)
        
        data.append({
            'date': date.strftime('%Y-%m-%d'),
            'day_of_week': date.strftime('%A'),
            'sleep_hours': sleep_hours,
            'sleep_quality': sleep_quality,
            'weather': weather_conditions,
            'temperature_celsius': temp,
            'caffeine_cups': caffeine_cups,
            'social_media_hours': social_media_hours,
            'work_app_hours': work_app_hours,
            'entertainment_hours': entertainment_hours,
            'total_screen_time': total_screen_time,
            'tasks_completed': tasks_completed,
            'focus_time_minutes': focus_time_minutes,
            'productivity_score': productivity_score,
            'mood_score': mood_score
        })
    
    return pd.DataFrame(data)

if __name__ == "__main__":
    # Generate the dataset
    df = generate_wellbeing_data(90)
    
    # Save to CSV
    df.to_csv('wellbeing_productivity_data.csv', index=False)
    
    print("Dataset generated successfully!")
    print(f"\nDataset shape: {df.shape}")
    print(f"\nFirst few rows:")
    print(df.head())
    print(f"\nBasic statistics:")
    print(df.describe())
