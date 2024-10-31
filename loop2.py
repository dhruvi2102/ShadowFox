
total_jumping_jacks = 100
completed_jumping_jacks = 0


while completed_jumping_jacks < total_jumping_jacks:
    completed_jumping_jacks += 10
    print(f"Completed {completed_jumping_jacks} jumping jacks.")
  
    tired = input("Are you tired? (yes/y or no/n): ").strip().lower()
    
    if tired in ["yes", "y"]:
 
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()
        
        if skip in ["yes", "y"]:
            
            print(f"You completed a total of {completed_jumping_jacks} jumping jacks.")
            break
    elif tired not in ["no", "n"]:
       
        print("Invalid input, please answer 'yes' or 'no'.")
        continue
    
    if completed_jumping_jacks >= total_jumping_jacks:
        print("Congratulations! You completed the workout.")
    else:
        
        remaining = total_jumping_jacks - completed_jumping_jacks
        print(f"{remaining} jumping jacks remaining.")
