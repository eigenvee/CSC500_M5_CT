earnings_table = [[2, 5], [4, 15], [6, 30], [8, 60]]
MIN_PURCHASE = 0
EARNINGS = 1

print()
print('CSU Book Club points calculator.')
print('Calculates points earned on purchases made during one calendar '
      'month.\n')

while(True):
    user_input = input('Enter the number of books purchased this month '
                       '(or "q" to quit): ')
    if user_input == 'q':
        break
    num_books = int(user_input)

    earned_points = 0

    for brkpoint in earnings_table:
        if num_books < brkpoint[MIN_PURCHASE]:
            break
        earned_points = brkpoint[EARNINGS]

    print("You've earned {} CSU Book Club points this month.\n"
          .format(earned_points))
