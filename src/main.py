import robin_connection as rc
class main:
    steve_rc = rc.robin_connection('Steve')
    steve_rc.robin_login('636396')
    profile = steve_rc.see_full_profile()
    print(profile)
    profile = steve_rc.see_simple_profile()
    print(profile)
