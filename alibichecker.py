name = input("")
alloc = input("")
altime = input("")
critime = input("")
criloc = input("")

if criloc == alloc:
    validity = "Alibi status: Invalid"
elif critime != altime:
    validity = "Alibi status: Invalid"
else:
    validity = "Alibi status: Valid"

print(f"Suspect name: {name}")
print(f"Location of alibi: {alloc}")
print(f"Time of alibi: {altime}")
print(f"Time of crime: {critime}")
print(f"Location of crime: {criloc}")
print(f"\n{validity}")
