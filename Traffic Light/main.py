import time

North = "Red"
South = "Red"
states = ["Red", "Orange", "Green"]

def northlights() :
    time.sleep(5)
    North = states[2]
    print(f"North Light is now {North}, South Light is now {South}")
    time.sleep(15)
    North = states[1]
    print(f"North Light is now {North}, South Light is now {South}")
    time.sleep(3)
    North = states[0]
    print(f"North Light is now {North}, South Light is now {South}")
    return "North"


def southlights() :
    time.sleep(5)
    South = states[2]
    print(f"North Light is now {North}, South Light is now {South}")
    time.sleep(15)
    South = states[1]
    print(f"North Light is now {North}, South Light is now {South}")
    time.sleep(3)
    South = states[0]
    print(f"North Light is now {North}, South Light is now {South}")
    return "South"


x = "South"
print(f"Starting State: North Light: {North}, South Light: {South}")
for x in range(10) :
    x = northlights()
    while x == "South" :
        time.sleep(1)
    x = southlights()
    while x == "North" :
        time.sleep(1)
