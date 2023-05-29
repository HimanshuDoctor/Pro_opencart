import configparser # to read the data from the configurations(.ini file)
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')


class ReadConfig():
    @staticmethod
    # when you create any method with the staic, that method we can directly call by using a class."
    # we no need to create an object
    def getApplicationURL():
        url=config.get('commonInfo', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('commonInfo', 'email')
        return username

    @staticmethod
    def getPassword():
        password=config.get('commonInfo', 'password')
        return password


#Testing above methods - optional Code
#print(ReadConfig.getApplicationURL())
#print(ReadConfig.getUseremail())

