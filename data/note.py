import pandas as pd


df = pd.read_csv("processed 2019-2024.csv")

unique_schools = df[['Законченное образ. учреждение', 'Город образ. учреждения']].drop_duplicates()

# Присваиваем каждому образовательному учреждению уникальный ID
unique_schools['school_id'] = range(1, len(unique_schools) + 1)

# Датафрейм со школами
schools_df = unique_schools[['school_id', 'Законченное образ. учреждение', 'Город образ. учреждения']]
# schools_df.to_csv("schools 2019-2024.csv")

df_with_school_ids = df.merge(
    unique_schools[['Законченное образ. учреждение', 'school_id']],
    on='Законченное образ. учреждение',
    how='left'
)

# Датафрейм с абитуриентами
applicants_df = df_with_school_ids.drop(columns=['Законченное образ. учреждение', 'Город образ. учреждения'])
print(applicants_df.shape)
# Присваиваем каждому абитуриенту уникальный ID
# print(applicants_df.columns)

unique_applicants = applicants_df[[
    'ФИО', 'Пол', 'Дата рождения', 'Мобильный телефон', 'E-mail', 'Адрес регистрации', 'Ср. балл док-та об образовании',
    'Общая сумма баллов', 'Олимпиады', 'school_id']].drop_duplicates()
unique_applicants['applicants_id'] = range(1, len(unique_applicants) + 1)
unique_applicants.to_csv("applicants 2019-2024.csv")
direction_df = applicants_df.merge(
    unique_applicants[['applicants_id', 'ФИО']],
    on="ФИО",
    how="left"
)
print(unique_applicants.shape)
print(direction_df.columns)
direction_df = direction_df.drop(['Unnamed: 0', 'ФИО', 'Пол', 'Дата рождения', 'Мобильный телефон',
       'E-mail', 'Адрес регистрации', 'Ср. балл док-та об образовании',
       'Общая сумма баллов', 'Олимпиады', 'school_id'], axis=1)
print(direction_df)
direction_df.to_csv("directions 2019-2024.csv")
