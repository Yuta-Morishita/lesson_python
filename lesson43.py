
# ! import文とas


from lesson_package import utils  # lesson_package内のutilsをimportしている。
from lesson_package.talk import human, animal  # lesson_package内のtalk内のhumanをimportしている。
r = utils.say_twice('hello')

print(r)
# ? hellohello

print(human.sing())
# ? sign

print(human.cry())
# ? crycry

print(animal.sing())
print(animal.cry())
