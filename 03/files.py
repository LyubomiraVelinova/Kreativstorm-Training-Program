# try:
#     with open("test.txt") as f:
#         text = f.read()
#         text = text.upper()
#         print(text)
# except Exception as e:
#     print("Ooops! An error occured", e)

with open("mbox-short.txt") as f:
    text = f.read()
        if s.startswith('Received:'):
            print(s)