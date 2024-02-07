from django.shortcuts import render
from markdown2 import Markdown
import random
from django.shortcuts import redirect

from . import util

# Function to convert Markdown content to HTML
def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

# View function for the index page
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# View function for displaying a specific entry
def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html", {
            "message": "There is no such entry."
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })

# View function for handling search requests
def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        html_content = convert_md_to_html(entry_search)
        if html_content is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": entry_search,
                "content": html_content
            })
        else:
            # If no exact match is found, suggest similar entries
            allEntries = util.list_entries()
            rcmmndtn = []
            for entry in allEntries:
                if entry_search.lower() in entry.lower():
                    rcmmndtn.append(entry)
            return render(request, "encyclopedia/search.html", {
                "rcmmndtn": rcmmndtn
            })

# View function for creating a new page
def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleExist = util.get_entry(title)
        if titleExist is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "Entry page already exists"
            })
        else:
            util.save_entry(title, content)
            return redirect('entry', title=title)
        
# View function for editing an existing page
def edit(request):
    if request.method == 'POST':
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })
        
        
# View function for saving edits to a page
def save_edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convert_md_to_html(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })

# View function for displaying a random entry
def rand(request):
    allEntries = util.list_entries()
    rand_entry = random.choice(allEntries)
    html_content = convert_md_to_html(rand_entry)
    return render(request, "encyclopedia/entry.html", {
        "title": rand_entry,
        "content": html_content
    })
