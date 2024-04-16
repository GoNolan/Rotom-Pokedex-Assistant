# The Rotom Pokedex Assistant Prototype
This is a web application designed for use by public library partrons, in particular child and teen patrons, to ask questions about the specific mechanics of certain video games, in this instance, Pokemon. The application can help patrons to determine a helpful strategy within the video games combat mechanics by determining the appropriateness of a choice of pokemon based on factors of pokemon level and type matchups.

# Contents
- [Installation]
- [Usage]
- [License]
- [Folder]

## Installation
1. Set up API Key:
    setx OPENAI_API_KEY "API-key-found-in-.env"

2. Run app:
    python -m flask --app rotomassistant run

3. Modifying the GenAI:
    The AI's code determining its answers can be changed on line 19 in the rotomassistant.py file. For simplicity:
        "role", "system", "content": "Modify-the-wording-in-these-quotation-marks-or-rewrite-with-rules-on-answering-questions-apout-different-topics-or-video-games"

## Usage
1. Input queston on the topic of understanding the mechanics of the Pokemon video game combat in the application textbox to supply data for the GenAI assistant to answer

2. Provide a resource for library patrons to access easy to miss information regarding the Pokemon video games

3. Provides a framework for library staff to develop more GenAI assistants to support library patron inquiries into video games with Python code

### Using the Application
As an example of what can be asked of the Rotom Assistant application, consider trying one of the following prompts. These prompts are not meant to be perfect examples of what can be asked of the application. They are prompts that show both the potential benefits and drawbacks of the information the AI delivers:
    I have a normal and flying type Pidgeot. It is level 42. It is fighting against an electric type Electabuzz. The Electabuzz is level 40. What do you think about this?

    I do not know what to do about this pokemon. I am fighting a level 25 Scyther. My Grumpig is also level 25. It is a psychic type pokemon. Is it a good idea to use my Grumpig against this Scyther?

    Is Milotic a good choice to face off against a Pidove?

## License
This project is licensed under the [MIT License]

## Folder
### INFO6620_Final Folder
The main folder contains three separate folders: '_pycache_', 'static', and 'templates'. Several items in the folder are not separated into any of the three folders. They are as follows:

#### .env
'.env' is associated with the flask app. It contains the API Key that is used to connect the program to OPENAI. It is included within the .gitignore file.

#### .gitignore
'.gitignore' contains the various programs that Git should continue to leave untracked when using the application, including the '.env' and '_pycache_' files.

#### rotomassistant.py
This is the primary application code. It instructs the app on what functions to carry out and what processes it takes to use data to deliver messages from the OPENAI. It also includes the code that establishes the paramaters of the AI's responses to any user prompts. It is named after the pokemon 'Rotom'.

#### LICENSE
The license is the legal statement denoting the parties that can access and modify the included application code.

#### README
What you are currently reading. A document that outlines the various, necessary information required to run the application.

#### requirements.txt
A list of the necessary programs and systems required to properly run and access the application. These programs are not a part of the 'INFO6620_Final' folder, and must be installed in the computer running the program.

### templates
#### index.html
This is the .html file for the web application's front end.

### static
#### pokeball_icon.png
An image file for an icon associated with the image of a pokeball, an item significant to the Pokemon video games. It is an identical file to 'pokeball.png, and is not mapped to the application of the .html file.

#### pokeball.png
An image file for the logo associated with the image of a pokeball, an item significant to the Pokemon video games. This image is mapped onto the application's front end through the 'main.css' and 'index.html' files.

#### Rotom_Dex.png
An image file of the Pokemon Rotom, in its Pokedex form. This image is mapped onto the application's front end through the 'main.css' and 'index.html' files

#### main.css
The code that determines the visual layout of the web application's front end.

### _pycache_
This folder holds the cached code of 'rotomassistant.py', present in a file named 'rotomassistant.cpython-32.pyc'. It is included in the list found in '.gitignore'.
