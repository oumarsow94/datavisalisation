import psycopg2 as psy
import psycopg2.extras
from flask import Flask, Markup, render_template
from statistics import mean

app = Flask(__name__)

#----------------------Partie connexion à la base de données--------------------
def connectToDB():
    try:
    #  connectionString = 'dbname=music user=postgres password=kirbyk9 host=localhost'
        connection = psy.connect(user='nfqvwjhghbundx',
                                host='ec2-54-225-106-93.compute-1.amazonaws.com',
                                port='5432',
                                password='3cc1e5096c4e1b4f46589b8c36d61b4ca4079cbd1e351a940c5cd1ed79f35dc8',
                                database = 'd2uqbapnjb9stj'
                                )
        return connection
    except(Exception) as error:

        print("Probleme de connexion au serveur PostgreSQL", error)
connection = connectToDB()
curseur = connection.cursor()


@app.route('/')
def bar():
    a=list()
    connection = connectToDB()
    curseur = connection.cursor()
    curseur.execute("SELECT jan,fevrier,mar,avril,mai,juin,juillet,aout,septembre,octobre,novembre,decembre FROM vente WHERE type_produit='smartphones'")
    projects = curseur.fetchall()

    curseur.close()
    labels=list()
    # print(projects)
    for d in projects:
        labels.append(d)
        listes = list(sum(labels, ()))
        sm = mean(listes)
    a.append(sm)
    # print(sm)
    data = [d[1] for d in projects]

    connection = connectToDB()
    curseur = connection.cursor()
    curseur.execute("SELECT jan,fevrier,mar,avril,mai,juin,juillet,aout,septembre,octobre,novembre,decembre FROM vente WHERE type_produit='informatiques'")
    project = curseur.fetchall()
    curseur.close()
    liste = list()
    for d in project:
        liste.append(d)
        data = list(sum(liste, ()))
        inf = mean(data)
    a.append(inf)

    connection = connectToDB()
    curseur = connection.cursor()
    curseur.execute("SELECT jan,fevrier,mar,avril,mai,juin,juillet,aout,septembre,octobre,novembre,decembre FROM vente WHERE type_produit='electromenagers'")
    projec = curseur.fetchall()
    curseur.close()
    data1 = list()
    for d in projec:
        data1.append(d)
        liste = list(sum(data1, ()))
        ref = mean(liste)
    a.append(ref)
    print(a)
    return render_template('dashboard.html',listes=listes, data=data, liste=liste,a=a)
 
 
if __name__ == "__main__":
    app.run(debug=True)
