drug_inventory = ['Paracetamol', 'Amoxicillin 500mg',
'Ampiclox 500mg', 'Ampiclox 250mg', 'Erythromycin 250mg',
'Erythromycin 500mg', 'Amlodipine 5mg', 'Amlodipine 10mg',
'Lisinopril 5mg', 'Lisinopril 10mg', 'Vitamin - E', 'Vitamin A'
]
# List unpacking
anti_biotic, vitamins, act, * drug_inventory2 = ['Paracetamol', 'Amoxicillin 500mg',
'Ampiclox 500mg', 'Ampiclox 250mg', 'Erythromycin 250mg',
'Erythromycin 500mg', 'Amlodipine 5mg', 'Amlodipine 10mg',
'Lisinopril 5mg', 'Lisinopril 10mg', 'Vitamin - E', 'Vitamin A'
]
print(anti_biotic)
print(vitamins)
print(act)
print(drug_inventory2)



# drug_inventory[11] = 'Vitamin B'
print(drug_inventory)
drug_inventory.sort()

import string
alpha = list(string.ascii_uppercase)
print(alpha)
print(len(alpha))
print(alpha[21])

name = ' '.join(['Assalam\'alaikum, ' ' My Name Is Abdallah!'])
print(name)

drug_price = {
'Paracetamol': 120,
'Amoxicillin': 450,
'Vitamin': 200,
'Antibiotic': 650
}

print(drug_price.keys())

print(drug_price.values())

print(drug_price.items())

drug_price2 = drug_price.copy()

print(drug_price2)

print(drug_price2.clear())
#print(drug_price['Paracetamol'])
print(drug_price.get('Antibiotic',500))

print(type(drug_price))


my_turple = (1,2,3,4,5)

print(type(my_turple))


my_list = [1,2,3,4,5,5]

my_set = set(my_list)

print(my_set)

is_old = True
is_licenced = True

if is_old:
    print('You are old enough to drive!')
elif is_old and is_licenced:
    print('Good to go')
else:
    print('You are not qualify to drive')

you_know_him = False
grant_access = 'Allow Access and Entertain Him or Her' if you_know_him else 'Do not Allow Access'
print(grant_access)

is_magician = False
is_expert = True

for i in 'Items':
    print(i)
