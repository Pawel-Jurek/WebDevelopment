import random
from django.shortcuts import redirect, render
import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, word=None):   
    isSubstring = False
    actualTitle = ""
    possibleWords = [] 
    if word == None:
        word = request.GET.get('q')
    
    if util.get_entry(word) is None:             
        for entry in util.list_entries():
            if word.lower() in entry.lower():
                possibleWords.append(entry)
        
        entry_html = None
        if possibleWords:
            isSubstring = True
        else:
            possibleWords.append(word)
               
    else:
        actualTitle = word
        entry_html = markdown.markdown(util.get_entry(word))

    return render(request, "encyclopedia/wiki.html",{
    "entry": entry_html,
    "isSubstring": isSubstring,
    "possibleWords": possibleWords,
    "actualTitle": actualTitle
})


def newPage(request):
    duplicate = False
    title = ""
    text = ""
    if request.method == "POST":
        title = request.POST.get('titleText')
        text = request.POST.get('bodyText')
        if util.get_entry(title) is None:
            util.save_entry(title, f"# {title}\n\n{text}")
            return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
            })
        else:
            duplicate = True
            #to ma wrócić do formularza i wyświetlić alert
            return render(request, "encyclopedia/newPage.html", {
        "titlebox": title,
        "maintext": text,
        "duplicate": duplicate
            })

    return render(request, "encyclopedia/newPage.html", {
        "entries": util.list_entries()
    })

def getBodyText(markdownText):
    text = markdownText[markdownText.find("\n")+3:]
    return text

def updatePage(request, title):
    text = getBodyText(util.get_entry(title))
    if request.method == "POST":
        util.save_entry(title, f"# {title}\n\n{request.POST.get('bodyText')}")
        return redirect('wiki', word = title)
    return render(request, "encyclopedia/updatePage.html", {
        'text': text,
        'title': title
    })

def randomPage(request):
    entries = util.list_entries()
    random_number = random.randint(0, len(entries)-1)
    print(entries[random_number])
    return redirect('wiki', word=entries[random_number])

