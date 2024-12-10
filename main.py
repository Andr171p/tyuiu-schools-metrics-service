import pandas as pd
from pathlib import Path
from typing import List


def load_csv_data(path: str | Path) -> pd.DataFrame:
    return pd.read_csv(path)


def group_by_schools(
        data: pd.DataFrame,
        feature: str = "Законченное образ. учреждение"
) -> List[pd.DataFrame]:
    return [group for _, group in data.groupby(feature)]


def get_schools(
        data: pd.DataFrame,
        feature: str = "Законченное образ. учреждение"
) -> List[str]:
    return list(data[feature].unique())


def process_school(school: str) -> str:
    return ''.join(school.split('(')[0])


df = pd.read_csv(r"C:\Users\andre\EducationService\data\processed 2019-2024.csv")
unique_schools = df["Законченное образ. учреждение"].unique().tolist()
schools_df = pd.DataFrame(
    {
        "school_id": range(len(unique_schools)),
        "name": unique_schools
    }
)
df["school_id"] = df["Законченное образ. учреждение"].map({inst: idx for idx, inst in enumerate(schools_df['name'])})
applicants_df = df.drop(columns=['Законченное образ. учреждение']).copy()
print(applicants_df)