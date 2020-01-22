import random

def calculateDistributionSub(number, alpha, elements, distribution):
    sum = 0
    for i in range(0, elements):
        sum += distribution[i]
    remaining = number - sum
    if (remaining > alpha):
        fraction = remaining // alpha
        fractionMiddle = fraction // 2

        # assigning values to distribution
        for i in range(0, elements):

            # some hard coding here!!
            if (i == 0 or i == 6):
                distribution[i] += random.randint(0, fractionMiddle)
            else:
                distribution[i] += random.randint(fractionMiddle, fraction)

        distribution, remaining = calculateDistributionSub(number, alpha, elements, distribution)
    
    # return area - you don't mess with return
    return distribution, remaining

def calculateDistribution(number, alpha, elements):
    distribution = []
    # we should check if fraction can be an integer > 0
    # we should also check if there is more pigeons than holes
    if (number > alpha and alpha > elements):
        fraction = number // alpha
        for i in range(0, elements):
            distribution.append(fraction)
        distribution, remaining = calculateDistributionSub(number, alpha, elements, distribution)
    else:
        remaining = number

    # return area - you don't mess with return
    return distribution, remaining

def main():
    number, alpha = map(int, input("Enter number and alpha: ").split())
    elements = 7
    distribution, remaining = calculateDistribution(number, alpha, elements)
    print(distribution)
    print(remaining)

if __name__ == "__main__":
    main()