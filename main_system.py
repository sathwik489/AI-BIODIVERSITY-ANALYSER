from flask import Flask,render_template,request
from species_detector import detect_species
import json,webbrowser
from datetime import datetime
app=Flask(__name__)
def update_stats(species):
    with open("species_stats.json","r") as f:
        stats=json.load(f)

    name=species.capitalize()

    if name in stats:
        stats[name]+=1
    else:
        stats[name]=1

    with open("species_stats.json","w") as f:
        json.dump(stats,f)

    return stats

@app.route('/',methods=['GET','POST'])
def home():

    if request.method=='POST':

        file=request.files['image']
        img_path="static/animal.jpg"
        file.save(img_path)

        species,confidence=detect_species(img_path)

        stats=update_stats(species)

        return render_template(
        "index.html",
        species=species,
        confidence=confidence,
        stats=stats,
        now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

    with open("species_stats.json","r") as f:
        stats=json.load(f)

    return render_template("index.html",stats=stats)

if __name__=="__main__":

    webbrowser.open("http://127.0.0.1:5000")

    app.run(debug=True)