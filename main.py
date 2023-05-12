import httpx

for i in range(1):
    if __name__ == "__main__":
        user = "github"
        response = httpx.get(f"https://api.github.com/users/{user}/repos")
        repos = response.json()

        print("python/n")
        for project in repos:
            nazwa_projektu = project["name"]
            https_projektu = project["url"]
            print("Project:{}/nURL:{}".format(nazwa_projektu,https_projektu))

        #print(repos)


