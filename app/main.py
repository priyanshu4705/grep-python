import sys


class Pattern:
    ALNUM = "\\w"
    DIGIT = "\\d"
    MATCH_EXACT_START = "^"
    MATCH_EXACT_END = "$"
    REPEAT = "+"
    OPTIONAL = "?"


def match_pattern(input_line: str, pattern: str) -> bool:
    if len(input_line) == 0 and len(pattern) == 0:
        return True
    if not pattern:
        return True
    if not input_line:
        return False

    if pattern[0] == "^":
        pattern = pattern[1:]
        while len(pattern) > 0 and len(input_line) > 0:
            if pattern[0] == input_line[0]:
                pattern = pattern[1:]
                input_line = input_line[1:]
            else:
                return False
        return match_pattern(input_line, pattern)

    if pattern[-1] == Pattern.MATCH_EXACT_END:
        pattern = pattern[:-1]
        while len(pattern) > 0 and len(input_line) > 0:
            if pattern[-1] == input_line[-1]:
                pattern = pattern[:-1]
                input_line = input_line[:-1]
            else:
                return False
        return match_pattern(input_line, pattern)

    if pattern[0] == input_line[0]:
        if len(pattern) > 1:
            if pattern[1] == Pattern.REPEAT:
                return match_pattern(input_line[1:], pattern[2:]) or match_pattern(
                    input_line[1:], pattern
                )
            elif pattern[1] == Pattern.OPTIONAL:
                return match_pattern(input_line[1:], pattern[2:]) or match_pattern(
                    input_line, pattern[1:]
                )
        return match_pattern(input_line[1:], pattern[1:])

    elif pattern[0] != input_line[0] and len(pattern) > 1 and pattern[1] == Pattern.OPTIONAL:
        if pattern[1] == Pattern.OPTIONAL:
            return match_pattern(input_line, pattern[2:])
        return False

    elif pattern[:2] == Pattern.DIGIT:
        for i in range(len(input_line)):
            if input_line[i].isdigit():
                return match_pattern(input_line[i:], pattern[2:])
        else:
            return False

    elif pattern[:2] == Pattern.ALNUM:
        if input_line[0].isalnum():
            return match_pattern(input_line[1:], pattern[2:])
        else:
            return False

    elif pattern[0] == "[" and pattern[-1] == "]":
        if pattern[1] == Pattern.MATCH_EXACT_START:
            chrs = list(pattern[2:-1])
            for c in chrs:
                if c in input_line:
                    return False
            return True

        chrs = list(pattern[1:-1])
        for c in chrs:
            if c in input_line:
                return True
        return False

    else:
        return match_pattern(input_line[1:], pattern)

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
