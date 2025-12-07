"""Digital Wellbeing & Productivity Analysis
Analyzes correlations between sleep, screen time, weather, caffeine, and productivity
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

class WellbeingAnalyzer:
    def __init__(self, data_path='wellbeing_productivity_data.csv'):
        """Initialize analyzer with data"""
        self.df = pd.read_csv(data_path)
        self.df['date'] = pd.to_datetime(self.df['date'])
        
    def basic_statistics(self):
        """Generate basic statistical summary"""
        print("=" * 60)
        print("DIGITAL WELLBEING & PRODUCTIVITY ANALYSIS")
        print("=" * 60)
        print(f"\nAnalysis Period: {self.df['date'].min().date()} to {self.df['date'].max().date()}")
        print(f"Total Days Analyzed: {len(self.df)}")
        
        print("\n" + "=" * 60)
        print("SLEEP PATTERNS")
        print("=" * 60)
        print(f"Average Sleep: {self.df['sleep_hours'].mean():.2f} hours")
        print(f"Average Sleep Quality: {self.df['sleep_quality'].mean():.2f}/10")
        print(f"Best Sleep Day: {self.df.loc[self.df['sleep_hours'].idxmax(), 'day_of_week']}")
        
        print("\n" + "=" * 60)
        print("SCREEN TIME ANALYSIS")
        print("=" * 60)
        print(f"Average Total Screen Time: {self.df['total_screen_time'].mean():.2f} hours/day")
        print(f"Average Social Media: {self.df['social_media_hours'].mean():.2f} hours/day")
        print(f"Average Work Apps: {self.df['work_app_hours'].mean():.2f} hours/day")
        print(f"Average Entertainment: {self.df['entertainment_hours'].mean():.2f} hours/day")
        
        print("\n" + "=" * 60)
        print("PRODUCTIVITY METRICS")
        print("=" * 60)
        print(f"Average Productivity Score: {self.df['productivity_score'].mean():.2f}/100")
        print(f"Average Tasks Completed: {self.df['tasks_completed'].mean():.2f} tasks/day")
        print(f"Average Focus Time: {self.df['focus_time_minutes'].mean():.2f} minutes/day")
        print(f"Average Mood Score: {self.df['mood_score'].mean():.2f}/10")
        
        print("\n" + "=" * 60)
        print("LIFESTYLE FACTORS")
        print("=" * 60)
        print(f"Average Caffeine Intake: {self.df['caffeine_cups'].mean():.2f} cups/day")
        print(f"Most Common Weather: {self.df['weather'].mode()[0]}")
        
    def correlation_analysis(self):
        """Analyze correlations between variables"""
        print("\n" + "=" * 60)
        print("KEY CORRELATIONS")
        print("=" * 60)
        
        # Focus on key correlations
        factors = ['sleep_hours', 'sleep_quality', 'caffeine_cups', 
                  'social_media_hours', 'total_screen_time']
        outcomes = ['productivity_score', 'mood_score', 'focus_time_minutes']
        
        for outcome in outcomes:
            print(f"\n{outcome.replace('_', ' ').title()}:")
            for factor in factors:
                corr = self.df[factor].corr(self.df[outcome])
                print(f"  vs {factor.replace('_', ' ').title()}: {corr:+.3f}")
    
    def day_of_week_analysis(self):
        """Analyze patterns by day of week"""
        print("\n" + "=" * 60)
        print("DAY OF WEEK PATTERNS")
        print("=" * 60)
        
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_stats = self.df.groupby('day_of_week')[['productivity_score', 'sleep_hours', 'mood_score']].mean()
        day_stats = day_stats.reindex(day_order)
        
        print("\nAverage Productivity by Day:")
        for day, score in day_stats['productivity_score'].items():
            print(f"  {day:10s}: {score:.2f}")
            
    def weather_impact(self):
        """Analyze weather impact on productivity"""
        print("\n" + "=" * 60)
        print("WEATHER IMPACT ANALYSIS")
        print("=" * 60)
        
        weather_stats = self.df.groupby('weather')[['productivity_score', 'mood_score']].mean().sort_values('productivity_score', ascending=False)
        
        print("\nProductivity by Weather:")
        for weather, row in weather_stats.iterrows():
            print(f"  {weather:10s}: Productivity={row['productivity_score']:.2f}, Mood={row['mood_score']:.2f}")
    
    def generate_insights(self):
        """Generate actionable insights"""
        print("\n" + "=" * 60)
        print("KEY INSIGHTS & RECOMMENDATIONS")
        print("=" * 60)
        
        # Sleep vs Productivity
        sleep_prod_corr = self.df['sleep_hours'].corr(self.df['productivity_score'])
        if sleep_prod_corr > 0.3:
            print("\n✓ SLEEP: Strong positive correlation with productivity.")
            print(f"  Recommendation: Maintain {self.df[self.df['productivity_score'] > self.df['productivity_score'].quantile(0.75)]['sleep_hours'].mean():.1f}+ hours of sleep")
        
        # Screen time impact
        social_media_corr = self.df['social_media_hours'].corr(self.df['productivity_score'])
        if social_media_corr < -0.2:
            print("\n✓ SOCIAL MEDIA: Negative impact on productivity detected.")
            print(f"  Recommendation: Limit to {self.df[self.df['productivity_score'] > self.df['productivity_score'].quantile(0.75)]['social_media_hours'].mean():.1f} hours/day")
        
        # Caffeine sweet spot
        caffeine_groups = self.df.groupby('caffeine_cups')['productivity_score'].mean()
        optimal_caffeine = caffeine_groups.idxmax()
        print(f"\n✓ CAFFEINE: Optimal intake appears to be {optimal_caffeine} cups/day")
        print(f"  Current average: {self.df['caffeine_cups'].mean():.1f} cups/day")
        
        # Best productivity day
        best_day = self.df.groupby('day_of_week')['productivity_score'].mean().idxmax()
        print(f"\n✓ TIMING: {best_day} shows highest productivity")
        print("  Recommendation: Schedule important tasks on this day")
        
if __name__ == "__main__":
    # Run analysis
    analyzer = WellbeingAnalyzer()
    
    analyzer.basic_statistics()
    analyzer.correlation_analysis()
    analyzer.day_of_week_analysis()
    analyzer.weather_impact()
    analyzer.generate_insights()
    
    print("\n" + "=" * 60)
    print("Analysis complete! Run generate_wellbeing_data.py first to create dataset.")
    print("=" * 60)
