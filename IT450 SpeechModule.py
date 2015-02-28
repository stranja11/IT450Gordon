FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"
nums = [ "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" ]

def checkio(num):
    hundreds = num/100
    if num % 100 < 20:
        teen = nums[num % 100]
        if hundreds:
            if teen:
                return nums[hundreds] + " hundred " + teen
            else:
                return nums[hundreds] + " hundred"
            
        else:
            return teen
    else:
		num = num % 100
        tens = OTHER_TENS[num / 10]
        ones = nums[num % 10]
        if hundreds:
            if ones:
                return nums[hundreds] + " hundred " + tens + " " + ones
            else:
                return nums[hundreds] + " hundred " + tens
            
        else:
            if ones:
                return tens + " " + ones
            else:
                return tens

   #replace this for solution
    return 'string representation of n'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
