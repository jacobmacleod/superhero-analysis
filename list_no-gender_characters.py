from load_data import df_heroes

genders = ['-']

filtered_df = df_heroes[df_heroes['Gender'].isin(genders)]

print(filtered_df[["name", "Publisher"]])