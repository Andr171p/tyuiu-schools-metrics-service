import pandas as pd
import asyncio
from src.database.services.school import SchoolService
from src.database.models.school import School


school_service = SchoolService()

df = pd.read_csv(r"C:\Users\andre\SchoolsMetricsService\data\schools 2019-2024.csv")
print(df["Законченное образ. учреждение"].isna().sum())
df = df.dropna(subset=["Законченное образ. учреждение"])
schools = []
for _, row in df.iterrows():
    # print(row)
    schools.append(School(name=row["Законченное образ. учреждение"], city="Город образ. учреждения"))

print(schools)
asyncio.run(school_service.add_schools(schools=schools))
