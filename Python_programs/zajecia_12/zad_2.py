def sort_file_numbers(filename):
    try:
        with open(filename, 'r') as file:
            tab = []
            for line in file.readlines():
                tab.append(int(line.strip()))
            file.close()
            tab = sorted(tab)
            with open(filename + "_sorted", 'w') as file_sorted:
                for i in tab:
                    file_sorted.write(str(i) + '\n')
                file_sorted.close()
    except Exception as e:
        print("Błąd", e)
sort_file_numbers("test.txt")


            