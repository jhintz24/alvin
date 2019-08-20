# Alvin
## Speech-driven application development

### Idea
As the subtitle implies, Alvin is a tool for developing apps (particularly user interfaces) through natural language interpretation, which could ultimately reduce development time and increase app development accessibility. 

I'm an app developer and I often find myself with an idea for an app. Mapping out the screens in my head is easy, but translating those screens from my brain to computer code takes effort and time, even for languages that I know well. I've always thought it would be neat if I could just talk to the computer and describe what I want in natural language, and have the computer understand and build the screens for me. For example, telling the computer to *"add a label that says 'Hello World'"* is trivial. Telling it to *"create an app with five screens. The first is a standard login screen with textfields for username and password"* is certainly more complex but still within the same domain. Now coding UIs and coding complex behavior and logic are two different beasts, but certainly simple logic could be explained to a computer through natural language. Telling the computer to *"increase the top label by one everytime the user presses the button at the bottom"* is just about as simple as any UI descripton. Telling the computer to *"display a success popup whenever the program retreives new information from the Twitter API"* is more difficult but again, still within the same domain. A command such as *"create an app that allows me to talk with my friends"* is of course too vague, but the computer can start with an initial screen and ask the developer to clarify and drill down into details. It's an intriguing idea and I'm sure it's been explored before at some point somewhere, but regardless I thought it would be fun to try and code it.

### Scope
The current incarnation of Alvin is meant more as a proof-of-concept than a fully usuable assistant. But of course the goal is to get there one day.

### Implementation
Conceptually, Alvin has three parts:
1. A part to listen to the user and translate their voice into meaningful commands (essentially NLP)
2. A part to build an abstracted model of the UI and logic from these commands.
3. A part to write an app from this abstracted model. More specifically, Alvin will literally write code in whatever language is chosen and output an app that can be run independently, just like any other app of that language. The beauty is that from the abstracted model, Alvin can write out in any language for which it has an interpretter. 

I've chosen to write Alvin in Python because of it's ease of use, flexibility, and NLP libraries. I also know it the best :)

Functionally (at least how I've coded it), Alvin has four main classes:
1. A voice interpretter (voice-to-text)
2. A command interpretter (text-to-command)
3. A UI abstract (to hold the app structure dictated by the commands)
4. An output writer (to write the app from the UI abstract)


