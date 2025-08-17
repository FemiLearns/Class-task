names = ("Joy", "Ade", "Bola")
phone_numbers = ("08172600297", "08112345678", "07023456789")
name_and_numbers = dict(zip(names, phone_numbers))
print(name_and_numbers) 
whole = {
    "Joy" : "08172600297",
    "Ade" : "08112345678",
    "Bola" : "07023456789"
}             
Username = input("Enter a name: ")
if Username is not names:
    print(f"The phone number for {Username} in {whole.items()}")
else:
    print(f"{Username} not found")
