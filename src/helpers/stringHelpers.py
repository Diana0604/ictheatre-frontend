# Function to remove after N
# characters from string
def removeAfterN(string, N):
    if len(string) <= N:
        return string

    # Stores the resultant string
    res = ''

    # Traverse the string
    for i in range(N):

        # Insert current character
        res += string[i]

    # Return the string
    return res
