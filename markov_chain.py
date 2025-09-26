import random
def markov_chain(init_value: str, steps: int) -> list[str]:
    journey = [init_value]
    value = init_value
    for i in range(steps):
        n = random.random()
        if(value == "A" and n < 0.3):
            value = "B"
        elif(value == "A" and n > 0.7):
            value = "C"
        elif(value == "B" and n < 0.3):
            value = "A"
        elif(value == "B" and n > 0.7):
            value = "C"
        elif(value == "C" and n < 0.3):
            value = "A"
        elif(value == "C" and n > 0.7):
            value = "B"
        journey.append(value)
    return journey

print(markov_chain("B", 10))
