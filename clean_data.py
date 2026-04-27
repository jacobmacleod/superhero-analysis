from load_data import df_heroes

df_heroes_clean = df_heroes.copy(deep = True)
df_heroes_clean.drop(columns = ['Unnamed: 0','Height','Weight'], inplace = True)