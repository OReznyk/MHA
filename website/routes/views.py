from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from website.forms import UpdateAccountForm, QuestionForm, AnswerForm, ResearchForm, BasicForm
from website.models.gender import Gender
from website.models.role import Role
from website.models.permissions import Permissions
from website.models.research_participants import Participants
from website.models.question import Question
from website.models.questioner import Questioner
from website.models.answer import Answer
from website.models.research import Research
from website.models.user import User
from ..extensions import db

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('index.html')


@views.route('/builder')
def builder():
    research_form = ResearchForm()
    questioner_form = BasicForm()
    question_form = QuestionForm()
    answer_form = AnswerForm()
    questioners = []
    questions = []
    answers = []
    if question_form.validate_on_submit():
        q = Question(question=question_form.question.data, weight=question_form.weight.data, type=question_form.type.data, place=question_form.place.data, author_id=current_user.id)
        questions.append(q)
        db.session.add(q)
        # add question.id to all answers where no question.id
        # every question submit must be after answers for this question submitted
        for answer in answers:
            if answer.question_id == '':
                q.optional_answers.append(answer)
                db.session.add(answer)
                answers.remove(answer)
    elif answer_form.validate_on_submit():
        a = Answer(answer=answer_form.answer.data, type=answer_form.type.data, weight=answer_form.weight.data)
        answers.append(a)
    elif research_form.validate_on_submit():
        questioner = Questioner(title=questioner_form.title.data, content=questioner_form.content.data)
        for q in questions:
            questioner.question.append(q)
            questioner.remove(q)
        questioners.append(questioner)
        db.session.add(questioner)
    elif research_form.validate_on_submit():
        #TODO: get participants as well
        #TODO: check if save or publish
        r = Research(title=research_form.title.data, content=research_form.content.data)
        for q in questioners:
            r.questioner.append(q)
            questioners.remove(q)
        if research_form.publish.validate(research_form):
            if str(current_user.permission) != 'חוקר':
                r.waiting_to_approval = True
            else:
                r.approved = True
        db.session.add(r)

        p = Participants(research_id=r.id, participant_id=current_user.id)
        db.session.add(p)
        role = Role.query.filter_by(role='מחבר').first()
        role.participant.append(p)
        db.session.add(role)
        db.session.commit()
    return render_template("template_builder.html", questioner_form=questioner_form, question_form=question_form, answer_form=answer_form)


@views.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template("contact_us.html")


@views.route('/about')
def about():
    return render_template("about.html")


@views.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    # if user has no permission_confirmation -> it`s regular user
    table_name = 'מחקרים'
    table = Participants.query.filter_by(participant_id=current_user.id).all()
    # else
    if current_user.permission_confirmation and not str(current_user.permission) == "נחקר":
        if str(current_user.permission) == "מנהל":
            table_name = 'משתמשים לאישור הרשאות'
            table = User.query.filter_by(permission_confirmation=False).all()
        elif str(current_user.permission) == 'חוקר' or str(current_user.permission) == 'עוזר מחקר':
            return render_template("dashboard.html", table_name=table_name, table=Participants.query.filter_by(participant_id=current_user.id).all())
        else:
            flash('הרשאות לא הוגדרו', 'error')

    return render_template("dashboard.html", table=table, table_name=table_name)


@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if current_user.is_authenticated:
        form = UpdateAccountForm()
        if form.validate_on_submit():
            current_user.first_name = form.firstname.data
            current_user.second_name = form.name.data
            current_user.email = form.email.data
            current_user.birth_date = form.birthdate.data
            user = current_user
            g = db.session.query(Gender).filter_by(gender=form.gender.data).first()
            g.users.append(user)
            if current_user.permission != form.permissions.data:
                if form.permissions.data == "נחקר":
                    current_user.permission_confirmation = True
                else:
                    current_user.permission_confirmation = False
                p = Permissions.query.filter_by(permission=form.permissions.data).first()
                p.users.append(user)
            db.session.commit()
            flash('שינויים נשמרו בהצלחה', 'success')
        elif request.method == 'GET':
            form.firstname.data = current_user.first_name
            form.name.data = current_user.second_name
            form.email.data = current_user.email
            form.birthdate.data = current_user.birth_date
            form.gender.data = current_user.gender
            form.permissions.data = current_user.permission
        return render_template("profile.html", user=user, form=form)
    else:
        flash('משתמש לא מחובר', 'error')
        return redirect(url_for('auth.login'))

'''
def delete_user():
    if "user" in session:
        User.query.filter_by(id=session["user"].id).delete()
        flash ('משתמש נמחק בהצלחה', 'success')
        return redirect(url_for("view/home"))
'''
