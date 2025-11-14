task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

message = ""

match priority:
    case 'high':
        message = f"'{task}' is a high priority task"
    case 'medium':
        message = f"'{task}' is a medium priority task"
    case 'low':
        message = f"'{task}' is a low priority task. Consider completing it when you have free time."
    
reminder = ""

if time_bound == 'yes' and priority in ['high', 'medium']:
    
    reminder = message + " is a high priority task that requires immediate attention today!"

print(reminder)
print(message)