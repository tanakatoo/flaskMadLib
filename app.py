from flask import Flask, request, render_template
from stories import Story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ohsosecret'
debug=DebugToolbarExtension(app)

@app.route('/')
def make_story():
    return render_template('make_story.html')

@app.route('/fill-in-the-blanks', methods=["POST"])
def story():
    prompts = request.form["prompts"]
    prompts = prompts.split(',')
    text = request.form['story-text']
    s = Story(prompts,text)
    return render_template('fill-in.html', prompts=prompts,text=text)

@app.route('/story', methods=["POST"])
def return_story():
    # text=request.form['story-text']
    prompts=request.form
    # prompts_to_dict(prompts)
    # print(prompts)
    text = s.generate(prompts)
    
    
    # dictionary_prompts= prompts_to_dict(prompts)
    return render_template('the_story.html', text=text)

def prompts_to_dict(prompts):
    
    # prompts = prompts.split(',')
    dictionary_prompts={}
    for s in prompts:
        s=s.strip()
        dictionary_prompts[s]=''
    return dictionary_prompts