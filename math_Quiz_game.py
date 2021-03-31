from random import randint

# consumer


def calculateAnswer(lhs, rhs, oparator):
    if oparator == '+':
        return lhs + rhs
    elif oparator == '-':
        return lhs - rhs
    elif oparator == '*':
        return lhs * rhs
    elif oparator == '/':
        return lhs / rhs
    elif oparator == '**':
        return lhs ** rhs
    raise Exception('Unkown Operator')


def generatorQuestion():
    ops = "/*-+"
    opIndex = randint(0, len(ops) - 1)
    operator = ops[opIndex]
    lhs = randint(0, 10)
    rhs = randint(0, 10)
    while(rhs == 0 and operator == "/"):
        rhs = randint(0, 10)

    return lhs, rhs, operator


def isAccurateEnoughAnswer(giveAnswer, correctAnswer, tolerance=0.01):
    difference = abs(float(giveAnswer) - float(correctAnswer))
    return difference <= tolerance


totalQuestion = 10
correct = 0

for i in range(totalQuestion):
    question = generatorQuestion()
    correctAnswer = calculateAnswer(question[0], question[1], question[2])
    playerAnswer = input('{0} {2} {1} = '.format(
        question[0], question[1], question[2]))
    if(isAccurateEnoughAnswer(correctAnswer, playerAnswer)):
        print('Correct')
        correct += 1
    else:
        print('wrong. Correct answer = ' + str(correctAnswer))

print("You got {0} correct answer out of {1}. or {2}% correct".format(
    correct, totalQuestion, correct/totalQuestion*100))
