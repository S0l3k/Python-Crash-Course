first_name = "vadim"
last_name = "novikov"
full_name = f"{first_name} {last_name}"
print(full_name.title())

message = f"Hello, {full_name.title()}!"
print(message)

full_name_plus = first_name.title() + " " + last_name.title()
print(full_name_plus)

print("some \n\ttext")

f_l = " python "
print(f_l)
f_l = f_l.rstrip()
f_l = f_l.lstrip()
print(f_l)
