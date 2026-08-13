# ⚓ Below the Waterline
# Simple Ship Husbandry Data Check
# Idea & analysis: Wansaidon

print("⚓ BELOW THE WATERLINE")
print("What Did the Diver Find?")
print("=" * 40)

# Example made-up job record

vessel = "Vessel A"
days_since_cleaning = 180
area = "Hull"
growth = "Heavy"
cleaning_hours = 12
condition_before = 4
condition_after = 9

print("\n🤿 DIVER INSPECTION")
print(f"Vessel: {vessel}")
print(f"Area checked: {area}")
print(f"Marine growth: {growth}")
print(f"Days since last cleaning: {days_since_cleaning}")

print("\n🧹 CLEANING")
print(f"Cleaning time: {cleaning_hours} hours")

print("\n🔍 BEFORE & AFTER")
print(f"Before: {condition_before}/10")
print(f"After:  {condition_after}/10")

# Work out the change

improvement = condition_after - condition_before

print(f"Change: +{improvement} points")

print("\n" + "=" * 40)

if improvement >= 4:
    print("🟢 BIG CHANGE")
elif improvement >= 2:
    print("🟠 SOME CHANGE")
else:
    print("🔵 SMALL CHANGE")

print("\n📊 QUESTIONS TO CHECK")

questions = [
    "Does heavier growth take longer to clean?",
    "Which underwater parts need attention most often?",
    "What gets found during inspections?",
    "Which vessels normally need more work?"
]

for question in questions:
    print(f"• {question}")

print("\n" + "=" * 40)

print("One job gives us one record.")
print("Many jobs can start showing us a pattern.")

print("\n🤿 Most people see the ship from above.")
print("The diver sees the part we don't.")