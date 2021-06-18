
def main():
    questions = ["I feel that I am a person of worth, at least on an equal plane with others.",
        "I feel that I have a number of good qualities.",
        "All in all, I am inclined to feel that I am a failure.",
        "I am able to do things as well as most other people.",
        "I feel I do not have much to be proud of.",
        "I take a positive attitude toward myself.",
        "On the whole, I am satisfied with myself.",
        "I wish I could have more respect for myself.",
        "I certainly feel useless at times.",
        "At times I think I am no good at all."]

    score = 0
    for i in range(10):
        print(questions[i])
        answer = input("Enter D, d, a, or A: ")
        if i + 1 in [1, 2, 4, 6, 7]:
            if answer == "D":
                score += 0
            elif answer == "d":
                score += 1
            elif answer == "a":
                score += 2
            else:
                score += 3
        else:
            if answer == "A":
                score += 0
            elif answer == "a":
                score += 1
            elif answer == "d":
                score += 2
            else:
                score += 3    

    print(f"Your Score Is {score}")
    print("A score below 15 may indicate problematic low self-esteem.")

if __name__ == "__main__":
    main()

