# ⚓ Below the Waterline
# Simple Ship Hull Maintenance Analysis
# Idea & analysis: Wansaidon

print("⚓ BELOW THE WATERLINE")
print("Ship Hull Maintenance Check")
print("=" * 40)

# Example made-up maintenance data
vessel = "Vessel A"
days_since_cleaning = 180
growth_level = "Heavy"
cleaning_hours = 12
condition_before = 4
condition_after = 9

print("\n🚢 VESSEL")
print(vessel)

print("\n📊 MAINTENANCE RECORD")
print(f"Days since last cleaning: {days_since_cleaning}")
print(f"Marine growth: {growth_level}")
print(f"Cleaning time: {cleaning_hours} hours")

print("\n🔍 CONDITION")
print(f"Before cleaning: {condition_before}/10")
print(f"After cleaning:  {condition_after}/10")

# Work out the improvement
improvement = condition_after - condition_before

print(f"Improvement: +{improvement} points")

print("\n" + "=" * 40)

# Simple result
if improvement >= 4:
    print("🟢 BIG CHANGE")
    print("The recorded condition improved a lot after cleaning.")

elif improvement >= 2:
    print("🟠 SOME CHANGE")
    print("The recorded condition improved after cleaning.")

else:
    print("🔵 SMALL CHANGE")
    print("Only a small change was recorded.")

print("\n🔍 QUESTIONS TO EXPLORE")

questions = [
    "Does heavier growth mean longer cleaning time?",
    "Which parts of ships need cleaning most often?",
    "Does waiting longer lead to more marine growth?",
    "Which vessel types take longer to clean?",
    "What problems appear most often during inspection?"
]

for question in questions:
    print(f"• {question}")

print("\n" + "=" * 40)

print("One vessel tells us a story.")
print("Many vessels can show us a pattern.")

print("\n⚓ The data can help tell us")
print("what's happening below the waterline.")