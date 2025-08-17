Days_of_the_week = ("Monday", "Tuesday", "Wednessday", "Thursday", "Friday", "Saturday", "Sunday")

Monday = input("Enter activity for Monday: ")
Tuesday = input("Enter activity for Tuesday: ")
Wednessday = input("Enter activity for Wednessday: ")
Activity = {

    "Monday" : Monday,
    "Tuesday" : Tuesday,
    "Wednessday" : Wednessday

}
    
x = zip(Monday, Tuesday, Wednessday)

print(Activity)
