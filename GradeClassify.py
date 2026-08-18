# grade_classifier.py
"""
Simple grade classifier that collects three subject marks and prints a report card.
This version adds robust input handling so the script exits gracefully on
KeyboardInterrupt/EOFError and re-prompts on invalid numeric input.
"""
import sys


def get_input(prompt: str) -> str:
    """Get a string input from the user. Exit cleanly on interrupt or EOF."""
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\nInput cancelled. Exiting.")
        sys.exit(1)


def get_float(prompt: str) -> float:
    """Prompt until a valid float is entered. Exit on interrupt/EOF."""
    while True:
        try:
            value = get_input(prompt)
            return float(value)
        except ValueError:
            print("Invalid number. Please enter a numeric value.")
        except SystemExit:
            # propagate exit from get_input
            raise


def main() -> None:
    name = get_input("Enter learner name: ")
    mark1 = get_float("Enter Subject 1 mark: ")
    mark2 = get_float("Enter Subject 2 mark: ")
    mark3 = get_float("Enter Subject 3 mark: ")

    average = (mark1 + mark2 + mark3) / 3

    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    status = "Pass" if average >= 50 else "Fail"
    intervention = (
        "Needs Intervention" if (mark1 < 40 or mark2 < 40 or mark3 < 40) else "No Intervention Required"
    )

    print("\n" + "=" * 40)
    print("      STUDENT REPORT CARD")
    print("=" * 40)
    print(f"Learner Name : {name}")
    print(f"Subject 1    : {mark1:.2f}")
    print(f"Subject 2    : {mark2:.2f}")
    print(f"Subject 3    : {mark3:.2f}")
    print(f"Average      : {average:.2f}")
    print(f"Grade        : {grade}")
    print(f"Status       : {status}")
    print(f"Intervention : {intervention}")
    print("=" * 40)


if __name__ == "__main__":
    main()
