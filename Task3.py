class Switch(object):
    def __init__(self, unit_name, mac_address, ip_address, login, password):
        self.__unit_name = unit_name
        self.__mac_address = mac_address
        self.__ip_address = ip_address
        self.__login = login
        self.__password = password

    @property
    def unit_name(self):
        return self.__unit_name

    @unit_name.setter
    def unit_name(self, value):
        self.__unit_name = value

    @property
    def mac_address(self):
        return self.__mac_address

    @mac_address.setter
    def mac_address(self, value):
        self.__mac_address = value

    @property
    def ip_address(self):
        return self.__ip_address

    @ip_address.setter
    def ip_address(self, value):
        self.__ip_address = value

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        self.__login = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value


c = Switch('Mac', '50:46:5D:6E:8C:20', '192.42.116.16', 'logit', 'passit')
c.unit_name = 'mycomp'
c.mac_address = '00:19:b9:89:c1:59'
c.ip_address = '192.168.11.10'
c.login = 'unit'
c.password = '1234567890'
print(c.unit_name)
print(c.mac_address)
print(c.ip_address)
print(c.login)
print(c.password)