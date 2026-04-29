from load_data import df_heroes

print(df_heroes[df_heroes.duplicated(['name'])])