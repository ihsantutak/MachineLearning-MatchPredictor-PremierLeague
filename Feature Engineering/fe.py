import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Verinin ilk 370 satırı (son 10 satır tahmin verisi)
file_path = './Data/soccer18-19.csv'  
df = pd.read_csv(file_path).iloc[:370]

# Ev sahibi galibiyet, mağlubiyet, beraberlik
home_wins = len(df[df['FTR'] == 'H'])
away_wins = len(df[df['FTR'] == 'A'])
draws = len(df[df['FTR'] == 'D'])

print(f"Ev sahibi galibiyeti: {home_wins}, Deplasman galibiyeti: {away_wins}, Beraberlik: {draws}")

# Galibiyet, mağlubiyet ve beraberlik verileri
categories = ['Ev Sahibi Galibiyeti', 'Deplasman Galibiyeti', 'Beraberlik']
counts = [home_wins, away_wins, draws]

# Görselleştirme
plt.figure(figsize=(8, 6))
sns.barplot(x=categories, y=counts, palette='viridis')
plt.title('Toplam Galibiyet, Maglubiyet ve Beraberlik Sayilari')
plt.ylabel('Sayi')
plt.xlabel('Kategori')
plt.show()



# Ev sahibi ve deplasman için toplam atılan/yenen goller
home_goals_scored = df['FTHG'].sum()
home_goals_conceded = df['FTAG'].sum()

away_goals_scored = df['FTAG'].sum()
away_goals_conceded = df['FTHG'].sum()

print(f"Ev sahibi atilan goller: {home_goals_scored}, Ev sahibi yenilen goller: {home_goals_conceded}")
print(f"Deplasman atilan goller: {away_goals_scored}, Deplasman yenilen goller: {away_goals_conceded}")

# Toplam atılan ve yenilen goller
categories = ['Ev Sahibi', 'Deplasman']
goals_scored = [home_goals_scored, away_goals_scored]  # Atılan goller
goals_conceded = [home_goals_conceded, away_goals_conceded]  # Yenilen goller

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Barların genişliğini ve pozisyonlarını ayarlamak indeks
barWidth = 0.35  # Barların genişliği
r1 = np.arange(len(categories))  # İlk bar grubu için pozisyonlar (ev sahibi)
r2 = [x + barWidth for x in r1]  # İkinci bar grubu için pozisyonlar (deplasman)

# Görselleştirme
plt.figure(figsize=(8, 6))

# Atılan goller
plt.bar(r1, goals_scored, color='blue', width=barWidth, edgecolor='grey', label='Atilan Goller')

# Yenilen goller
plt.bar(r2, goals_conceded, color='red', width=barWidth, edgecolor='grey', label='Yenilen Goller')

# Grafiği düzenleme
plt.xlabel('Takim', fontweight='bold')
plt.xticks([r + barWidth/2 for r in range(len(categories))], categories)  # X eksenine kategorileri ekle
plt.ylabel('Gol Sayisi')
plt.title('Ev Sahibi ve Deplasman Atilan/Yenilen Goller')
plt.legend()

plt.show()


# Ev sahibi avantajı
home_advantage = home_wins / len(df) * 100
away_advantage = away_wins / len(df) * 100

print(f"Ev sahibi avantaji: %{home_advantage:.2f}")
print(f"Deplasman avantaji: %{away_advantage:.2f}")

# Avantaj verileri
categories = ['Ev Sahibi Avantaj', 'Deplasman Avantaj']
advantage = [home_advantage, away_advantage]

# Görselleştirme
plt.figure(figsize=(8, 6))
sns.barplot(x=categories, y=advantage, palette='coolwarm')
plt.title('Ev Sahibi ve Deplasman Avantaji(%)')
plt.ylabel('Avantaj (%)')
plt.xlabel('Takim Turu')
plt.ylim(0, 100)  # Oranları %0 ile %100 arasında sınırlamak için
plt.show()






# Gol averajı (Atılan goller - yenilen goller)
home_goal_difference = home_goals_scored - home_goals_conceded
away_goal_difference = away_goals_scored - away_goals_conceded

print(f"Ev sahibi gol averaji: {home_goal_difference}")
print(f"Deplasman gol averaji: {away_goal_difference}")

# Gol averajı verileri
categories = ['Ev Sahibi Gol Averaji', 'Deplasman Gol Averaji']
goal_difference = [home_goal_difference, away_goal_difference]

# Görselleştirme
plt.figure(figsize=(8, 6))
sns.barplot(x=categories, y=goal_difference, palette='Blues')
plt.title('Ev Sahibi ve Deplasman Gol Averaji')
plt.ylabel('Gol Averaji')
plt.xlabel('Takim Turu')
plt.axhline(0, color='black', linewidth=1)  # Sıfır çizgisi
plt.show()
