def sum_of_squares(x):
    total = 0
    while x > 0:
        total += pow(x % 10, 2)
        x = int(x / 10)
    return total
    
def is_happy(x):
    sequence = []
    while x != 1:
        sequence.append(x)
        x = sum_of_squares(x)
        if x in sequence:
            return False
    return True

def task_one():
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))
    happy_list = []
    count = 0
    for i in range(start_range, end_range + 1):
        if is_happy(i):
            happy_list.append(i)
            count += 1
    print(happy_list)
    print("Count: ", count)
    print("Max: ", max(happy_list) if happy_list else 0)
    print("Percentage: ", str(round(count / (end_range + 1 - start_range) * 100, 2)) + "%")

task_one()
