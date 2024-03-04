msg = str(input('Digite algo: '))
print(f""" 
O tipo primitivo desse valor é {type(msg)}
Só tem espaços? {msg.isspace()}
É alfabético? {msg.isalpha()}
É um número? {msg.isnumeric()}
É alfanumérico? {msg.isalnum()}
Está em maiúsculas? {msg.isupper()}
Está em minúsculas? {msg.islower()}
Está capitalizada? {msg.istitle()}
""")
