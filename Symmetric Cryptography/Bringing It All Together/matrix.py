def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    result = ""
    for i in matrix:
        for val in i:
            res = val.to_bytes(16).decode()
            result += str(res)
    return result
    #return bytes([val for row in matrix for val in row])
    
# matrix = [
#     [99, 114, 121, 112],
#     [116, 111, 123, 105],
#     [110, 109, 97, 116],
#     [114, 105, 120, 125],
# ]
matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 114],
    [ 48, 117, 110, 100],
    [107,  51, 121, 125],
]

#print(matrix2bytes(matrix))
