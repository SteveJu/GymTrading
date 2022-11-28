import robin_connection as rc


class main:
    def go(Name):
        steve_rc = rc.robin_connection(Name)
        steve_rc.robin_login('')

        full_profile = steve_rc.see_full_profile()
        # print(profile)
        simple_profile = steve_rc.see_simple_profile()
        # print(profile)
        #stock = steve_rc.see_a_stock('AAPL')
        option = steve_rc.see_an_option()
        #print(option)

        for item in option:
            for k, v in item.items():
                print(k, ':', v)


    if __name__ == '__main__':
        go('Steve')
