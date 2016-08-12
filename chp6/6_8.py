number = int(raw_input('Please input a number between 1 to 1000: ... '))

units = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens_units = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

print 'The number you input is: '

if 0 <= number <= 9:
    print units[number]
elif 10 <= number <= 19:
    print tens_units[number - 10]
elif 20 <= number <= 99:
    if number % 10 == 0:
        print tens[number / 10 - 2]
    else:
        print '%s-%s' % (tens[number / 10 - 2], units[number % 10])
elif 100 <= number <= 999:
    if number % 100 == 0:
        print '%s hundred' % (units[number / 100])
    elif number % 10 == 0 and (number - 100 * (number / 100)) != 10:
        print '%s hundred and %s' % (units[number / 100], tens[(number - 100 * (number / 100))/10 - 2])
    elif number % 10 == 0 and (number - 100 * (number / 100)) == 10:
        print '%s hundred and ten' % (units[number / 100])
    elif number % 10 != 0 and 20 < (number - 100 * (number / 100))<= 99:
        print '%s hundred and %s-%s' % (units[number / 100], tens[(number - 100 * (number / 100)) / 10 - 2], units[number - 10 * (number / 10)])
    elif number % 10 != 0 and 10 < (number - 100 * (number / 100))< 20:
        print '%s hundred and %s' % (units[number / 100], tens_units[number - 100 * (number / 100) - 10])
    elif number % 10 != 0 and 0 < (number - 10 * (number / 10)) < 10:
        print '%s hundred and %s' % (units[number / 100], units[number - 10 * (number / 10)])
else: print 'ten hundred'