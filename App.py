#!/usr/bin/env python3
from flask import Flask, render_template, request, url_for, redirect, flash
from flask import jsonify, make_response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import base, Country, Club, User
from flask import session as login_session
import random
import string
import httplib2
import json
import requests

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

app = Flask(__name__)

CLIENT_ID = json.loads(open('client_secret.json',
                            'r').read())['web']['client_id']
APPLICATION_NAME = 'Top Clubs'
engine = create_engine('sqlite:///clubs.db',
                       connect_args={'check_same_thread': False},
                       echo=True)
base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def createUser():
    newUser = User(name=login_session['username'],
                   email=login_session['email'],
                   picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def userinfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def userID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return False


@app.route('/login/')
def login():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid State Parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    code = request.data

    try:
        ouath_flow = flow_from_clientsecrets('client_secret.json', scope='')
        ouath_flow.redirect_uri = 'postmessage'
        credentials = ouath_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(json.dumps('Failed to upgrade\
                                            the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)  # noqa
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])

    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(json.dumps("Token's user ID doesn't\
                                            match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print ("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')

    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps
                                 ('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    UserExist = userID(login_session['email'])

    if UserExist:
        login_session['user_id'] = UserExist
    else:
        createUser()
        login_session['user_id'] = UserExist

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;\
                -webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print ("done!")
    return output


@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print('Access token is none')
        response = make_response(json.dumps('Current User Is Not\
                                            Connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    print 'In gdisconnect access token is %s', access_token
    print 'Username is: '
    print login_session['username']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']  # noqa
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        flash('Successfully Logged-out')
        return redirect('/main')
    else:
        response = make_response(json.dumps('Failed to revoke token for\
                                 given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


@app.route('/')
@app.route('/main/')
def main():
    countries = session.query(Country)
    latest = session.query(Club).order_by(Club.id.desc()).limit(5).all()
    return render_template('main.html', countries=countries, latest=latest)


@app.route('/<coun>/')
def clubs(coun):
    country = session.query(Country).filter_by(name=coun).one()
    teams = session.query(Club).filter_by(Country_id=country.id)
    return render_template('clubs.html', country=country, teams=teams)


@app.route('/<coun>/<int:club_id>/')
def club(coun, club_id):
    country = session.query(Country).filter_by(name=coun).one()
    team = session.query(Club).filter_by(Country_id=country.id
                                         ).filter_by(id=club_id).one()
    creator = userinfo(team.user_id)
    if 'username' in login_session:
        if login_session['email'] == creator.email:
            return render_template('desc.html', team=team)
        else:
            return render_template('desc_public.html', team=team)
    else:
        return render_template('desc_public.html', team=team)


@app.route('/newclub/', methods=['GET', 'POST'])
def new_club():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        club = Club(name=request.form['name'],
                    description=request.form['description'],
                    Country_id=request.form['coun'],
                    user_id=login_session['user_id'])
        session.add(club)
        session.commit()
        flash('New Club Added!')
        return redirect(url_for('main'))
    else:
        return render_template('New Club.html')


@app.route('/<int:club_id>/edit', methods=['GET', 'POST'])
def edit_club(club_id):
    EditedClub = session.query(Club).filter_by(id=club_id).one()
    creator = userinfo(EditedClub.user_id)
    if 'username' not in login_session:
        return redirect('/login')
    if login_session['email'] != creator.email:
        return redirect('/login')
    if request.method == 'POST':
        if request.form['name']:
            EditedClub.name = request.form['name']
        if request.form['description']:
            EditedClub.description = request.form['description']
        session.add(EditedClub)
        session.commit()
        flash('Club Data Updated!')
        return redirect(url_for('main'))
    else:
        return render_template('EditClub.html', club_id=club_id,
                               EditedClub=EditedClub)


@app.route('/<int:club_id>/delete', methods=['GET', 'POST'])
def delete_club(club_id):
    DeletedClub = session.query(Club).filter_by(id=club_id).one()
    creator = userinfo(DeletedClub.user_id)
    if 'username' not in login_session:
        return redirect('/login')
    if login_session['email'] != creator.email:
        return redirect('/login')
    if request.method == 'POST':
        session.delete(DeletedClub)
        session.commit()
        flash('Club Deleted!')
        return redirect(url_for('main'))
    else:
        return render_template('Delete Club.html', club_id=club_id,
                               DeletedClub=DeletedClub)


@app.route('/main/json')
def MainJson():
    clubs = session.query(Club).all()
    return jsonify(Clubs=[i.serialize for i in clubs])


@app.route('/<coun>/json')
def ClubsJson(coun):
    country = session.query(Country).filter_by(name=coun).one()
    teams = session.query(Club).filter_by(Country_id=country.id)
    return jsonify(Clubs=[i.serialize for i in teams])


@app.route('/<coun>/<int:club_id>/json')
def clubJson(coun, club_id):
    country = session.query(Country).filter_by(name=coun).one()
    team = session.query(Club).filter_by(Country_id=country.id
                                         ).filter_by(id=club_id).one()
    return jsonify(Club=team.serialize)


@app.route('/About')
def about():
    return render_template('About.html')

if __name__ == "__main__":
    app.secret_key = 'Obba'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
