import myfitnesspal

client = myfitnesspal.Client("shiv213")

day = client.get_date(2022, 3, 21)

print(day)
print(day.exercises[0][0])
