import requests
def main(url):
    res = requests.get(url)
    res = res.json()
    print(res)
    for result in res["results"]:
        print(result["name"]+"  "+str(result["id"]))
query=input("enter the film name")    
url ="https://api.themoviedb.org/3/search/company?api_key=097f22e0aa702d57dfff42acef5b1874&query="+query+"&page=1"
main(url)
