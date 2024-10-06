import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Takımların listesi
teams = pd.concat([df['HomeTeam'], df['AwayTeam']]).unique()

# Son 5 maçlık periyod için form incelemesi
N = 5

# Her takımın son N maçtaki form durumunu hesaplayalım
team_performance = {}

for team in teams:
    # Takımın hem ev sahibi hem de deplasman olarak oynadığı tüm maçlar
    team_matches = df[(df['HomeTeam'] == team) | (df['AwayTeam'] == team)].tail(N)
    
    # Her maç için takımın kazandığını belirleyelim (Ev sahibi ve deplasman durumu)
    team_matches['Win'] = np.where(
        (team_matches['HomeTeam'] == team) & (team_matches['FTR'] == 'H') |
        (team_matches['AwayTeam'] == team) & (team_matches['FTR'] == 'A'),
        1, 0
    )
    
    # Galibiyet oranını hesaplayalım
    win_rate = team_matches['Win'].rolling(window=N, min_periods=1).mean()
    
    # Takımın performansını saklayalım
    team_performance[team] = win_rate.values


# Görselleştirme
plt.figure(figsize=(14, 10))

# Her takım için grafiği oluşturalım
for team, performance in team_performance.items():
    plt.plot(performance, label=team)

# Grafiğe bazı düzenlemeler ekleyelim
plt.title(f'Her Takim Icin Son {N} Macta Form Durumu (Galibiyet Orani)', fontsize=16)
plt.xlabel('Mac Sayisi (Son 5 Mac)', fontsize=12)
plt.ylabel('Galibiyet Orani', fontsize=12)
plt.xticks(range(N), labels=[f'Mac {i+1}' for i in range(N)], rotation=45)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)  # Legend'i sağa kaydırmak için

plt.grid(True)
plt.tight_layout()
plt.show()

