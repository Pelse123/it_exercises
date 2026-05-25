zdanie = input()
print(len(zdanie.split()))
print(zdanie.upper())
slowo = "python"
if zdanie.lower().find(slowo.lower()) != -1:
    print(zdanie.lower().find(slowo.lower()))
else:
    print("nie wystepuje")
print(zdanie.lstrip().rstrip())

