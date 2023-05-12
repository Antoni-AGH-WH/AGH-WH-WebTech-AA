import httpx


if __name__ == "__main__":
    response = httpx.get("https://www.agh.edu.pl/")
    lines = response.text
    print(lines.upper().count("AGH"))