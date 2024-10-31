justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"] 

mem=len(justice_league)
print(mem)

justice_league.extend(["Batgirl","Nightwing"])
print(justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print(justice_league)

aquaman_index = justice_league.index("Aquaman")
flash_index = justice_league.index("Flash")
justice_league.remove("Superman")
justice_league.insert(aquaman_index + 1, "Superman")
print(justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(justice_league)

justice_league.sort()
print(justice_league)


new_leader = justice_league[0]
print(new_leader)
