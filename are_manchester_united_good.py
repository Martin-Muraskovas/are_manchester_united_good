import requests
from bs4 import BeautifulSoup

# url for manchester united football results
url = "https://fbref.com/en/squads/19538871/Manchester-United-Stats#all_matchlogs"

# uses a get request to retrieve the content of the url
response = requests.get(url)

# parses the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# finds the div containing the latest match results
div = soup.find("div", {"id": "all_matchlogs"})


if div is not None:
    # Extract the results of the last 5 matches
    matches = div.find_all("tr")[1:6]  # Exclude header row and get the latest 5 matches

    # Check if Manchester United won, drawn, or lost their last 5 matches
    result_summary = ""
    for match in matches:
        result = match.find_all("td")[5].text.strip()
        if "W" in result:
            result_summary += "Won, "
        elif "D" in result:
            result_summary += "Drawn, "
        elif "L" in result:
            result_summary += "Lost, "

    results = "Manchester United's Recent Form: \n" + result_summary[:-2]  # removes unnecessary formatting
    print(results)
    wins = results.count("Won")
    losses = results.count("Lost")

    if wins > 2:
        print("\nManchester United are Good at the moment.")
    else:
        print("\nAs usual, Manchester United are bad at the moment.")
else:
    print("Results not found")


