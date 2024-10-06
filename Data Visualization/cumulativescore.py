import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = './Data/soccer18-19.csv'  
df = pd.read_csv(file_path)

# Takım listesi
teams = pd.concat([df['HomeTeam'], df['AwayTeam']]).unique()

# Takımların haftalık puanlarını tutacak bir dictionary
points_dict = {team: [0] * 38 for team in teams}

# Maç sonuçlarına göre puan hesaplama
for i, row in df.iterrows():
    # Ev sahibi ve deplasman takımlarının haftasını bul
    week = (i // 10) + 1  # Her hafta 10 maç olduğu varsayımıyla haftayı bul

    # Maç sonucu
    if row['FTR'] == 'H':  # Ev sahibi kazandıysa
        points_dict[row['HomeTeam']][week-1] += 3
    elif row['FTR'] == 'A':  # Deplasman takımı kazandıysa
        points_dict[row['AwayTeam']][week-1] += 3
    else:  # Beraberlik durumu
        points_dict[row['HomeTeam']][week-1] += 1
        points_dict[row['AwayTeam']][week-1] += 1

# Her takım için birikimli puanlar
for team in teams:
    points_dict[team] = pd.Series(points_dict[team]).cumsum()

# Grafik ayarları
plt.figure(figsize=(14, 8))
sns.set(style="whitegrid")

# Renk paleti 
team_colors = {
    'Arsenal': 'red', 'Man City': 'blue', 'Chelsea': 'green', 'Liverpool': 'darkred',
    'Man United': 'purple', 'Tottenham': 'navy', 'Everton': 'teal', 'Leicester': 'orange',
    'Wolves': 'gold', 'West Ham': 'pink', 'Watford': 'yellow', 'Crystal Palace': 'cyan',
    'Newcastle': 'black', 'Bournemouth': 'lime', 'Burnley': 'maroon', 'Southampton': 'brown',
    'Brighton': 'lightblue', 'Huddersfield': 'lightgreen', 'Cardiff': 'lightcoral', 'Fulham': 'gray'
}

# Haftaları tanımla (1'den 38'e)
weeks = list(range(1, 39))

# Her takımın çizgi grafiği
for team, points in points_dict.items():
    plt.plot(weeks, points, label=team, color=team_colors.get(team, 'gray'))

# Başlık ve etiketler
plt.title('2018-2019 Premier League', fontsize=16)
plt.xlabel('Hafta', fontsize=12)
plt.ylabel('Puan', fontsize=12)

# Takım isimlerini göstermek için legend
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Teams", fontsize=10)
plt.tight_layout()

plt.show()
