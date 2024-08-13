import sys


class Pattern:
    ALNUM = "\\w"
    DIGIT = "\\d"
    MATCH_EXACT_START = "^"
    MATCH_EXACT_END = "$"
    REPEAT = "+"


def match_pattern(input_line: str, pattern: str) -> bool:
    if not pattern:
        return True

    if pattern[0] == Pattern.MATCH_EXACT_START:
        return input_line.startswith(pattern[1:])

    if pattern[-1] == Pattern.MATCH_EXACT_END:
        return input_line.endswith(pattern[:-1])

    if len(pattern) > 1 and pattern[1] == Pattern.REPEAT:
        curr = input_line[0]
        i = 0
        while i < len(input_line) and input_line[i] == curr:
            i += 1
        return match_pattern(input_line[i:], pattern[2:])

    if pattern[:2] == Pattern.DIGIT and input_line and input_line[0].isdigit():
        return match_pattern(input_line[1:], pattern[2:])

    if pattern[:2] == Pattern.ALNUM and input_line and input_line[0].isalnum():
        return match_pattern(input_line[1:], pattern[2:])

    if pattern[0] == "[" and pattern[-1] == "]":
        negation = pattern[1] == "^"
        chars_to_match = pattern[2:-1] if negation else pattern[1:-1]
        if negation:
            return not any(match_pattern(input_line, char) for char in chars_to_match)
        return any(match_pattern(input_line, char) for char in chars_to_match)

    return input_line and pattern[0] == input_line[0] and match_pattern(input_line[1:], pattern[1:])


def main():
    if len(sys.argv) != 3 or sys.argv[1] != "-E":
        print("Usage: script.py -E <pattern>")
        exit(1)

    pattern = sys.argv[2]
    input_line = sys.stdin.read().strip()

    if match_pattern(input_line, pattern):
        print("Matched")
        exit(0)
    else:
        print("Not Matched")
        exit(1)


if __name__ == "__main__":
    main()
