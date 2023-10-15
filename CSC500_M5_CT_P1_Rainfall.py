MONTHS_PER_YEAR = 12
months_of_year = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November',
                  'December']
total_rainfall = 0

print('\nRainfall calculator.')
print('Calculates total and average monthly rainfall for the '
      'entered time period. ')
print()
num_years = int(input('Enter the number of years of '
                      'rainfall data to be evaluated: '))
num_months = num_years * MONTHS_PER_YEAR

for year in range(1, num_years + 1):
    print()
    for month in range(MONTHS_PER_YEAR):
        total_rainfall += float(input('Enter total rainfall in inches '
                                      'for {} of year {}: '
                                       .format(months_of_year[month], year)))

avg_monthly_rainfall = total_rainfall / num_months

print()
print('Total rainfall over the {} month period was {} inches.'
      .format(str(num_months), total_rainfall))
print('Average rainfall per month was {} inches.'
      .format(str(avg_monthly_rainfall)))
