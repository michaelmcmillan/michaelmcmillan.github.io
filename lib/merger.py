def merge(first_string, second_string, pad=40):
    first_lines = [line.replace('\n', '') for line in first_string.split('\n')]
    second_lines = [line.replace('\n', '') for line in second_string.split('\n')]
    merged_lines = []

    total_lines = max(len(first_lines), len(second_lines))

    for line_index in range(0, total_lines):
        first_line_exists = line_index < len(first_lines)
        second_line_exists = line_index < len(second_lines)

        merged_line = ''

        if first_line_exists:
            merged_line += first_lines[line_index]

            # and second line exists 
            if second_line_exists:
                padding = (pad - len(first_lines[line_index])) * ' '
                merged_line += padding + second_lines[line_index]

        # First line does not exist
        elif not first_line_exists: # and we're still looping, meaning second line does
            padding = pad * ' '
            merged_line += padding + second_lines[line_index]

        merged_lines.append(merged_line)

    return '\n'.join(merged_lines)
