from . import create_shedule as m


def start_py(x, y):
    kurs = x
    group = y

    print(f'Курс: {x}\nГруппа: {y}')

    if (kurs is not None) or (group is not None):
        if (kurs.isdigit()) and (int(kurs) < 7):
            m.html_table_html = ""
            m.create_request(kurs, group)
            # print(f'Курс: {x}\nГруппа: {y}')

            return m.html_table_html
            # eel.view_table(m.html_table_html)