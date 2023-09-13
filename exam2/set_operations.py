# set_operations.py

specs1 = {"core", "ram", "cpu"}
specs2 = {"ram", "bios", "cpu", "os"}

# Write the missing set operations on the four lines below (Replace None)
set_operation_1 = set.union(specs1, specs2)
set_operation_2 = set.intersection(specs1, specs2)
set_operation_3 = set.difference(specs1, specs2)
set_operation_4 = specs1.symmetric_difference(specs2)

if __name__ == '__main__':
    print(f"Set operation 1: {set_operation_1}")
    print(f"Set operation 2: {set_operation_2}")
    print(f"Set operation 3: {set_operation_3}")
    print(f"Set operation 4: {set_operation_4}")