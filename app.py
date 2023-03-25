from stories import Story, story
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'peepsluvr'
debug = DebugToolbarExtension(app)

@app.route('/')
def show_madlibs_form():
    # iterate through story.prompts, each prompt is the label for each input
    prompts = story.prompts
        
    return render_template('madlib-form.html', prompts=prompts)

@app.route('/story')
def get_story():
    """ creates a story from Story instance when answers are passed to story.generate() """
    # display story.template
    
    # story.generate({}) takes as an arg a dictionary
    # key/value pairs in this dict {prompt: answer}
    #print(request.args)
    answers_dict = dict(request.args)
    # [('place', 'the ocean'), ('noun', 'mermaid'), ('verb', 'sings'), ('adjective', 'loudly'), ('plural_noun', 'dinglehoppers')]
    
    generated_story = story.generate(answers_dict)
    return render_template('story.html', paragraph=generated_story)