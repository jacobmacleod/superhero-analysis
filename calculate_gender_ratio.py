from load_data import df_heroes

print(df_heroes['Gender'].value_counts() / df_heroes.shape[0] * 100)