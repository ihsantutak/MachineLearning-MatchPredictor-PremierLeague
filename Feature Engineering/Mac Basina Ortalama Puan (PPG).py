import pandas as pd

# Veriyi yükle
data_path = 'data/processed/train_with_datetime.csv'
df = pd.read_csv(data_path)

# Tarih formatının doğru olduğunu kontrol et ve sıralama yap
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# Takımların her biri için toplam puanları ve maç sayıları tutan bir sözlük
team_stats = {team: {'TotalHomePoints': 0, 'HomeGames': 0, 'TotalAwayPoints': 0, 'AwayGames': 0} for team in pd.concat([df['HomeTeam'], df['AwayTeam']]).unique()}

# PPG listeleri
home_ppg = []
away_ppg = []

# Her maç için PPG'yi hesapla
for i, row in df.iterrows():
    home_team = row['HomeTeam']
    away_team = row['AwayTeam']

    # Maçtan önce mevcut ev sahibi ve deplasman takımının PPG'sini hesapla
    # Ev sahibi PPG (ev sahibi maçlarından kazandığı toplam puan / ev sahibi maç sayısı)
    if team_stats[home_team]['HomeGames'] > 0:
        home_ppg_value = team_stats[home_team]['TotalHomePoints'] / team_stats[home_team]['HomeGames']
    else:
        home_ppg_value = 0
    home_ppg.append(home_ppg_value)
    
    # Deplasman PPG (deplasman maçlarından kazandığı toplam puan / deplasman maç sayısı)
    if team_stats[away_team]['AwayGames'] > 0:
        away_ppg_value = team_stats[away_team]['TotalAwayPoints'] / team_stats[away_team]['AwayGames']
    else:
        away_ppg_value = 0
    away_ppg.append(away_ppg_value)

    # Maç sonuçlarına göre puanları güncelle (bu güncelleme sonraki maç için geçerli olacak)
    if row['FTR'] == 'H':  # Ev sahibi kazandı
        team_stats[home_team]['TotalHomePoints'] += 3
    elif row['FTR'] == 'D':  # Beraberlik
        team_stats[home_team]['TotalHomePoints'] += 1
        team_stats[away_team]['TotalAwayPoints'] += 1
    elif row['FTR'] == 'A':  # Deplasman kazandı
        team_stats[away_team]['TotalAwayPoints'] += 3

    # Maç sayısını güncelle (bu da sonraki maç için geçerli olacak)
    team_stats[home_team]['HomeGames'] += 1
    team_stats[away_team]['AwayGames'] += 1

# Hesaplanan HomePPG ve AwayPPG değerlerini veri setine ekle
df['HomePPG'] = home_ppg
df['AwayPPG'] = away_ppg

# Güncellenmiş veri setini kaydet
df.to_csv('data/processed/train_with_ppg_fixed.csv', index=False)

print("HomePPG ve AwayPPG başarıyla hesaplandı ve veri setine eklendi.")
