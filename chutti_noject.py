import random

# Define the list of data types globally
a_b = [1, 1.1, {1, 2, 3}, {"hello": 90}, "string", True, [1, 2, 3], None, (9, 10), 1 + 2j]


def choose_a_data():
    return random.choice(a_b)


def data_type_of_random_choice():
    a = choose_a_data()
    return type(a).__name__.lower()


def main():
    score = 0
    
    while True:
        i = input("Please make the input in lowercase letters: ")
        data_type = data_type_of_random_choice()
        
        if i.lower() in ["exit", "close"]:
            print("Final score:", score)
            break
        
        if data_type == i:
            score += 1
            print("Correct! The data type is:", data_type)
        else:
            if score > 0:
                score -= 1
            print(f"Wrong! The correct data type is: {data_type}. Try again.")
    
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
