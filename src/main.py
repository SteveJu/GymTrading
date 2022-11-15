import robin_connection as rc


class main:
    steve_rc = rc.robin_connection('Steve')
    steve_rc.robin_login('636396')

    full_profile = steve_rc.see_full_profile()
    # print(profile)
    simple_profile = steve_rc.see_simple_profile()
    # print(profile)
    stock = steve_rc.see_a_stock('AAPL')
    for item in stock:
        for k, v in item.items():
            print(k, ':', v)
