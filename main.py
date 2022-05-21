from utils import array_to_number, number_to_array

if __name__ == '__main__':
    numbers = input('write numbers, separated by commas: ')
    numbers = [int(number) for number in numbers.strip().split(',')]
    print('unique number : ', array_to_number(numbers))
    ascii_code = input('write ASCII code: ')
    print('array: ', number_to_array(ascii_code))
