import pandas as pd

# Veriyi yükle
df = pd.read_csv('data/processed/train_with_ppg_fixed.csv')

# Takımların geçmiş performanslarını takip etmek için bir dictionary (sözlük) oluştur
team_stats = {team: {'TotalHomePoints': 0, 'HomeGames': 0, 'TotalAwayPoints': 0, 'AwayGames': 0,
                     'TotalHomeGoals': 0, 'TotalAwayGoals': 0} 
              for team in pd.concat([df['HomeTeam'], df['AwayTeam']]).unique()}

# Hesaplanacak değişkenler için boş listeler
home_form_points = []
away_form_points = []
home_form_goals = []
away_form_goals = []

# Her maçı iterasyondan geçirerek özellikleri hesapla
for i, row in df.iterrows():
    home_team = row['HomeTeam']
    away_team = row['AwayTeam']

    # HomeFormPoints ve AwayFormPoints
    home_form_points_value = team_stats[home_team]['TotalHomePoints']
    away_form_points_value = team_stats[away_team]['TotalAwayPoints']
    
    home_form_points.append(home_form_points_value)
    away_form_points.append(away_form_points_value)

    # HomeFormGoals ve AwayFormGoals
    home_form_goals_value = team_stats[home_team]['TotalHomeGoals']
    away_form_goals_value = team_stats[away_team]['TotalAwayGoals']
    
    home_form_goals.append(home_form_goals_value)
    away_form_goals.append(away_form_goals_value)

    # Maç sonucuna göre puanları güncelle
    if row['FTR'] == 'H':  # Ev sahibi kazandı
        team_stats[home_team]['TotalHomePoints'] += 3
    elif row['FTR'] == 'D':  # Beraberlik
        team_stats[home_team]['TotalHomePoints'] += 1
        team_stats[away_team]['TotalAwayPoints'] += 1
    elif row['FTR'] == 'A':  # Deplasman kazandı
        team_stats[away_team]['TotalAwayPoints'] += 3

    # Maçtaki gol sayıları ile toplam gol sayısını güncelle
    team_stats[home_team]['TotalHomeGoals'] += row['FTHG']  # Full Time Home Goals
    team_stats[away_team]['TotalAwayGoals'] += row['FTAG']  # Full Time Away Goals

    # Maç sayısı güncellenir
    team_stats[home_team]['HomeGames'] += 1
    team_stats[away_team]['AwayGames'] += 1

# Veri setine hesaplanan özellikleri ekle
df['HomeFormPoints'] = home_form_points
df['AwayFormPoints'] = away_form_points
df['HomeFormGoals'] = home_form_goals
df['AwayFormGoals'] = away_form_goals

# Güncellenmiş veriyi kaydet
df.to_csv('data/processed/train_with_form_updated.csv', index=False)
