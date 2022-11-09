# """WordSequence II"""
# def wordseqtwo(text1, text2):
#     """WordSequence II"""
#     count = 0
#     print("".join(text1))
#     if len(text2) < len(text1):
#         wordseq(text1, text2)
#     elif len(text2) > len(text1):
#         for _ in range(len(text2)):
#             if text1 == text2:
#                 break
#             else:
#                 lennn = len(text1)
#                 for sub in text2:
#                     if count == lennn:
#                         res = sub.replace(sub, text2[count])
#                         text1.insert(count, res)
#                         print("".join(text1))
#                         count += 1
#                         break
#                     res = sub.replace(sub, text2[count])
#                     text1.insert(count, res)
#                     text1.pop(count+1)
#                     print("".join(text1))
#                     count += 1
#     else:
#         for _ in range(len(text1)):
#             if text1 == text2:
#                 break
#             else:
#                 for sub in text2:
#                     res = sub.replace(sub, text2[count])
#                     text1.insert(count, res)
#                     text1.pop(count+1)
#                     print("".join(text1))
#                     count += 1
# def wordseq(text1, text2):
#     """WordSequence II"""
#     count = 0
#     for _ in range(len(text1)):
#         if len(text1) == len(text2):
#             break
#         else:
#             lenn = len(text2)
#             for sub in text2:
#                 if count >= lenn:
#                     del text1[count]
#                     print("".join(text1))
#                     break
#                 elif count < len(text2):
#                     res = sub.replace(sub, text2[count])
#                     text1.insert(count, res)
#                     text1.pop(count+1)
#                     print("".join(text1))
#                     count += 1
# wordseqtwo(list(input()), list(input()))

'''PSCP Program'''
def main(word1, word2):
    '''WordSequence II'''
    length = max(len(word1), len(word2))
    for i in range(length+1):
        out = word2[:i] + word1[i:]
        print(out)
main(input(), input())
