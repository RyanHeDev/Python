# auto google search from terminal
try:
    from googlesearch import search
except ImportError:
    print("Module not found")

query = input("Enter your query: \n")

for i in search(query, tld="com", num=10, stop=10, pause=2):
    print(i)
    
