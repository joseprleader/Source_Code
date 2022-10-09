# Module 4 of PY4E: Conditional Statements Exercise 3.3

# Enter 0.85 as the score to complete the challenge.

score = float(input("Enter Score: "))

if score < 0 and score > 1.0:
    print("Error, Score out of range.")

elif score >= 0.9:
    print("A")

elif score >= 0.8:
    print("B")

elif score >= 0.7:
    print("C")

elif score >= 0.6:
    print("D")

else:
    print("F")
