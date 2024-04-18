from django.shortcuts import render, redirect
from django.urls import reverse
from random import choice

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


# Reads markdown file and returns html with content of markdown
def title(request, title):
    entries = util.list_entries()
    # If title not in entries return error page
    html_content = util.mark_to_html(title)
    if not html_content:
        # Check if something like title in entries
        for entrie in entries:
            if title.lower() in entrie.lower():
                html_content = util.mark_to_html(entrie)
                return render(request, "encyclopedia/title.html", {
                    "title": html_content,
                    "file_name": title,
                })
        return render(request, "encyclopedia/error.html", {
            "message": "Page " + title + " found."
        })
    else:
        # return title page
        return render(request, "encyclopedia/title.html", {
            "title": html_content,
            "file_name": title,
        })


# Redirects to page you searched for
def search(request):
    if request.method == "POST":
        q = request.POST["q"]
        return redirect(reverse("title", args=[q]))
    else:
        return redirect("/")


# Add new page to wiki
def new(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        if util.get_entry(title):
            return render(request, "encyclopedia/error.html", {
                "message": "Page already exists"
            })
        else:
            util.save_entry(title, content)
            print(title, content)
            return redirect(reverse("title", args=[title]))
    else:
        return render(request, "encyclopedia/new.html")


# Edit existing page
def edit(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = util.get_entry(title)
        if not content:
            return render(request, "encyclopedia/error.html", {
                "message": "Page not found."
            })
        else:
            return render(request, "encyclopedia/edit.html", {
                "title": title,
                "content": content,
            })
    else:
        return redirect("/")


# Saves edits
def confrim(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title, content)
        return redirect(reverse("title", args=[title]))
    else:
        return render(request, "encyclopedia/new.html")


# Returns random page
def random(request):
    if request.method == "GET":
        random_item = choice(util.list_entries())
        return redirect(reverse("title", args=[random_item]))
    else:
        return redirect("/")


def fail(request):
    return redirect("/")
