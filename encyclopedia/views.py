from django.contrib import messages
from django.shortcuts import redirect, render
from markdown2 import Markdown
from random import randint
from . import forms
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    

def wiki(request, title):
    entry = util.get_entry(title)
    if entry:
        return render(request, "encyclopedia/entry.html", {
           "title": title, "entry": Markdown().convert(entry),
        })
    else:
        return render(request, "encyclopedia/404.html", {
            "msg": "Entry not found.",
        })


def search(request):
    query = request.GET.get("q", "")
    entries = util.list_entries()
    if query in entries:
        return redirect(f"/wiki/{query}")
    subStrings = [entry for entry in entries if query in entry]
    return render(request, "encyclopedia/search.html", {
        "query": query, "entries": subStrings,
    })

def new(request):
    entries = util.list_entries()
    if request.method == "POST":
        form = forms.NewEntryForm(request.POST)
        if form.is_valid():
            newEntry = form.cleaned_data["entryName"]
            markDown = form.cleaned_data["markDown"]
            if newEntry in entries:
                messages.error(request, "Entry already exists.")
                redirect("/new")
            util.save_entry(newEntry, markDown)
            messages.success(request, "New entry made.")
            return redirect(f"/wiki/{newEntry}")
    return render(request, "encyclopedia/new.html", {
        "form": forms.NewEntryForm()
    })

def edit(request, title):
    entry = util.get_entry(title)
    if not entry:
        return render(request, "encyclopedia/404.html", {
            "msg": "Entry not found.",
        })
    if request.method == "POST":
        form = forms.EditEntryForm(request.POST)
        if form.is_valid():
            markDown = form.cleaned_data["markDown"]
            util.save_entry(title, markDown)
            messages.succes(request, "Entry edited.")
            return redirect(f"/wiki/{title}")
    return render(request, "encyclopedia/edit.html", {
        "title": title, "form": forms.EditEntryForm()
    })

def random(request):
    entries = util.list_entries()
    entryNum = randint(0, len(entries) - 1)
    entry = entries[entryNum]
    return redirect(f"/wiki/{entry}")
