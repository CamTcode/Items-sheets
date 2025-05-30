import csv
from collections import Counter

# Read inventory file
with open("inventory.txt", "r") as f:
    items = [line.strip() for line in f if line.strip()]

# Count each item
inventory_count = Counter(items)

# Write to Excel-style CSV file
with open("inventory_output.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Item Name", "Quantity"])  # Header
    for item, count in inventory_count.items():
        writer.writerow([item, count])

print("Inventory exported to inventory_output.csv")
