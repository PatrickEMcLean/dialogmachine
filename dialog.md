
# Learning How to Use Dialog Machine

## Description:

*Patrick, hunched over his computer struggles to make a useful tool for writing interactive dialog. He jumps slightly as you enter the room, but then, recognizing you, he smile and begins to speak.*


## dialog:

Patrick: This is a simple tool to preview interactive dialogs. In the root folder you will find a file called dialog.md. It's a valid [markdown file.](https://www.markdownguide.org/cheat-sheet/)  So you can edit that file with any text editor you like. Just make sure it's saved as plain text  with an .md ending

When you run render.py by entering this in Powershell or the Mac Terminal

`python render.py`

The script then reads the dialog file, creating a unique page for every section of markdown inbetween the dash delimiters. But, if you put links in the text file (and/or images) you can build a clickable preview of interactive dialog simply by typing. Which is cool.

You: So what do I do now?

Patrick: You have choices.


# choices:

[How is the dialog file is structured?](file_structure.html)

[Love it, what's next?](whats_next.html)

[Jesus, you're weird!](weird.html)


---

# file_structure

## Description

*Patrick is happy to explain. He's please with himself, even though he just got GPT-4 to do most of the work.*

## dialog

PATRICK: The dialog.md file isn't structured. It's just Markdown, but if you use the sections in the same way every time. It works. 

The trick (if you can call it a trick) is the links -- so do this

 ` [dialog or player choice](Heading.html) `

Then, if you have this in the dialog.md file. 

```

# Heading

yada yada yada, stuff goes here

```

It will render the content in that section into a page called 'headling.html' and your link will be good. 

But you can't have any empty spaces in the heading description. 

So "File Structure" won't work, but "File_Structure" will. 

# choices:

[Meh.](https://meh.com/)

[Love it, what's next?](what's_next.html)

[Why did you do this?](why.html)

---

# whats_next

## Description

*Patrick shakes his head and sighs. He understands the challenge. User's break everything. But still, this might be the start of something*

## Dialog

Patrick: I mean, it's held together with bailing wire. And maybe this only makes sense to me. 

- I'd make the links so you don't have to type html. 
- I'd love to have a folder watcher that rebuilds every time you save. 
- Spin up a server for a local preview? 
- How do you organize a larger collection of dialogs? Maybe we should be able to inlcude other files? YAML header info? 
- Do some validation on them or parsing them so they don't break if you leave a space in there or (heaven forbid) and apostrophe
- some kind of visualizer for link structure
- link validation?
- better styling
- (and everything else)


## Choices

[Jesus, you're weird!](weird.html)

---

# why



## dialog:

Patrick: Well, 

1. I believe in prototyping things as rapidly as possible. 
2. I also believe in flat text files. And LOVE, LOVE, LOVE Markdown.
3. Git is the best system ever invented for managing large text files across a distributed team. And scripts are just large text files. It just make sense to my brain that that we should use git and/or github to manage the massive amount of story and script. 

You can't search across a directory of word docs. Or do find and replace across them. It's also not easy to chunk up word docs and feed them to an LLM for Document Assisted Retrieval. but if we had ALL of the documents in flat files we could do all of that and more. 

And we could probably parse it into OEI so some poor bastard doesn't waste their life retyping a smell writer's word doc. 

## Choices:

[Jesus, you're weird!](weird.html)

[You're right. It worked for that plain-text screenplay format](https://fountain.io/)


---

# weird

<iframe src="https://giphy.com/embed/TL6poLzwbHuF2" width="480" height="354" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/big-dude-jeff-TL6poLzwbHuF2">via GIPHY</a></p>

## Choices:

[Why did you do this?](why.html)

[Okay, fine, what's next?](whats_next.html)

