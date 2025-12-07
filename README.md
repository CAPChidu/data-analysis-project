# Digital Wellbeing & Productivity Analysis

## Overview

A unique data analysis project examining the intricate relationships between **digital wellbeing factors** and **productivity metrics**. This project goes beyond traditional productivity analysis by incorporating holistic lifestyle factors including sleep patterns, screen time across different app categories, weather conditions, and caffeine intake.

### What Makes This Project Unique?

While most data analysis projects focus on business metrics or popular datasets (Titanic, Iris, etc.), this project:
- **Analyzes the intersection of health and productivity** in the digital age
- **Combines multiple lifestyle factors** rarely studied together
- **Provides actionable insights** for optimizing personal productivity
- **Uses synthetic but realistic data** modeling real-world correlations
- **Focuses on modern digital wellbeing challenges** (screen time, social media impact)

## Project Features

### Data Generation
- **90 days of synthetic wellbeing data** with realistic correlations
- **15 variables** tracking sleep, screen time, productivity, weather, mood, and more
- Probabilistic modeling reflecting real-world patterns

### Comprehensive Analysis
- **Statistical summaries** of all key metrics
- **Correlation analysis** between lifestyle factors and productivity
- **Day-of-week patterns** revealing temporal productivity trends
- **Weather impact analysis** on mood and performance
- **Actionable insights** with personalized recommendations

### Variables Tracked

**Sleep Metrics:**
- Hours of sleep (4-10 hours)
- Sleep quality score (1-10)

**Screen Time (Hours):**
- Social media usage
- Work applications
- Entertainment apps
- Total screen time

**Productivity Indicators:**
- Daily tasks completed
- Focus time (minutes)
- Productivity score (0-100)

**Lifestyle Factors:**
- Caffeine intake (cups per day)
- Weather conditions
- Temperature
- Day of week
- Mood score (1-10)

## Installation

1. **Clone this repository:**
```bash
git clone https://github.com/CAPChidu/data-analysis-project.git
cd data-analysis-project
```

2. **Install required packages:**
```bash
pip install -r requirements.txt
```

## Usage

### Step 1: Generate the Dataset
```bash
python generate_wellbeing_data.py
```
This creates `wellbeing_productivity_data.csv` with 90 days of synthetic data.

### Step 2: Run the Analysis
```bash
python analyze_wellbeing.py
```
This performs comprehensive analysis and displays:
- Basic statistics
- Correlation analyses
- Day-of-week patterns
- Weather impact
- Personalized insights and recommendations

## Key Insights

The analysis reveals interesting patterns such as:

- **Sleep Quality**: Strong positive correlation with productivity
- **Social Media**: Negative impact on focus time and task completion
- **Caffeine**: Optimal intake levels for peak productivity  
- **Weather**: Sunny days correlate with better mood and performance
- **Weekly Patterns**: Productivity varies significantly by day of week

## Project Structure

```
data-analysis-project/
├── README.md                       # Project documentation
├── requirements.txt                # Python dependencies
├── generate_wellbeing_data.py      # Data generation script
├── analyze_wellbeing.py            # Main analysis script
└── wellbeing_productivity_data.csv # Generated dataset (after running script)
```

## Technologies Used

- **Python 3.8+**
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **matplotlib** - Data visualization
- **seaborn** - Statistical visualizations
- **scipy** - Statistical analysis
- **scikit-learn** - Machine learning utilities

## Future Enhancements

- [ ] Add interactive visualizations with Plotly
- [ ] Implement time-series forecasting models
- [ ] Create a dashboard using Streamlit or Dash
- [ ] Add clustering analysis to identify productivity patterns
- [ ] Include exercise and nutrition tracking
- [ ] Build a recommendation system for optimal daily routines

## Why This Project Matters

In our increasingly digital world, understanding the relationship between our digital habits and productivity is crucial. This project:

1. **Demonstrates data science skills** applicable to health tech and wellness industries
2. **Shows ability to work with multidimensional data**
3. **Provides real-world value** through actionable insights
4. **Explores a growing field** of digital wellbeing research

## Contributing

Feel free to fork this project and adapt it for your own wellbeing analysis! Suggestions for improvements are welcome.

## License

This project is open source and available for educational and personal use.

## Author

**Chidghana** - [GitHub Profile](https://github.com/CAPChidu)

---

*This project was created as a unique portfolio piece demonstrating data analysis skills with real-world applications in the digital wellbeing space.*
