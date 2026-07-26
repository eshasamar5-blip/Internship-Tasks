import pandas as pd
import numpy as np
df=pd.read_csv("database.csv")
print ("Orignal Database=\n")
print (df)

df.fillna(df.mean(numeric_only=True), inplace=True)
print(df.isnull().sum())
df.drop_duplicates(inplace=True)
subjects=["Python","Maths","Physics","Chemistry","Biology"]
for subject in subjects:
    df[subject]=df[subject].clip(0,100)

    df["Average"]=df[subjects].mean(axis=1)

    df["Result"]= np.where(df["Average"]>=40, "Pass","Fail")
    topper =(
        df.loc[df["Average"].idxmax()])
    lowest =(
        df.loc[df["Average"].idxmin()])
    print("\nSubject Statics")

    for subject in subjects :
        print(f"\n{subject}")
        print("Mean:",np.mean(df[subject]), "\n")
        print("Median:",np.median(df[subject]), "\n")
        print("Standard Deviation:",np.std(df[subject]), "\n")
        print("\n Summary")
        print("Total Students:",len(df))
        print("Passed:",(df["Result"]=="Pass").sum())
        print("Failed:",(df["Result"]=="Fail").sum())
        print ("Subject-wise class average:")
        print(df[subjects].mean())
        print("Topper")
        print(topper)
        print ("Needs Assistance")
        print(lowest)
        df=df.sort_values(by="Average", ascending=False)
        print (" Final Database")
        print(df)
         


























    # df.fillna(df.mean(numeric_only=True),inplace=True),