FILENAME = 'Journal.txt'

def write_entry():
    entry = input("Write your journal entry: ") + '\n'
    with open(FILENAME, 'a') as file:
        file.write(entry)

def read_all():
    with open(FILENAME, 'r') as file:
        print('\nAll Journal Entries:')
        print(file.read())

def search():
    Keyword = input("Enter thr keywork you are looking: ")

    with open(FILENAME,'r') as file:
        all_lines = file.readlines()
        for line in all_lines:
            if Keyword.lower() in line.lower():
                print(line.strip())
                return
    print("no matching entries")
            


def main_menu():
    while True:
        print('\n=== File Journal Menu ===')
        print('1. Add Entry')
        print('2. Read All Entries')
        print('3. Search Entries')
        print('4. Exit')

        choices= int(input('Choose options(1-4): '))

        if choices == '1':
            write_entry()
        elif choices == '2':
            read_all()
        elif choices == '3':
            search()
        elif choices == '4':
            print("!!!GoodBye!!!")
            break
        else:
            print("invalid choice")
if __name__ == "__main__":
    main_menu()
