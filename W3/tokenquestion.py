import tiktoken

# Use the "cl100k_base" encoding instead of "gpt-4"
encoding = tiktoken.get_encoding("cl100k_base")

# The input message you want to tokenize
input_message = """
List only the valid English words from these: cdKedeI, t8sW5cWA, RdYvFX8A8, dqbn0LPQ7L, G5LOk8, aSKVx7Z7q, 1vGiGuZ, JlDWD, 59X5BRM, D, Rm65, 2k, z, 4, X99gkPCCDM, xTptNacT, 3GkwImB, tp, PpOWVQj, Wd, J, NBCrxVe, c7A31U3x, mefGWk9d, BrrgpJND, KenUa, R, LR0oOpP, 932yU, RTWFjwhN, qj, I3AbT, iyeUHOVYw, 90PmKHJC, gJsp, h, 9L1Tr, 8ct4cD5, L7, fSmlw56o, XNIm, mRF6, NNDDlcIILP, c3wpu6HqmX, ZR, cyBJG, GEOBFkV, 2KlY0t, kGVMFpW, FOPurt8, 1jdm, M, h5YiX, m7X, Tnzuh, vZV6M, d, z29F758nW, bmdYsDT, Doy, oxg1P, mdKiJjpDh8
"""

# Tokenize the input message
tokens = encoding.encode(input_message)

# Get the token count
num_tokens = len(tokens)

print(f"The input message uses {num_tokens} tokens.")
