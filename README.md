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
        "author": "Aria Alamalhodaei",
        "desc": "The U.S. National Reconnaissance Office is looking to bolster its hyperspectral sensing capabilities with six new contracts.",
        "img": "https://techcrunch.com/wp-content/uploads/2022/03/Pixxel-Hyperspectral-Images-Water.jpg?w=1057",
        "p_date": "2023-03-22T18:47:37Z",
        "source": {
            "id": "techcrunch",
            "name": "TechCrunch"
        },
        "title": "America's space-based spy agency awards six contracts to hyperspectral imagery providers",
        "url": "https://techcrunch.com/2023/03/22/americas-space-based-spy-agency-awards-six-contracts-to-hyperspectral-imagery-providers/"
    },
    {
        "author": "Ron Miller",
        "desc": "The UK Competition and Markets Authority expressed concern today that the $61B Broadcom-VMware deal could adversely impact competition.",
        "img": "https://techcrunch.com/wp-content/uploads/2023/03/GettyImages-1321540139.jpg?w=1024",
        "p_date": "2023-03-22T18:47:29Z",
        "source": {
            "id": "techcrunch",
            "name": "TechCrunch"
        },
        "title": "UK competition authority is concerned about the $61B Broadcom-VMware deal",
        "url": "https://techcrunch.com/2023/03/22/uk-competition-authority-is-concerned-about-the-61b-broadcom-vmware-deal/"
    },
    {
        "author": null,
        "desc": "To reassure customers, VeraBank CEO Brad Tidwell gave them his cell number and said they could call. \"Most of the institutions you're hearing about were somewhat single-focused,\" he says. \"I do not believe there's a reason to panic. I do not believe this is s…",
        "img": "https://cdn.cnn.com/cnnnext/dam/assets/230318094005-smr-bank-ceo-gives-customers-cell-00015101-super-tease.png",
        "p_date": "2023-03-22T18:37:34.8665328Z",
        "source": {
            "id": "cnn",
            "name": "CNN"
        },
        "title": "To reassure banking customers, CEO gives them his cell number - CNN Video",
        "url": "http://us.cnn.com/videos/business-money/2023/03/18/smr-bank-ceo-gives-customers-cell.cnn"
    },
    {
        "author": "Rebecca Bellan",
        "desc": "The reintroduced E-BIKE Act would provide $1,500 in federal tax rebates, which could help buyers avoid low-quality e-bikes that cause fires.",
        "img": "https://techcrunch.com/wp-content/uploads/2023/03/GettyImages-1395791732.jpg?resize=1200,800",
        "p_date": "2023-03-22T18:35:58Z",
        "source": {
            "id": "techcrunch",
            "name": "TechCrunch"
        },
        "title": "How a proposed federal e-bike incentive could lead to fewer battery fires",
        "url": "https://techcrunch.com/2023/03/22/how-a-proposed-federal-e-bike-incentive-could-lead-to-fewer-battery-fires/"
    },
    {
        "author": null,
        "desc": "The integration of OpenAI's technology into Microsoft-owned Bing has driven people to the little-used search engine and helped it compete better with market leader Google in page visits growth, according to data from analytics firm Similarweb.",
        "img": "https://www.reuters.com/resizer/XwIF5vvAtCaY-__VAjMyOtpbpOg=/1200x628/smart/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/2NCL3FQEORKWJNLIBYSEFTOBRM.jpg",
        "p_date": "2023-03-22T18:34:15Z",
        "source": {
            "id": "reuters",
            "name": "Reuters"
        },
        "title": "OpenAI tech gives Microsoft's Bing a boost in search battle with Google",
        "url": "https://www.reuters.com/technology/openai-tech-gives-microsofts-bing-boost-search-battle-with-google-2023-03-22/"
    },
    {
        "author": null,
        "desc": "Wall Street jumped after the U.S. Federal Reserve concluded its monetary policy meeting on Wednesday by hiking its key policy rate by 25 basis points, as widely expected.",
        "img": "https://www.reuters.com/resizer/i-4cFkXSScOiqQ02pV-2n_qq50Y=/1200x628/smart/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/KDUR3KSGI5KS3CFHSPGFLFXNME.jpg",
        "p_date": "2023-03-22T18:31:15Z",
        "source": {
            "id": "reuters",
            "name": "Reuters"
        },
        "title": "Wall Street spikes as Fed hints at rate hike pause",
        "url": "https://www.reuters.com/markets/us/futures-edge-lower-caution-ahead-fed-rate-decision-2023-03-22/"
    },
    {
        "author": "Jagmeet Singh",
        "desc": "We surveyed a few Indian investors to better understand how they're approaching investments, which sectors have their attention, and how to pitch them.",
        "img": "https://techcrunch.com/wp-content/uploads/2023/03/GettyImages-1339718258.jpg?resize=1200,900",
        "p_date": "2023-03-22T18:25:27Z",
        "source": {
            "id": "techcrunch",
            "name": "TechCrunch"
        },
        "title": "4 Indian investors explain how their investment strategy has changed since 2021",
        "url": "https://techcrunch.com/2023/03/22/4-indian-investors-explain-how-their-investment-strategy-has-changed-since-2021/"
    },
    {
        "author": "Amanda Silberling",
        "desc": "At a company that helps people find jobs, 2,200 employees will now have to embark on a job search of their own. Indeed laid off 15% of employees today, CEO Chris Hyams announced in an all-hands meeting. In a blog post, Hyams elaborated on the decision by expl…",
        "img": "https://techcrunch.com/wp-content/uploads/2023/03/GettyImages-1244460682.jpg?resize=1200,799",
        "p_date": "2023-03-22T18:21:49Z",
        "source": {
            "id": "techcrunch",
            "name": "TechCrunch"
        },
        "title": "Job listing platform Indeed lays off 2,200 employees",
        "url": "https://techcrunch.com/2023/03/22/job-listing-platform-indeed-lays-off-2200-employees/"
    },
    {
        "author": "Jay Peters",
        "desc": "The new “Creator Economy 2.0” pool is a new way for Epic to pay Fortnite creators. Forty percent of Fortnite’s net revenues will be given back to creators.",
        "img": "https://cdn.vox-cdn.com/thumbor/_uD97WV2v8D0_eTUimvC9wk695c=/0x0:1920x1080/1200x628/filters:focal(836x528:837x529)/cdn.vox-cdn.com/uploads/chorus_asset/file/24517269/Still025.jpg",
        "p_date": "2023-03-22T18:20:48Z",
        "source": {
            "id": "the-verge",
            "name": "The Verge"
        },
        "title": "Epic is going to give 40 percent of Fortnite’s net revenues back to creators",
        "url": "http://www.theverge.com/2023/3/22/23645633/fortnite-creator-economy-2-0-epic-games-editor-state-of-unreal-2023-gdc"
    },
    {
        "author": null,
        "desc": "The Federal Reserve on Wednesday raised interest rates by a quarter of a percentage point, but indicated it was on the verge of pausing further increases in borrowing costs amid recent turmoil in financial markets spurred by the collapse of two U.S. banks.",
        "img": "https://www.reuters.com/resizer/oIfe3n9D9LXDMZcpWmaGsiziLvk=/1200x628/smart/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/NYCEZWPXPJKGRD4L7MJP7HNYWQ.jpg",
        "p_date": "2023-03-22T18:17:10Z",
        "source": {
            "id": "reuters",
            "name": "Reuters"
        },
        "title": "Fed delivers small rate hike, says 'some additional' tightening possible",
        "url": "https://www.reuters.com/markets/rates-bonds/feds-powell-faces-political-storm-policy-minefield-over-svb-oversight-2023-03-22/"
    },
    {
        "author": "Lorenzo Franceschi-Bicchierai",
        "desc": "Kelly \"Aloria\" Lum was 41 when she passed away in New York City. She was a beloved member of the cybersecurity community, particularly in the city.",
        "img": "https://techcrunch.com/wp-content/uploads/2023/03/Patricio_Robayo_KellyLum2014-11.jpg?resize=1200,800",
        "p_date": "2023-03-22T17:32:40Z",
        "source": {
            "id": "techcrunch",
            "name": "TechCrunch"
        },
        "title": "Beloved hacking veteran Kelly ‘Aloria’ Lum passes away at 41",
        "url": "https://techcrunch.com/2023/03/22/kelly-aloria-lum-passes-away-at-41-obituary/"
    },
    {
        "author": "Benj Edwards",
        "desc": "Adobe trained new AI generator on Adobe Stock, licensed content, public domain.",
        "img": "https://cdn.arstechnica.net/wp-content/uploads/2023/03/adobe_firefly_hero-760x380.jpg",
        "p_date": "2023-03-22T17:27:41+00:00",
        "source": {
            "id": "ars-technica",
            "name": "Ars Technica"
        },
        "title": "Ethical AI art generation? Adobe Firefly may be the answer",
        "url": "https://arstechnica.com/information-technology/2023/03/ethical-ai-art-generation-adobe-firefly-may-be-the-answer/"
    },
    {
        "author": "Jonathan M. Gitlin",
        "desc": "It's the answer to a question we've been pondering for some time.",
        "img": "https://cdn.arstechnica.net/wp-content/uploads/2023/03/DB2023AU00181_large-760x380.jpg",
        "p_date": "2023-03-22T17:16:46+00:00",
        "source": {
            "id": "ars-technica",
            "name": "Ars Technica"
        },
        "title": "VW will support Android Automotive for the “lifetime” of a car—15 years",
        "url": "https://arstechnica.com/cars/2023/03/android-infotainment-will-be-supported-for-at-least-15-years-vw-says/"
    },
    {
        "author": null,
        "desc": "Johnson & Johnson <a href=\"https://www.reuters.com/companies/JNJ.N\" target=\"_blank\">(JNJ.N)</a> said on Wednesday that it would ask the U.S. Supreme Court to revive its effort to resolve tens of thousands of lawsuits over its talc products through the bankrup…",
        "img": "https://www.reuters.com/resizer/3ua0j2WcVxLnysCj-zZXlgwLz24=/1200x628/smart/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/K75IOUA6GRIZXPD5JVU5PCKLGE.jpg",
        "p_date": "2023-03-22T17:13:42Z",
        "source": {
            "id": "reuters",
            "name": "Reuters"
        },
        "title": "J&J to seek U.S. Supreme Court review on unit's bankruptcy",
        "url": "https://www.reuters.com/legal/jj-seek-us-supreme-court-review-units-bankruptcy-2023-03-22/"
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
## Requirements
The user can perform the following functions:

- See various news sources on the homepage of the application
- Select a news source and see all news articles from the selected news source in the application.
- See the image, description and the time a news article was created.
- Click on an article and read the full article on the source website.


## Technologies
- python 3.11




## Contact Information


