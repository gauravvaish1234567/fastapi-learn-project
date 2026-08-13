from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app = FastAPI()

templates = Jinja2Templates(directory="templates") #to get html templates 

app.mount("/assets", StaticFiles(directory="assets"), name="assets") #to mount assests for html page

posts = {
    "Technology": [
        {
            "image": "img/blog/blog-post-3.webp",
            "date": "Apr. 14th, 2025",
            "title": "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
            "url": "blog-details.html"
        }
    ],

    "Security": [
        {
            "image": "img/blog/blog-post-portrait-1.webp",
            "date": "Apr. 14th, 2025",
            "title": "Sed do eiusmod tempor incididunt ut labore",
            "url": "blog-details.html"
        }
    ],

    "Career": [
        {
            "image": "img/blog/blog-post-9.webp",
            "date": "Apr. 14th, 2025",
            "title": "Ut enim ad minim veniam, quis nostrud exercitation",
            "url": "blog-details.html"
        }
    ],

    "Cloud": [
        {
            "image": "img/blog/blog-post-7.webp",
            "date": "Apr. 14th, 2025",
            "title": "Adipiscing elit, sed do eiusmod tempor incididunt",
            "url": "blog-details.html"
        }
    ],

    "Programming": [
        {
            "image": "img/blog/blog-post-6.webp",
            "date": "Apr. 14th, 2025",
            "title": "Excepteur sint occaecat cupidatat non proident",
            "url": "blog-details.html"
        }
    ],

    "Health": [
        {
            "image": "img/blog/blog-post-6.webp",
            "author": "William G.",
            "date": "28 April 2024",
            "title": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem",
            "url": "blog-details.html"
        }
    ],

    "Education": [
        {
            "image": "img/blog/blog-post-7.webp",
            "author": "Emma D.",
            "date": "30 May 2024",
            "title": "Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis",
            "url": "blog-details.html"
        }
    ],

    "Gaming": [
        {
            "image": "img/blog/blog-post-5.webp",
            "author": "James F.",
            "date": "3 June 2024",
            "title": "Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit",
            "url": "blog-details.html"
        },
        {
            "image": "img/blog/blog-post-6.webp",
            "date": "6 April 2026",
            "title": "Quis autem vel eum iure reprehenderit qui in ea voluptate",
            "read_time": "2 mins read",
            "url": "blog-details.html"
        },
        {
            "image": "img/blog/blog-post-9.webp",
            "date": "12 June 2026",
            "title": "At vero eos et accusamus et iusto",
            "read_time": "2 mins read",
            "url": "blog-details.html"
        },
        {
            "image": "img/blog/blog-post-10.webp",
            "date": "9 May 2026",
            "title": "Et harum quidem rerum facilis est et expedita distinctio",
            "read_time": "2 mins read",
            "url": "blog-details.html"
        },
        {
            "image": "img/blog/blog-post-2.webp",
            "date": "15 July 2026",
            "title": "Nam libero tempore, cum soluta nobis est eligendi",
            "read_time": "2 mins read",
            "url": "blog-details.html"
        },
        {
            "image": "img/blog/blog-post-1.webp",
            "date": "18 August 2026",
            "title": "Temporibus autem quibusdam et aut officiis debitis",
            "read_time": "2 mins read",
            "url": "blog-details.html"
        },
        {
            "image": "img/blog/blog-post-3.webp",
            "date": "21 September 2026",
            "title": "Itaque earum rerum hic tenetur a sapiente delectus",
            "read_time": "2 mins read",
            "url": "blog-details.html"
        }
    ],

    "Politics": [
        {
            "image": "img/blog/blog-post-1.webp",
            "author": "Maria Doe",
            "date": "Jan 1, 2022",
            "title": "Dolorum optio tempore voluptas dignissimos",
            "url": "blog-details.html"
        },
        {
            "image": "img/blog/blog-post-5.webp",
            "author": "Denis Peterson",
            "date": "Jan 30, 2022",
            "title": "Accusamus quaerat aliquam qui debitis facilis consequatur",
            "url": "blog-details.html"
        }
    ],

    "Sports": [
        {
            "image": "img/blog/blog-post-2.webp",
            "author": "Allisa Mayer",
            "date": "Jun 5, 2022",
            "title": "Nisi magni odit consequatur autem nulla dolorem",
            "url": "blog-details.html"
        },
        {
            "image": "img/blog/blog-post-4.webp",
            "author": "Lisa Neymar",
            "date": "Jun 30, 2022",
            "title": "Non rem rerum nam cum quo minus olor distincti",
            "url": "blog-details.html"
        }
    ],

    "Entertainment": [
        {
            "image": "img/blog/blog-post-3.webp",
            "author": "Mark Dower",
            "date": "Jun 22, 2022",
            "title": "Possimus soluta ut id suscipit ea ut in quo quia et soluta",
            "url": "blog-details.html"
        },
        {
            "image": "img/blog/blog-post-6.webp",
            "author": "Mika Lendon",
            "date": "Feb 14, 2022",
            "title": "Distinctio provident quibusdam numquam aperiam aut",
            "url": "blog-details.html"
        }
    ]
}
@app.get("/")
def hello():
    return {"message":"best of luck work hard!!!"}

#DATA APIS

@app.get("/posts")
def get_posts():
    return posts


#PAGES ROUTES

@app.get("/home")
def home(request:Request):
    return templates.TemplateResponse(request, "index.html", {"posts": posts})