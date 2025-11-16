subject = ["Java", "C++", "C#", "Node"]
print(subject)
print(subject[0])
print(subject[1:])
print("Java" in subject)
# Add Item in list
print(subject + ["Swift", "Kotlin"])
print(len(subject))
# Add last
subject.append("Toc")
print(subject)
# Add Specific Index
subject.insert(2, "Flutter")
print(subject)
subject.remove("Flutter")
print(subject)
# Sorting
subject.sort()
print(subject)
# Reverse
subject.reverse()
print(subject)
# Remove last item
subject.pop()
print(subject)
# count , copy, clear
