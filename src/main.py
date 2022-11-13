import robin_connection as rc


class main:
    try:
        steve_rc = rc.robin_connection('Steve')
        steve_rc.robin_login('636396')
        print('Steve has logged in.')
    except:
        print('Login failed')
        print(Exception)

    profile = steve_rc.see_full_profile()
    # print(profile)
    profile = steve_rc.see_simple_profile()
    # print(profile)
    stock = steve_rc.see_a_stock('GOOG')
    print(stock)
