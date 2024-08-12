import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line: str, pattern: str) -> bool:
    if len(pattern) == 1:
        return pattern in input_line
    elif pattern == "\\d":
        return any(char.isdigit() for char in input_line)
    elif pattern == "\\w":
        return any(char.isalnum() for char in input_line)
    elif pattern[0] == "[" and pattern[-1] == "]":
        return any(char in pattern[1:-1] for char in input_line)
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read().strip()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    if match_pattern(input_line, pattern):
        print("PASSED")
        exit(0)
    else:
        print("FAILED")
        exit(1)


if __name__ == "__main__":
    main()
