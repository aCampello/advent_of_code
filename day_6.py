with open('input_6.txt', 'r') as f:
    days = [int(n) for n in f.read().split(',')]

# Part A: Naive approach

class LanternFish:
    def __init__(self, timer):
        self.timer = timer

    def __repr__(self):
        return str(self.timer)

    def produce_fish(self):
        """ Produces a fish or returns none if timer != 0 """
        self.timer = 6
        return LanternFish(timer=8)


fish_list = [LanternFish(timer=n) for n in days]


for _ in range(80):
    new_fishes = []
    for fish in fish_list:
        if fish.timer == 0:
            new_fishes.append(fish.produce_fish())
        else:
            fish.timer -= 1

    fish_list += new_fishes

print(len(fish_list))


# For part 2 we need a smarter data structure. We'll define a hash table with how many fishes have
# a certain timer, and decrement it every day
timer_to_fish = [0] * 9

for timer in days:
    timer_to_fish[timer] += 1

for _ in range(256):
    # Compute new fishes
    new_fish_produced = timer_to_fish[0]
    timer_to_fish[0] = 0

    # Decrement the rest
    for timer in range(1, 9):
        timer_to_fish[timer-1] += timer_to_fish[timer]
        timer_to_fish[timer] = 0

    # Add day 8 and day 6 fishes produced by reproduction
    timer_to_fish[8] += new_fish_produced
    timer_to_fish[6] += new_fish_produced


print(sum(timer_to_fish))
