

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
