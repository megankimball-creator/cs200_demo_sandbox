def make_list():
    nums = []
    print('Enter numbers one at a time. Enter 0 to stop.')
    x = int(input('num:'))
    while x != 0:
        nums.append(x)
        x = int(input('num:'))
        print('You added', len(nums), 'numbers.')
    return nums

def choices(data):
    print('Here is the data:')
    print(data)

    choice = ''
    while True:
        choice = input('Select an option. 1-sum  2-min  3-max  4-quit')
        if choice == '1':
            print('The sum is',sum(data))
        elif choice == '2':
            print('The min is', min(data) )
        elif choice == '3':
            print('The max is', max(data))
        elif choice == '4':
            print('Goodbye')
            return
        else:
            print('Please choose 1-4')

def main():
    print("Welcome")
    data = make_list()
    choices(data)

if __name__ == "__main__":
    main()