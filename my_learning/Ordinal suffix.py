# Ordinal suffix 

def ordinalSuffix(number):
    numberStr = str(number)
    if numberStr.endswith(("11", "12", "13" )):
        return f"{number}th"
    elif numberStr.endswith("1"):
        return f"{number}st"
    elif numberStr.endswith("2"):
        return f"{number}nd"
    elif numberStr.endswith("3"):
        return f"{number}rd"
    else:
        return f"{number}th"


print(ordinalSuffix(0))

print(ordinalSuffix(1))

print(ordinalSuffix(2))

print(ordinalSuffix(3))

print(ordinalSuffix(4))

print(ordinalSuffix(10))

print(ordinalSuffix(11))

print(ordinalSuffix(12))

print(ordinalSuffix(13))

print(ordinalSuffix(14))

print(ordinalSuffix(101))
