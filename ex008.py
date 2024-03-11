met = float(input('Uma distância em metros: '))
print(f"""
A medida de {met}m corresponde a:
{met * 10**-3}km
{met * 10**-2}hm
{met * 10**-1}dam
{met * 10**1}dm
{met * 10**2}cm
{met * 10**3}mm
""")
