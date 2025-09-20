task = input("Enter your task: ")
priority = input("priority (high/medium/low): ")
time_bound = input("is it time bound ? (yes/no): ")

match priority:
	case "high":
		print(f"Reminder: {task} (Priority: HIGH)")
	case "medium":
		print(f"Reminder: {task} (Priority: MEDIUM)")
	case "low":
		print(f"Reminder: {task} (Priority: LOW)")
	case _:
		print(f"Reminder: {task} (Priority: UNKNOWN)")
		
if time_bound == "yes":
    due_time = input("Enter the due time :")
    print(f"This task is time-bound and should be completed by {due_time}.")