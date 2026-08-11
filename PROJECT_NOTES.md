# Below the Waterline — My Notes

## What is it?

This project looks at ship hull cleaning and maintenance.

The question is:

**What can the maintenance records tell us?**

---

## What does my Python do?

It uses example information about:

- Days since cleaning
- Marine growth
- Cleaning time
- Condition before cleaning
- Condition after cleaning

It then checks how much the condition changed.

---

## Simple Example

**Before cleaning:** 4/10  
**After cleaning:** 9/10

`9 - 4 = 5`

Result:

🟢 **BIG CHANGE**

---

## How does it work?

`if` → Checks how big the change is.

`elif` → Checks another result if the first one doesn't match.

`else` → Uses the final result if neither matches.

---

## Important

The numbers and ratings are examples, not real vessel data.

---

## One-Sentence Explanation

> **"I used Python to compare a ship's condition before and after cleaning and show how much it changed."**
