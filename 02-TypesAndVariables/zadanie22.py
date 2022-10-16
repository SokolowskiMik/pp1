Amount = 15.84
print(f'Amount : {Amount} zł')
VAT = 0.23 * Amount
formatted_string = "{:.2f}".format(VAT)
float_VAT = float(formatted_string)
print(f'VAT 23% : {float_VAT} zł')