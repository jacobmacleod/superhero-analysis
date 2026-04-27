import kagglehub
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("claudiodavi/superhero-set")

df_heroes = pd.read_csv(f"{path}/heroes_information.csv")
df_powers = pd.read_csv(f"{path}/super_hero_powers.csv")