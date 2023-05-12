import httpx


if __name__ == "__main__":
    user = "github"
    response = httpx.get(f"https://api.github.com/users/{user}/repos")
    repos = response.json()

    print(repos)
