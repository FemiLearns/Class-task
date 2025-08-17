User_name = input("Enter 3 Names (seperated by comma): ")
Set_of_names = set(User_name.strip() for User_name in User_name.split(","))
# print(Set_of_names)
All_Users = {
    "name": User_name,
    "name2": User_name,
    "name3": User_name

}
print({All_Users["name"]}, {All_Users["name2"]}, {All_Users["name3"]})