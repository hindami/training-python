import tiktoken

enc = tiktoken.get_encoding("o200k_base")
# assert enc.decode(enc.encode("hello world")) == "hello world"

enc = tiktoken.encoding_for_model("gpt-4o")


print(enc.encode("the lord of the rings the return of the king!"))

print(enc.encode("2 + 2 = 4"))
