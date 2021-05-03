sports = {"football","cricket","Tennis"}

sport2 = {"soccer","bowling","hockey","football"}

sports.symmetric_difference_update(sport2)

print(sports)

new = sport2.symmetric_difference(sports)

print(new)