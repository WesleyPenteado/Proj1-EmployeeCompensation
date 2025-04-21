#Instalar no terminal ydata-profiling
# pip install ydata-profiling


# pandas para ler csv e transformar em dataframe
import pandas as pd

# pandas profile (ydata_p)
from ydata_profiling import ProfileReport

df = pd.read_csv('Employee_Compensation.csv')
profile = ProfileReport(df, title="Profiling Report")
profile.to_file("output.html")
