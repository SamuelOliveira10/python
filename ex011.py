larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print(f"""
Sua parede tem a dimensão de {larg}x{alt} e sua área é de {area}m².
Para pintar essa parede, você precisará de {area/2}L de tinta.
""")
