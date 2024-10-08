import pandas as pd
import matplotlib.pyplot as plt

# Veriyi yükle
data_path = 'data/processed/train_with_dominance_score.csv'  # Dominasyon skoru eklenmiş veri seti
df = pd.read_csv(data_path)

# Görselleştirmek istediğimiz takımlar
teams = ['Man City', 'Liverpool', 'Chelsea', 'Tottenham', 'Arsenal', 'Man United']

# Her takım için çizgi grafiği
plt.figure(figsize=(10, 6))

# Renkleri tanımla (her takım için farklı renk)
team_colors = {
    'Man City': 'blue',
    'Liverpool': 'red',
    'Chelsea': 'green',
    'Tottenham': 'purple',
    'Arsenal': 'orange',
    'Man United': 'pink'
}

# Her takımın ev sahibi olduğu maçlardaki HomePPG değerini çiz
for team in teams:
    team_data = df[df['HomeTeam'] == team]  # Takımın ev sahibi olduğu maçları al
    plt.plot(team_data.index, team_data['HomePPG'], label=team, color=team_colors[team])

# Grafik başlıkları ve etiketler
plt.title('Ev Sahibi Takimlarin HomePPG Degerleri')
plt.xlabel('Mac Sirasi')
plt.ylabel('HomePPG')

# Efsane (legend) ekleyelim
plt.legend()

# Grafik gösterimi
plt.grid(True)
plt.show()
