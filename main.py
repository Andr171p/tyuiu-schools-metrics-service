import pandas as pd
import numpy as np
from datetime import datetime
import asyncio
from src.database.services.school import SchoolService
from src.database.models.school import School
from src.database.models.applicant import Applicant
from src.database.services.applicant import ApplicantService
from src import utils


school_service = SchoolService()

applicant_service = ApplicantService()

# df = pd.read_csv(r"C:\Users\andre\SchoolsMetricsService\data\schools 2019-2024.csv")
'''df = df.dropna(subset=["Законченное образ. учреждение"])
schools = []
for _, row in df.iterrows():
    # print(row)
    if row["Город образ. учреждения"] is not np.nan:
        schools.append(School(name=row["Законченное образ. учреждение"], city=row["Город образ. учреждения"]))
    else:
        schools.append(School(name=row["Законченное образ. учреждение"], city=None))

# print(schools)
asyncio.run(school_service.add_schools(schools=schools))'''

df = pd.read_csv(r"C:\Users\andre\SchoolsMetricsService\data\applicants 2019-2024.csv")
print(df.columns)
df['Ср. балл док-та об образовании'] = df['Ср. балл док-та об образовании'].fillna(0)
df['Общая сумма баллов'] = df['Общая сумма баллов'].fillna(0)
df['Дата рождения'] = df['Дата рождения'].apply(lambda x: utils.get_date_from_str(x))

for _, row in df.iterrows():
    school_id = row['school_id']
    if row['Олимпиады'] is not np.nan:
        applicant = Applicant(
            full_name=row['ФИО'],
            gender=row['Пол'],
            bdate=row['Дата рождения'],
            gpa=row['Ср. балл док-та об образовании'],
            score=row['Общая сумма баллов'],
            olympiads=row['Олимпиады']
        )
    else:
        applicant = Applicant(
            full_name=row['ФИО'],
            gender=row['Пол'],
            bdate=row['Дата рождения'],
            gpa=row['Ср. балл док-та об образовании'],
            score=row['Общая сумма баллов'],
            olympiads=None
        )
    asyncio.run(applicant_service.add_applicant_by_school_id(
        school_id=school_id,
        applicant=applicant
    ))


'''s = asyncio.run(school_service.get_school_with_applicants(id=4))
print(s.applicants)'''
