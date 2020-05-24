
# lesson_package内のutilsをimportする。

from lesson_package import utils


def sing():
    return 'sing'


def cry():
    return utils.say_twice('cry')
