# Fetch Hacker News tool
This project is a simple script that automatically searches for relevant articles on Hacker News based on a list of keywords.

Why I done that? I used to check Hacker News almost every day. Then I discovered the Hacker News API, which allows us to fetch the latest news programmatically. So I thought: why not automate my search using keywords?
And that want I've done!

How it works? Keywords are stored in a configuration file; every time you run the script, it searches Hacker News for the most relevant articles based on those keywords and (optionally) saves results to a JSON file.

We use the official Firebase Hacker News API to retrieve stories. 

Here's an example of the data returned for a story.
You can access items (stories, comments, etc.) by their ID, for example:
https://hacker-news.firebaseio.com/v0/item/9224.json


    {
        "by": "dhouston",
        "descendants": 71,
        "id": 8863,
        "kids": [9224, 8917, 8884, ...],
        "score": 104,
        "time": 1175714200,
        "title": "My YC app: Dropbox - Throw away your USB drive",
        "type": "story",
        "url": "http://www.getdropbox.com/u/2/screencast.html"
    }

This the output:

![image_alt](https://github.com/FrancescoPaoloL/FetchHN/blob/main/output.jpg?raw=true)


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


## Languages and Tools
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## Requirements
```
aiohttp==3.11.16
PyYAML==6.0.2
```

## Test coverage
TODO


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

<hr>

## Connect with me
<p align="left">
<a href="https://www.linkedin.com/in/francescopl/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="francescopaololezza" height="20" width="30" /></a>
<a href="https://www.kaggle.com/francescopaolol" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/kaggle.svg" alt="francescopaololezza" height="20" width="30" /></a>
</p>



