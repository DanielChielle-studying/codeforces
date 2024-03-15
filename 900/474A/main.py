def solve_error(c, s):
    keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"
    keyboard_dict = {keyboard[key]: key for key in range(len(keyboard))}

    if s == "R":
        correct_sequence = [keyboard[(keyboard_dict[key] - 1) % len(keyboard)] for key in c]
    else:
        correct_sequence = [keyboard[(keyboard_dict[key] + 1) % len(keyboard)] for key in c]

    return ''.join(correct_sequence)

def main():
    shift = input()
    characters = input()

    corrected_sequence = solve_error(characters, shift)
    print(corrected_sequence)

if __name__ == "__main__":
    main()
