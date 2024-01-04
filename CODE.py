# Currency exchange rates as of a specific date
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.94,
    'JPY': 149.72,
    'GBP': 0.82,
    'CAD': 1.36,
    'AUD': 1.57,
    'CHF': 0.90,
    'CNY': 7.31,
    'INR': 83.24,
    'BRL': 5.02,
    'ZAR': 18.74,
    'RUB': 97.78,
    'MXN': 17.94,
    'SGD': 1.37,
    'KRW': 1354.19,
    'NZD': 1.69,
    'SEK': 10.91,
    'NOK':10.96,
    'HKD': 7.82,
    'SAR': 3.75,
    'AED': 3.67,
    'ARS': 350.04,
    'TRY': 27.92,
    'IDR': 15718.05,
    'MYR': 4.74,
    'THB': 36.33,
    'EGP': 30.90,
    'ILS': 4.02,
    'CLP': 946.10
}

# Create a dictionary for full and short currency names
currency_names = {
    'USD': 'United States Dollar',
    'EUR': 'Euro',
    'JPY': 'Japanese Yen',
    'GBP': 'British Pound Sterling',
    'CAD': 'Canadian Dollar',
    'AUD': 'Australian Dollar',
    'CHF': 'Swiss Franc',
    'CNY': 'Chinese Yuan Renminbi',
    'INR': 'Indian Rupee',
    'BRL': 'Brazilian Real',
    'ZAR': 'South African Rand',
    'RUB': 'Russian Ruble',
    'MXN': 'Mexican Peso',
    'SGD': 'Singapore Dollar',
    'KRW': 'South Korean Won',
    'NZD': 'New Zealand Dollar',
    'SEK': 'Swedish Krona',
    'NOK': 'Norwegian Krone',
    'HKD': 'Hong Kong Dollar',
    'SAR': 'Saudi Riyal',
    'AED': 'UAE Dirham',
    'ARS': 'Argentine Peso',
    'TRY': 'Turkish Lira',
    'IDR': 'Indonesian Rupiah',
    'MYR': 'Malaysian Ringgit',
    'THB': 'Thai Baht',
    'EGP': 'Egyptian Pound',
    'ILS': 'Israeli New Shekel',
    'CLP': 'Chilean Peso'
}

# Display a menu for the user with full names and short forms
print("Available Currencies:")
for short_form, full_name in currency_names.items():
    print(f"- {full_name} ({short_form})")

from_currency = input("Enter the currency code you have: ").upper()
to_currency = input("Enter the currency code you want to convert to: ").upper()

# Check if the currencies are in the exchange rate dictionary
if from_currency in exchange_rates and to_currency in exchange_rates:
    amount = float(input(f"Enter the amount in {currency_names[from_currency]} ({from_currency}): "))
    converted_amount = amount * (exchange_rates[to_currency] / exchange_rates[from_currency])
    print(f"{amount} {currency_names[from_currency]} ({from_currency}) is equal to {converted_amount} {currency_names[to_currency]} ({to_currency})")
else:
    print("Currency not found in the exchange rates.")


'WRITE A LINE BY LINE TEXT EXPLAINATION OF THE ABOVE CODE'
