import whois

def domain_info(link):
    domain = whois.whois(url)
    print(f"Server: {domain.whois_server}\n Expiration Date: {domain.expiration_date}\n Name: {domain.name}\n Organisation: {domain.org}\n State: {domain.state}\n City: {domain.city}\n Country: {domain.country}")


url = input("Enter url: \n")

try:
    domain = whois.whois(url)
except:
    print("This domain is available")

else:
    print("This domain is already purchased")
    print("Domain information\n")
    domain_info(url)
