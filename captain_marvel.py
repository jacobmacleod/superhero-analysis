from clean_data import df_heroes_clean

names = ["Captain Marvel"]

print(df_heroes_clean[df_heroes_clean['name'].isin(names)])