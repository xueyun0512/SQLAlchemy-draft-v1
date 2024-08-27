from flask import render_template, request, redirect, url_for
from models import Person

def register_routes(app, db):
    @app.route("/", methods=["GET", "POST", "DELETE"])
    def index():
        if request.method=="GET":
            people = Person.query.all()
            return render_template("index.html", people = people)
        
        elif request.method=="POST":
            name = request.form["name"]
            age = int(request.form["age"])
            job = request.form["job"]
            
            new_user = Person(name=name, job=job, age=age)
            db.session.add(new_user)
            db.session.commit()

            people = Person.query.all()
            #return render_template("index.html", people = people)
            return redirect(url_for('index'))


    @app.route('/delete/<int:pid>')
    def delete(pid):
        user_to_delete = Person.query.get_or_404(pid)

        try:
            db.session.delete(user_to_delete)
            db.session.commit()
            return redirect(url_for('index'))
        except:
            return "There was a problem deleting that user"


    @app.route("/details/<pid>", methods=["DELETE"])
    def details(pid):
        person = Person.query.filter(Person.pid==pid).first()
        return render_template("details.html", person=person)