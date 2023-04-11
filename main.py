#DivideBy3
#Steven Halla

from typing import Final

#a constant 3 because we are dividing everything by 3
THREE: Final = 3
print("***Divide input by 3***")

try_again: bool = True

 #input
while try_again:
    try:
        string_input: float = float(input("Please enter a number: "))
        input_number: float = float(string_input)

        # process
        answer: float = input_number / THREE

        # output
        print("Your number divided by 3 is: ", answer)
        try_again_input: str = input("would you like to input again type y or n: ")
        if try_again_input == "n":
            try_again = False
        else:
            try_again = True

    except ValueError:
        print("Invalid input. Please enter a number.")


