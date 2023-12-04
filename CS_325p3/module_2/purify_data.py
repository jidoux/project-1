# this module writes the purified file data to a file
# input: the raw data file
# output: the purified file data, in a file
def purify_data(input_filename, output_file):
    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            lines = input_file.readlines()

        # Creates a list to store the lines that come after the line that starts with "[–]"
        comments = []

        for i, line in enumerate(lines):
            # Checks if the line starts with "[–]"
            if line.strip().startswith("[–]"):
                # Append the lines that come after the line that starts with "[–]"
                for j in range(i+1, len(lines)):
                    if not lines[j].strip().startswith("[–]"):
                        comments.append(lines[j].strip())
                    else:
                        break

        # Saves the filtered lines to comments.txt
        with open(output_file, 'w', encoding='utf-8') as output_file:
            output_file.write('\n'.join(comments))

    except Exception as e:
        print(f'An error occurred: {str(e)}')
