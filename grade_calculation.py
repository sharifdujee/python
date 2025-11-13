mark = int(input("Enter marks"))

if mark >= 80:
    print("The Grade is A+")
elif mark >= 70:
    print("The Grade is A")
elif mark >= 60:
    print("The Grade is A -")
elif mark >= 50:
    print("The Grade is B")
elif mark >= 40:
    print("The Grade is C")
elif mark >= 33:
    print("The Grade is D")

else:
    print(f"Failed Best of Luck Next Time {mark}")

print("Thanks for enter marks")
