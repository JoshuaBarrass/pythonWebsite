from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import  login_required, current_user
from .models import Note, CheckItem
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])   #run at www.page.com/
@login_required

def home():

    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Error - Note to short', category='error')
        else:
            new_note = Note(data=note, userId=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note created!', category='success')
            return redirect(url_for('views.home'))



    return render_template("home.html", user=current_user)

@views.route('/CheckList', methods = ['GET', 'POST'])
@login_required

def checkListHome():

    if request.method == 'POST':
        checkText = request.form.get('item')

        if len(checkText) < 1:
            flash('Error - Note to short', category='error')
        else:
            new_check = CheckItem(data=checkText, userId=current_user.id)
            db.session.add(new_check)
            db.session.commit()
            flash('Checklist Item created!', category='success')
            return redirect(url_for('views.checkListHome'))

    activities = len(current_user.checklistItems)
    done = 0
    percentDone = 0
    if activities > 0:
        for item in current_user.checklistItems:
            if item.done:
                done += 1
        
        percentDone = round((done/activities) * 100)
        
    return render_template("checkList.html", user=current_user, perdone=percentDone, todo=(int(activities-done)))

@views.route('/delete-check', methods=['POST'])
def delete_check():
    item = json.loads(request.data)
    itemId = item['checkId']
    item = CheckItem.query.get(itemId)
    if item:
        if item.userId == current_user.id:
            db.session.delete(item)
            db.session.commit()

    return jsonify({})

@views.route('/change-item-state', methods=['POST'])
def change_item_state():
    item = json.loads(request.data)
    itemId = item['checkId']
    item = CheckItem.query.get(itemId)
    if item:
        if item.userId == current_user.id:
            temp_item = CheckItem(data=item.data, userId=item.userId, date=item.date, done= not item.done)
            db.session.delete(item)
            db.session.add(temp_item)
            db.session.commit()

    return jsonify({})

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.userId == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


