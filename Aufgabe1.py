with open("text.txt", "r") as file:
    for row in file.readlines():
        row_data = row.split(",")
        print(f"{row_data[0]} is {row_data[1]} and {row_data[2]}")
