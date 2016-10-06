def test_edit_contact(app_cont):
    app_cont.session_cont.login(username="admin", password="secret")
    app_cont.contact.edit_contact()
    app_cont.session_cont.logout()