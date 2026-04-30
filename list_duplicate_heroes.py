from clean_data import df_heroes_clean

print(df_heroes_clean[df_heroes_clean.duplicated(['name'])])