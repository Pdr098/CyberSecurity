msg = input("Enter the message: ")

depth = int (input("Enter the depth value: "))

def cipher(text, key):
    result =""

    matrix = [["" for j in range(len(text))] for i in range(key)]

    increment = 1
    row = 0
    col = 0

    for char in text:
        if (row+increment < 0 or row+increment >= len(matrix)):
            increment = increment * -1

        matrix[row][col] = char
        row += increment
        col += 1
    
    for lst in matrix:
        result += "".join(lst)

    return result

def decipher(cipText, key):
    result = ""

    matrix = [["" for j in range(len(cipText))] for i in range(key)]

    idx = 0
    increment = 1

    for Row in range(len(matrix)):
        row = 0

        for col in range(len(matrix[row])):

            if (row+increment < 0 or row+increment >= len(matrix)):
                increment = increment * -1

            if (row == Row):
                matrix[row][col] = cipText[idx]
                idx += 1
            row += increment
        
    matrix = transpose(matrix)

    for lst in matrix:
        result += "".join(lst)

    return result

def transpose(m):

    transposed = [["" for j in range(len(m))] for j in range(len(m[0]))]

    for i in range(len(m)):
        for j in range(len(m[0])):
            transposed[j][i] = m[i][j]

    return transposed

cipherMsg = cipher(msg, depth)
decipherMsg = decipher(cipherMsg, depth)

print("Message: " + msg)
print("Ciphered message: " + cipherMsg)
print("Deciphered message:", decipherMsg)
