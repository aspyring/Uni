# ▪ The number of days spent in the hospital
# ▪ The amount of medication charges
# ▪ The amount of surgical charges
# ▪ The amount of lab fees
# ▪ The amount of physical rehabilitation charges

# If the patient is claiming their health insurance benefit, the total amount they need to pay
# after discharge is none. If the patient is a hospital staff, lab fees and physical rehabilitation
# charges are waived. If the number of stays is 30 days and more, 20% discount from the total
# charge will be applicable for the patient.
base = 350
days = int(input(f"Please enter the number of days spent in the hospital: "))
med = int(input(f"\nEnter Amount of medical charges: "))
surg = int(input(f"\nEnter the amount of surgical charges: "))
lab = int(input(f"\nEnter the amount of lab fees: "))
rehab = int(input(f"\nEnter the amount of physical rehabilitation charges: "))
staff = str.lower(input(f"\nIs the patient a hostpital staff? (Y/N): "))
if staff == 'y':
    s = 1
else:
    s = 0
health = str.lower(input(f"\nIs the patient claiming their health insurance benefit? (Y/N): "))
if health == 'y':
    h = 1
else:
    h = 0

if h == 1:
    total = 0
elif s ==1:
    total = ((base * days) + med + surg)
elif days > 30:
    total = (0.80 * ((base * days) + med + surg + lab + rehab))

print(f"\nTotal Amount for Hostpital Stay: {total}$")





