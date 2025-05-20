"""
CGPA Calculator Implementation
Author: Ayuba Mathias
Course: EIE326 - Software Techniques
Topic: Python Programming
Assignment: Implementation of CGPA Calculator for Computing Cumulative Grade Point Average

This program calculates a student's Cumulative Grade Point Average (CGPA) based on
the grades received in various courses and their respective credit units. The program
provides a simple interface for inputting course details and displays the final CGPA.
"""

def grade_converter(grade):
    """
    Converts letter grades to their numerical grade point equivalents.
    
    Args:
        grade (str): The letter grade (A, B, C, D, or F)
        
    Returns:
        float: The corresponding grade point or -1.0 if invalid grade
    """
    grade_points = {
        'A': 5.0,
        'B': 4.0,
        'C': 3.0,
        'D': 2.0,
        'F': 0.0
    }
    
    return grade_points.get(grade.upper(), -1.0)


def calculate_cgpa():
    """
    Calculates CGPA based on courses, grades, and credit units input by the user.
    """
    try:
        # Get number of courses
        while True:
            try:
                num_courses = int(input("Please input the number of courses offered: "))
                if num_courses > 0:
                    break
                else:
                    print("Number of courses must be positive. Try again.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Initialize arrays for storing grades and credit units
        credit_units = []
        grades = []
        
        # Get course details
        for i in range(num_courses):
            # Get credit unit
            while True:
                try:
                    credit_unit = int(input(f"Please enter the credit unit of course {i + 1}: "))
                    if credit_unit >= 0:
                        credit_units.append(credit_unit)
                        break
                    else:
                        print("Credit unit must be positive. Try again.")
                except ValueError:
                    print("Please enter a valid number.")
            
            # Get grade
            while True:
                grade = input(f"Please enter the Grade obtained in course {i + 1} (A, B, C, D, or F): ").strip().upper()
                if grade in ['A', 'B', 'C', 'D', 'F']:
                    grades.append(grade)
                    break
                else:
                    print("Invalid grade. Please enter A, B, C, D, or F.")
        
        # Calculate CGPA
        total_grade_points = 0
        total_credit_units = 0
        
        # Display course summary
        print("\nCourse Summary:")
        print("-" * 50)
        print("Course\tCredit Unit\tGrade\tGrade Point\tQuality Point")
        print("-" * 50)
        
        for i in range(num_courses):
            grade_point = grade_converter(grades[i])
            quality_point = grade_point * credit_units[i]
            
            print(f"{i + 1}\t{credit_units[i]}\t\t{grades[i]}\t{grade_point}\t\t{quality_point}")
            
            total_grade_points += quality_point
            total_credit_units += credit_units[i]
        
        # Calculate and display CGPA
        cgpa = total_grade_points / total_credit_units
        
        print("-" * 50)
        print(f"Total Credit Units: {total_credit_units}")
        print(f"Total Quality Points: {total_grade_points}")
        print("-" * 50)
        print(f"Your CGPA is: {cgpa:.2f}")
        
    except ZeroDivisionError:
        print("Error: Total credit units cannot be zero.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    """Main function to run the CGPA calculator program"""
    print("===== CGPA Calculator Program =====")
    print("Welcome to the CGPA Calculator!")
    print("This program calculates your Cumulative Grade Point Average based on course grades and credit units.")
    
    continue_program = True
    
    while continue_program:
        calculate_cgpa()
        
        continue_choice = input("\nWould you like to calculate another CGPA? (Y/N): ").upper()
        if continue_choice != "Y":
            continue_program = False
    
    print("\nThank you for using the CGPA Calculator!")


if __name__ == "__main__":
    main()
