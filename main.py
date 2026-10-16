import pandas as pd
import numpy as np

SUBJECTS = ["Machine_Learning", "Java", "Mathematics", "Operating_Systems", "Artificial_Intelligence"]

def calculate_total(row):
    return sum(row[subject] for subject in SUBJECTS)

def calculate_average(row):
    return calculate_total(row) / len(SUBJECTS)

def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    return "F"

def pass_fail(row):
    return "Pass" if calculate_average(row) >= 50 and row["Attendance"] >= 75 else "Fail"

def main():
    print("=" * 65)
    print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 65)

    df = pd.read_csv("student_data.csv")
    print("\n1. DATASET PREVIEW")
    print(df.to_string(index=False))

    totals, averages, grades, results = [], [], [], []
    for _, row in df.iterrows():
        average = calculate_average(row)
        totals.append(calculate_total(row))
        averages.append(round(average, 2))
        grades.append(assign_grade(average))
        results.append(pass_fail(row))

    df["Total"] = totals
    df["Average"] = averages
    df["Grade"] = grades
    df["Result"] = results

    print("\n2. STUDENT PERFORMANCE SUMMARY")
    print(df[["Student_ID", "Name", "Total", "Average", "Grade", "Attendance", "Result"]].to_string(index=False))

    print("\n3. OVERALL ANALYSIS")
    print("Number of students:", len(df))
    print("Class average:", round(float(np.mean(df["Average"])), 2))
    print("Highest average:", round(float(df["Average"].max()), 2))
    print("Lowest average:", round(float(df["Average"].min()), 2))
    print("Students passed:", int((df["Result"] == "Pass").sum()))
    print("Students failed:", int((df["Result"] == "Fail").sum()))

    print("\n4. SUBJECT-WISE PERFORMANCE")
    subject_means = {subject: float(np.mean(df[subject])) for subject in SUBJECTS}
    for subject, average in subject_means.items():
        print(f"{subject:15s}: {average:.2f}")
    print("Best subject:", max(subject_means, key=subject_means.get))
    print("Lowest subject average:", min(subject_means, key=subject_means.get))

    print("\n5. TOP 3 PERFORMERS")
    print(df.sort_values("Average", ascending=False).head(3)[["Student_ID", "Name", "Average", "Grade"]].to_string(index=False))

    marks = df[SUBJECTS].to_numpy()
    print("\n6. NUMPY SUMMARY")
    print("Overall marks mean:", round(float(np.mean(marks)), 2))
    print("Overall marks maximum:", int(np.max(marks)))
    print("Overall marks minimum:", int(np.min(marks)))

    df.to_csv("student_results.csv", index=False)
    print("\nAnalysis saved to: student_results.csv")
    print("=" * 65)

if __name__ == "__main__":
    main()
