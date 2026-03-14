def main():
    a,b,c = 100,70,90
    average = calculate_averages(a,b,c)
    grade = determine_grade(average)
    report = print_report(grade)

    print("Averages:", average)
    print("Grade:", grade)
    print("Status:", report)

def calculate_averages(a,b,c):
    return (a+b+c)/3

def determine_grade(average_score):
    grade = ""
    if average_score>=90:
        grade = "A"
    elif average_score >=80:
        grade = "B"
    elif average_score >= 70:
        grade = "C"
    elif average_score >= 60:
        grade = "D"
    else:
        grade = "E"
    return grade

def print_report(grade):
    if grade == "A" or grade == "B" or grade == "C":
        return "Pass"
    elif grade == "D":
        return "Just Pass"
    else:
        return "Fail" 

if __name__ == "__main__":
    main()