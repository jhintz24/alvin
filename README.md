# Alvin
Speech-driven application development

## Idea
Alvin is an tool for developing apps (particularly user interfaces) through natural language interpretation, which could ultimately reduce development time and increase app development accessibility. 

I've found that mapping out app screens in my head is relatively easy, but translating those screens from my brain to computer code takes effort and time, even for languages that I know well. It would be neat if I could just talk to the computer and describe what I want in natural language, and have the computer understand and build the screens for me. For example, telling the computer to 
>*"Add a label that says 'Hello World'"* 

is trivial. Telling it to 
>*"Create an app with five screens. The first is a standard login screen with textfields for username and password"* 

is certainly more complex but still within the same domain. Of course coding UIs and coding complex logical behavior are two different beasts, but certainly simple logic could be explained to a computer through natural language. Telling the computer to 
>*"Increase the top label by one everytime the user presses the button at the bottom"* 

is just about as simple as any UI descripton. Telling the computer to 
>*"Display a success popup whenever the program retreives new information from the Twitter API"* 

is more difficult but again, still within the same domain. A command such as 
>*"Create an app that allows me to talk with my friends"* 

is of course too vague, but the computer can start with an initial screen and ask the developer to clarify and drill down into details. 

However possible/practical, it is an intriguing and fun idea.

## Scope
The current version of Alvin is more of a proof-of-concept than a fully usuable assistant. But of course the goal is to get there one day.

## Implementation
*Conceptually*, Alvin has two parts:
1. A part to listen to the user and translate their voice into meaningful commands (essentially NLP)
2. A part to write an app based on these commands. More specifically, Alvin will literally write code in whatever language is chosen and output an app that can be run independently, just like any other app of that language.

*Functionally*, Alvin has four main classes:
1. A voice interpretter (voice-to-text)
2. A command interpretter (text-to-command)
3. A UI abstract (to hold the app structure dictated by the commands)
4. An output writer (to write the app from the UI abstract). Alvin can write out an app from the UI abstract in any language for which it has an output writer (i.e. Tkinter, PyQt, etc.)

I've chosen to write Alvin in Python because of Python's flexibility and NLP libraries. I also know it the best :)

## Running Alvin
Alvin is built to run using Python 3.7.4. You can [download and install Python directly](https://www.python.org/downloads/) or you can download a handy [Anaconda distribution](https://www.anaconda.com/distribution/).

To run Alvin:
```python
python alvin.py -appname YOUR_APP_NAME
```
and replace YOUR_APP_NAME with the name of the output app (i.e. cool-app.py)

## Commands
Alvin can currently handle commands for text, color, position, and basic events for buttons and labels. Example commands include:
* "Create a new app"
* "Add a label that says 'hello world'"
* "Make the label blue"
* "Add a button that says press me"
* "Move the label to the bottom"
* "Change the button color to red"
* "Make the label say "it worked" when I press the button"
* "Move the button to the right"
* "Remove the label"

## Third-Party Tools
Alvin uses the following third-party tools:
1. [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) and [PyAudio](http://people.csail.mit.edu/hubert/pyaudio/#downloads) for translating voice-to-text.
2. [Spacy](https://spacy.io/) for lemmanizing individual words before they are turned into commands. A "lemma" is the canonical or dictionary root word for any given set of words. For example, "worry" is the lemma of "worries, worried, etc.". Spacy also provides a tokenizer, but I chose to build my own because of Alvin's specific (and simple) use cases.
3. [Tkinter](https://docs.python.org/3/library/tkinter.html) for the graphical user interface builder. I chose Tkinter over PyQt for it's simplicity.

