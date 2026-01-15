import sys

def generate_permutations(s):
    if len(s) == 1:
        return [s]
    
    perms = []
    prev = None
    for i, c in enumerate(s):
        # Skip duplicate characters to avoid duplicate permutations
        if c == prev:
            continue
        
        prev = c
        remaining = s[:i] + s[i+1:]
        for perm in generate_permutations(remaining):
            perms.append(c + perm)
        
    return perms

def main(in_file):
    try:
        with open(in_file, 'r') as file:
            for line in file:
                word = line.strip()
                if not word:
                    continue
                    
                # Sort characters in "digit < uppercase < lowercase" order
                word = ''.join(sorted(word))
                # Generate all permutations
                permutations = generate_permutations(word)
                # Print as comma separated values
                print(','.join(permutations))
    except FileNotFoundError:
        print(f"Error: The file '{in_file}' was not found.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py [file_name]")
        sys.exit(1)
    
    main(sys.argv[1])