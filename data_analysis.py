import pandas as pd
import matplotlib.pyplot as plt

from djinni.config import STACK_LIST, LANGUAGE

df = pd.read_csv("vacancies.csv").dropna(subset=["stack"])

for tech in STACK_LIST:
    df[tech] = df["stack"].apply(lambda x: 1 if tech in x else 0)

df["DRF"] = df[["Django Rest Framework", "DRF"]].max(axis=1)

tech_counts = df[STACK_LIST].sum().sort_values(ascending=False).head(26)

plt.figure(figsize=(14, 9))
tech_counts.plot(kind='bar', color="skyblue")
plt.title(f"Amount of {LANGUAGE} vacancies for each technology")
plt.xlabel("Technologies")
plt.ylabel("Vacancies")
plt.show()
