from django.core.validators import ValidationError


UA_SIM_PROVIDERS = {"039", "067", "068", "096", "097", "098", "050", "066", "095",
                    "099", "063", "073", "093", "091", "092", "089", "094"}
UA_PHONE_NUMBER_LENGTH = 12


def get_table_with_students(all_students):
    table = "<table><tr><th>Name</th><th>Email</th><th>Birthday</th></tr>"
    for st in all_students:
        table += f"""
        <tr>
            <td> <a href=\"{st.pk}\"> {st.name} {st.surname} </a></td>
            <td>{st.email}</td>
            <td>{st.birthday}</td>
        </tr>
        """
    table += "</table>"
    return table


def not_found():
    page = f"""
    <center>
        <h1> 404 Not Found </h1>
        {student_navigation()}
    </center>
    """
    return page


def student_navigation():
    return "<br><br> " \
           "<a href=\"/students/\"> All students </a> | " \
           "<a href=\"/students/create/\"> Create </a>"


def format_phone_number(phone_number: str):
    if not phone_number.isnumeric():
        phone_number = get_only_numbers(phone_number)
    
    country_code = phone_number[:3]
    provider = phone_number[3:5]
    numbers = "{}-{}-{}".format(phone_number[5:8], phone_number[8:10], phone_number[10:])
    
    phone_format = f"{country_code} {provider} {numbers}"
    return phone_format


def normalize_phone_number(phone_number: str):
    only_numbers = get_only_numbers(phone_number)
    
    # this will work only for UA phone numbers
    # to support all phone numbers - it's required to divide country code & number
    
    if len(only_numbers) != UA_PHONE_NUMBER_LENGTH:
        message = f"Wrong phone number, should be {UA_PHONE_NUMBER_LENGTH} numbers, got {len(only_numbers)}"
        raise ValidationError(message=message)
    elif only_numbers[:3] != "380":
        raise ValidationError(message="That's not UA number")
    elif only_numbers[2:5] not in UA_SIM_PROVIDERS:
        raise ValidationError(message="There are no such sim-card provides")
    else:
        country_code = only_numbers[:3]
        provider = only_numbers[3:5]
        numbers = "{}-{}-{}".format(only_numbers[5:8], only_numbers[8:10], only_numbers[10:])
        
        phone_format = f"{country_code} {provider} {numbers}"
        return phone_format


def get_only_numbers(phone_number: str):
    res = ""
    for char in phone_number:
        if char.isnumeric():
            res += char
    return res


# def Homework_12_task_1(phone_number: str):
#     """
#     1. A new field phone has been added to the Student model. Add it to the form.
#       Create a method that will validate the entered phone number and strip it of all
#       characters except numbers, buses, pluses, and parentheses.
#     """
#     from django.core.validators import ValidationError
#     allowed = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", " ", ")", "("]
#
#     # clear
#     result = ""
#     first_3_numbers = ""
#     total_numbers = 0
#     for char in phone_number:
#         if char in allowed:
#             result += char
#         if char.isnumeric():
#             total_numbers += 1
#             if len(first_3_numbers) < 3:
#                 first_3_numbers += char
#
#
#     if first_3_numbers == "380" and total_numbers == 12:
#         return result
#     else:
#         raise ValidationError(message="Wrong phone number")
