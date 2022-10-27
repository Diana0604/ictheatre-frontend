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

# given a string that contains a number with decimals, return with only two decimals
# for example 1.23123 becomes 1.23
def numberToTwoDecimals(string):
    string = str(string)
    if '.' in string:
        commaIndex = string.index('.')
        string = removeAfterN(string, commaIndex + 3)
    return string
