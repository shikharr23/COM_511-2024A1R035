# clean the sentence from unwanted spaces at end and back

sen1 = input()

print("org:",sen1)
sen2 = sen1.strip()
sen3 = sen2.replace("  ", " ")
print("neuwu:",sen3)