# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

print("\nReminder:", end=" ")

# Process based on priority using match case
match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a high priority task. You should focus on this soon.")
    case "medium":
        if time_bound == "yes":
            print(f"'{task}' is a medium priority task that should be completed today.")
        else:
            print(f"'{task}' is a medium priority task. Try to complete it this week.")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task but has a deadline today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level entered. Please use high, medium, or low.")

print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
print("\n🚀 Click here to tweet! 🚀")
