# FakeNewsCalculator
- Calculates a fake-ness score given a URL to a news article.
- Python Flask server running on Heroku for back-end
- Covfefe score is based on keyword instances, as well as results from searching for similar content using the Bing Web Search API
- The more keywords, and the less similar other articles are, the more fake the article is (higher score)
- Project completed during the HackWestern hackathon at Western University in November 2018
- Link to web-portal https://fakenewscalculator.herokuapp.com/webportal.html

# Dependencies
- html2text, json, requests, flask (see requirements.txt)

# Structure
- Flask backend with custom Python utilities (ie. bing search and keyword search scripts)
- Custom front-end web portal written in HTML, CSS, and Javascript.

# Web Portal Demo (GIF)
![alt text](https://github.com/Setoville/FakeNewsCalculator/blob/master/images/demo.gif)
