

def get_table_with_students(all_students):
    table = "<table><tr><th>Name</th><th>Birthday</th><th>Email</th></tr>"
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


def get_only_numbers(phone_number: str):
    res = ""
    for char in phone_number:
        if char.isnumeric():
            res += char
    return res


def HW_task_1(phone_number: str):
    from django.core.validators import ValidationError
    allowed = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", " ", ")", "("]
    
    # clear
    result = ""
    first_3_numbers = ""
    total_numbers = 0
    for char in phone_number:
        if char in allowed:
            result += char
        if char.isnumeric():
            total_numbers += 1
            if len(first_3_numbers) < 3:
                first_3_numbers += char
                
            
    if first_3_numbers == "380" and total_numbers == 12:
        return result
    else:
        raise ValidationError(message="Wrong phone number")
