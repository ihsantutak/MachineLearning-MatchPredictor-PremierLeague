# Premier League Match Outcome Prediction (Machine Learning Model)

![Premier League Logo](https://mysportsmovement.com/wp-content/uploads/2019/05/Premier-league-18-19-season-800x360.jpg)

Predict the outcomes of Premier League matches (home win, draw, away win) using machine learning with a Random Forest classifier. This project leverages historical data and feature engineering techniques to enhance predictive accuracy.

## Key Features
- ⚽ Predict Premier League match outcomes with machine learning
- 📊 Engineered features like HomePPG, AwayPPG, and Form data for more accurate predictions
- 🌲 Built and optimized using Random Forest classifier
- 🔍 Performance evaluated with confusion matrix and feature importance analysis
- 📈 Achieved 60% accuracy on unseen test data

## Understanding the Dataset and Extracting Insights 🔍

To better analyze and understand the dataset, I visualized a cumulative points table for all 20 Premier League teams throughout the 2018-2019 season. 📊 This visualization allowed us to track each team's total points on a weekly basis, providing clear insights into how their performance evolved over the season. It also highlighted performance differences between the teams, making it easier to identify trends and outliers. 🚀

![Cumulative Points Graph](https://raw.githubusercontent.com/ihsantutak/MachineLearning-MatchPredictor-PremierLeague/refs/heads/main/Data%20Visualization/2018-2019%20Premier%20League.png)


  ## Model Performance

Below is the confusion matrix for the Random Forest model, showcasing how the model performed in predicting match outcomes:

![Confusion Matrix](https://raw.githubusercontent.com/ihsantutak/MachineLearning-MatchPredictor-PremierLeague/refs/heads/main/Models/Random%20Forest/Confusion%20Matrix%20Visualization/Figure_1.png)

## Feature Importance

To understand which features had the most influence on the model's predictions, feature importance scores were calculated and visualized. This analysis revealed that **HomePPG** and **AwayPPG** played the most significant roles in determining the outcomes.

![Feature Importance Graph](https://raw.githubusercontent.com/ihsantutak/MachineLearning-MatchPredictor-PremierLeague/refs/heads/main/Models/Random%20Forest/Feature%20Importance%20Visualization/fiv.png)



## Dataset Description
The dataset used in this project contains data from 380 matches played during the 2018-2019 English Premier League season. It includes a total of 23 variables, each capturing key aspects of match outcomes and statistics. Below is a summary of the features available in the dataset:

| **Variable** | **Description**                                                                 |
|--------------|---------------------------------------------------------------------------------|
| `Div`        | The division where the match was played (Premier League)                        |
| `Date`       | The date the match was played                                                   |
| `HomeTeam`   | The home team                                                                   |
| `AwayTeam`   | The away team                                                                   |
| `FTHG`       | Full-time goals scored by the home team                                         |
| `FTAG`       | Full-time goals scored by the away team                                         |
| `FTR`        | Full-time result (Home Win, Draw, Away Win)                                     |
| `HTHG`       | Half-time goals scored by the home team                                         |
| `HTAG`       | Half-time goals scored by the away team                                         |
| `HTR`        | Half-time result (Home Win, Draw, Away Win)                                     |
| `Referee`    | The referee of the match                                                        |
| `HS`         | Number of shots taken by the home team                                          |
| `AS`         | Number of shots taken by the away team                                          |
| `HST`        | Number of shots on target by the home team                                      |
| `AST`        | Number of shots on target by the away team                                      |
| `HF`         | Number of fouls committed by the home team                                      |
| `AF`         | Number of fouls committed by the away team                                      |
| `HC`         | Number of corners taken by the home team                                        |
| `AC`         | Number of corners taken by the away team                                        |
| `HY`         | Number of yellow cards received by the home team                                |
| `AY`         | Number of yellow cards received by the away team                                |
| `HR`         | Number of red cards received by the home team                                   |
| `AR`         | Number of red cards received by the away team                                   |

## Dataset Summa
- Matches: 380
- Variables: 23
- Season: 2018-2019

## Feature Engineering

1. **HomePPG (Home Team's Average Points Per Game)**  
   - **Description**: Represents the average points earned by the home team in all of their home matches throughout the season.
   
2. **AwayPPG (Away Team's Average Points Per Game)**  
   - **Description**: Represents the average points earned by the away team in all of their away matches throughout the season.

3. **HomeFormPoints (Home Team's Points in the Last 5 Matches)**  
   - **Description**: Shows the home team's performance in terms of points earned over their last 5 home matches.

4. **AwayFormPoints (Away Team's Points in the Last 5 Away Matches)**  
   - **Description**: Indicates the away team's performance based on the points earned in their last 5 away matches.

5. **HomeFormGoals (Home Team's Goals in the Last 5 Matches)**  
   - **Description**: The total number of goals scored by the home team in their last 5 home matches. Reflects the team's attacking efficiency over a short-term period.

6. **AwayFormGoals (Away Team's Goals in the Last 5 Away Matches)**  
   - **Description**: The total number of goals scored by the away team in their last 5 away matches. Reflects the team's short-term attacking efficiency.

  ![Premier League Logo](https://images6.alphacoders.com/135/1357833.jpeg)
   



