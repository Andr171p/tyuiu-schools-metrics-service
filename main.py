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

# df = pd.read_csv(r"C:\Users\andre\SchoolsMetricsService\data\applicants 2019-2024.csv")
'''print(df.columns)
df['Ср. балл док-та об образовании'] = df['Ср. балл док-та об образовании'].fillna(0)
df['Общая сумма баллов'] = df['Общая сумма баллов'].fillna(0)
df['Дата рождения'] = df['Дата рождения'].apply(lambda x: utils.get_date_from_str(x))


async def main() -> None:
    arr = []
    for _, row in df.iterrows():
        school_id = row['school_id']
        if school_id == 21943:
            continue
        else:
            if row['Олимпиады'] is not np.nan:
                applicant = Applicant(
                    full_name=row['ФИО'],
                    gender=row['Пол'],
                    bdate=row['Дата рождения'],
                    gpa=row['Ср. балл док-та об образовании'],
                    score=row['Общая сумма баллов'],
                    olympiads=row['Олимпиады']
                )
                applicant.school_id = school_id
            else:
                applicant = Applicant(
                    full_name=row['ФИО'],
                    gender=row['Пол'],
                    bdate=row['Дата рождения'],
                    gpa=row['Ср. балл док-та об образовании'],
                    score=row['Общая сумма баллов'],
                    olympiads=None
                )
                applicant.school_id = school_id
        arr.append(applicant)
    await applicant_service.add_applicants(arr)

asyncio.run(main())'''

# df = pd.read_csv(r"C:\Users\andre\SchoolsMetricsService\data\directions 2019-2024.csv")
'''print(df.columns)
df = df.dropna(subset=['Формирующее подр.'])


from src.database.models.direction import Direction
from src.database.services.direction import DirectionService


async def main() -> None:
    arr = []
    for _, row in df.iterrows():
        applicant_id = row["applicants_id"]
        if applicant_id == 40839:
            continue
        else:
            if row['Приказ о зачислении'] is np.nan:
                direction = Direction(
                    university=row['Формирующее подр.'],
                    reception=row['Вид приема'],
                    direction=row['Направление подготовки'],
                    order=None
                )
                direction.applicant_id = applicant_id
                arr.append(direction)
            else:
                direction = Direction(
                    university=row['Формирующее подр.'],
                    reception=row['Вид приема'],
                    direction=row['Направление подготовки'],
                    order=row['Приказ о зачислении']
                )
                direction.applicant_id = applicant_id
                arr.append(direction)
    try:
        await DirectionService().add_directions(arr)
    except Exception as _ex:
        print(_ex)


asyncio.run(main())'''