import wmi

pc = wmi.WMI()
my_system = pc.Win32_ComputerSystem()[0]

print(f'Marca: {my_system.Manufacturer}') 
print(f'Modelo: {my_system.Model}')
print(f'Nome: {my_system.Name}')
print(f'Quantidade de CPU\'s: {my_system.NumberOfProcessors}')
print(f'Arquitetura: {my_system.SystemType}')
print(f'Família: {my_system.SystemFamily}')