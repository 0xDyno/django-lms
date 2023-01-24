

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
