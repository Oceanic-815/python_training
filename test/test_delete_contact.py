def test_delete_contact(app_cont):
    app_cont.session_cont.login(username="admin", password="secret")
    app_cont.contact.del_contact()
    app_cont.session_cont.logout()