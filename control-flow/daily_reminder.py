task = input("Enter the task for the reminder: ")
priority = input("Enter the priority level (high/medium/low): ")
time_bound = input("Enter the time bound (yes/no): ")

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