from load_data import df_heroes

genders = ['-']

filtered_df = df_heroes[df_heroes['Gender'].isin(genders)]

filtered_df[["name", "Publisher"]]

print(f"There are {filtered_df.shape[0]} superheroes with no gender listed.")