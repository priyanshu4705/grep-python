import sys


class Pattern:
    ALNUM = "\\w"
    DIGIT = "\\d"


def match_pattern(input_line: str, pattern: str) -> bool:

    if len(input_line) == 0 and len(pattern) == 0:
        return True
    if not pattern:
        return True
    if not input_line:
        return False
    
    if pattern[0] == input_line[0]:
        return match_pattern(input_line[1:], pattern[1:])
    elif pattern[:2] == Pattern.DIGIT:
        for i in range(len(input_line)):
            if input_line[i].isdigit():
                return match_pattern(input_line[i+1:], pattern[2:])
        else:
            return False
    elif pattern[:2] == Pattern.ALNUM:
        if input_line[0].isalnum():
            return match_pattern(input_line[1:], pattern[2:])
        else:
            return False
    elif pattern[0] == "[" and pattern[-1] == "]":
        if pattern[1] == "^":
            return not match_pattern(input_line, pattern[2:-1])
        return match_pattern(input_line, pattern[1:-1])
    else:
        return match_pattern(input_line[1:], pattern)


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
