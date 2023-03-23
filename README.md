# News_API
The News API project involves designing and building an application programming interface (API) that can retrieve news articles and related information from various sources and deliver them to users through a standardized interface

![](/app/static/assets/img/screenshot.PNG)

## Returns news data as JSON objects 
```json
[
    {
        "author": null,
        "desc": "The Federal Reserve on Wednesday raised interest rates by a quarter of a percentage point, but indicated it was on the verge of pausing further increases in borrowing costs amid recent turmoil in financial markets spurred by the collapse of two U.S. banks.",
        "img": "https://www.reuters.com/resizer/NWVFUzvrPlMxde7PrIKhK5WuTlc=/1200x628/smart/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/VL7XFOQFJNP3NC7LYLIS5QUVAM.jpg",
        "p_date": "2023-03-22T18:51:13Z",
        "source": {
            "id": "reuters",
            "name": "Reuters"
        },
        "title": "U.S. Fed delivers small rate hike amid global banking turmoil",
        "url": "https://www.reuters.com/business/finance/us-banks-face-scrutiny-fed-rate-decision-looms-2023-03-22/"
    },
    {
        "author": "Taylor Hatmaker",
        "desc": "TikTok's CEO will offer reassurances that the company can safeguard the safety of minors and ward off threats to U.S. user privacy.",
        "img": "https://techcrunch.com/wp-content/uploads/2022/04/GettyImages-1231203702.jpeg?resize=1200,800",
        "p_date": "2023-03-22T18:49:22Z",
        "source": {
            "id": "techcrunch",
            "name": "TechCrunch"
        },
        "title": "TikTok gears up for its big day in Congress",
        "url": "https://techcrunch.com/2023/03/22/tiktok-gears-up-for-its-big-day-in-congress/"
    },
    {
        "author": null,
        "desc": "A Delaware judge wrapped up a two-day hearing in the $1.6 billion defamation lawsuit by Dominion Voting Systems against Fox Corp <a href=\"https://www.reuters.com/companies/FOXA.O\" target=\"_blank\">(FOXA.O)</a> over vote-rigging claims aired by Fox News, but di…",
        "img": "https://www.reuters.com/resizer/-pDUOJaUBTbn6Gfa9uF-AEpci2k=/1200x628/smart/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/76AKZUKCBNKC5EDC2T66FAQTI4.jpg",
        "p_date": "2023-03-22T17:11:34Z",
        "source": {
            "id": "reuters",
            "name": "Reuters"
        },
        "title": "Judge wraps up hearing in Dominion defamation suit against Fox; no ruling",
        "url": "https://www.reuters.com/legal/judge-wraps-up-hearing-dominion-defamation-suit-against-fox-no-ruling-2023-03-22/"
    },
    {
        "author": "Ashley Belanger",
        "desc": "Trump family names are also seemingly blocked on AI-imager Midjourney.",
        "img": "https://cdn.arstechnica.net/wp-content/uploads/2023/03/AI-faked-Trump-arrest-image_Eliot-Higgins_Midjourney-760x380.jpeg",
        "p_date": "2023-03-22T17:05:28+00:00",
        "source": {
            "id": "ars-technica",
            "name": "Ars Technica"
        },
        "title": "AI platform allegedly bans journalist over fake Trump arrest images",
        "url": "https://arstechnica.com/tech-policy/2023/03/ai-platform-allegedly-bans-journalist-over-fake-trump-arrest-images/"
    },
    {
        "author": "Emma Roth, Mitchell Clark",
        "desc": "The Counter-Strike 2 beta test program launches today before Valve officially launches the CS:GO replacement this summer in a bigger, brighter, faster refresh of its popular FPS title.",
        "img": "https://cdn.vox-cdn.com/thumbor/9OLfVccqzJP_upDarGO2oOXBhFw=/0x0:2524x1730/1200x628/filters:focal(1262x865:1263x866)/cdn.vox-cdn.com/uploads/chorus_asset/file/24528220/Screenshot_2023_03_22_at_09.43.05.png",
        "p_date": "2023-03-22T16:50:35Z",
        "source": {
            "id": "the-verge",
            "name": "The Verge"
        },
        "title": "Valve announces Counter-Strike 2, a free replacement for CS:GO",
        "url": "http://www.theverge.com/2023/3/22/23651939/counterstrike-cs2-valve-smoke-grenades-limited-test"
    },
    {
        "author": "Jon Brodkin",
        "desc": "Newsmax said it now accepts that DirecTV isn't trying to censor conservatives.",
        "img": "https://cdn.arstechnica.net/wp-content/uploads/2023/03/getty-newsmax-760x380.jpg",
        "p_date": "2023-03-22T16:42:04+00:00",
        "source": {
            "id": "ars-technica",
            "name": "Ars Technica"
        },
        "title": "DirecTV puts Newsmax back on the air after Republicans’ angry protests",
        "url": "https://arstechnica.com/tech-policy/2023/03/directv-puts-newsmax-back-on-the-air-after-republicans-angry-protests/"
    }
]

```
## Endpoints 
-The `home()` route returns a JSON response with the published articles. 
-The `headlines()` route returns a JSON response with the top headlines. 
-The `articles()` route returns a JSON response with random articles. 
-The `sources()` route returns a plain text response with the news sources.

-The `business()`, `tech()`, `entertainment()`, `science()`, `sports()`, and` health()` routes each return a JSON response 
    with articles related to their respective categories.




## Technologies
- python 3.11



