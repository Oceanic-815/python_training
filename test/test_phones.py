import re #импортируем пакет для работы с рег. выражениями
def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0] # Получаем контакт с индексом 0
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0) # получаем информацию из формы редактирования
    assert contact_from_home_page.home ==  clear(contact_from_edit_page.home) # сравниваем номера между собой
    assert contact_from_home_page.work == clear(contact_from_edit_page.work)
    assert contact_from_home_page.mobile == clear(contact_from_edit_page.mobile)
    assert contact_from_home_page.phone2 == clear(contact_from_edit_page.phone2)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)  # получаем информацию со страницы просмотра контакта
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)  # получаем информацию из формы редактирования
    assert contact_from_view_page.home == contact_from_edit_page.home # сравниваем номера между собой
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

def clear(s):
    return re.sub("[() -]", "", s)# sub("что заменять", "на что заменять", где заменять)
