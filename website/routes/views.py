from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from jinja2 import Environment, FileSystemLoader
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
        # add questions to questioner
        questioner = Questioner(title=questioner_form.title.data, content=questioner_form.content.data)
        for q in questions:
            questioner.question.append(q)
            questioner.remove(q)
        questioners.append(questioner)
        db.session.add(questioner)
    elif research_form.validate_on_submit():
        # TODO: get participants as well
        r = Research(title=research_form.title.data, content=research_form.content.data)
        # add questioners to research
        for q in questioners:
            r.questioner.append(q)
            questioners.remove(q)
        if research_form.publish.validate(research_form):
            if str(current_user.permission) != 'חוקר':
                r.waiting_to_approval = True
            elif current_user.permission_confirmation and str(current_user.permission) == 'חוקר':
                r.approved = True
        db.session.add(r)
        # add user as participant in research
        p = Participants(research_id=r.id, participant_id=current_user.id)
        db.session.add(p)
        # add user as research creator
        role = Role.query.filter_by(role='מחבר').first()
        role.participant.append(p)
        db.session.add(role)
        db.session.commit()
    return render_template("template_builder.html", questioner_form=questioner_form, question_form=question_form, answer_form=answer_form)

@views.route('/builder2')
def builder2():
    return render_template("template_builder2.html")


@views.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template("contact_us.html")


@views.route('/about')
def about():
    return render_template("about.html")


@views.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    # TODO: set dashboard functions: approval from admin & researcher
    # if user has no permission_confirmation -> it`s regular user
    table_name = 'מחקרים'
    table = Participants.query.filter_by(participant_id=current_user.id).all()
    # TODO: add table_headers for each table view
    table_headers = []
    # else change data-view by permissions
    if current_user.permission_confirmation and not str(current_user.permission) == "נחקר":
        if str(current_user.permission) == "מנהל":
            table_name = 'משתמשים לאישור הרשאות'
            table_headers = ['שם', 'שם משפחה', 'אימייל', 'תאריך הרשמה', 'הרשאות']
            table = User.query.filter_by(permission_confirmation=False).all()
        elif str(current_user.permission) == 'עוזר מחקר':
            table = Participants.query.filter_by(participant_id=current_user.id).all()
        elif str(current_user.permission) == 'חוקר':
            table_name = 'מחקרים לאישור פרסום'
            table = Participants.query.filter_by(participant_id=current_user.id, waiting_to_approval=True).all()
        else:
            flash('הרשאות לא הוגדרו', 'error')

    env = Environment(loader=FileSystemLoader('/path/to/templates'))

    # TODO: put this functions to other file
    def query_db(tag, query, table_name):
        #TODO: delete user properly
        return 'todo'

    def delete_user(email):
        #TODO: delete user properly
        return 'todo'

    def validate_user(email):
        u = User.query.filter_by(email=email).first()
        u.permission_confirmation = True
        db.session.commit
        return 'todo: check'

    def change_permissions(email, permission):
        u = User.query.filter_by(email=email).first()
        u.permission = permission
        if str(current_user.permission) == "מנהל" or permission == "נחקר":
            u.permission_confirmation = True
        db.session.commit
        return 'todo'

    def validate_research(id):
        # TODO: if Participants.query.filter_by():
        r = Research.query.filter_by(id=id).first()
        r.approved = True
        r.waiting_to_approval = False
        db.session.commit
        return 'todo'

    def delete_research(id):
        return 'todo'

    def delete_participant(email, id):
        u = User.query.filter_by(email=email).first()
        p = Participants.delete().where(Participants.c.participant_id == u.id, Participants.c.research_id == id)
        p.execute()
        return 'todo: check'

    def add_participant(email, id):
        u = User.query.filter_by(email=email).first()
        p = Participants(research_id=id, participant_id=u.id)
        db.session.add(p)
        db.session.commit
        return 'todo: check'

    # TODO put to init file
    env.globals['delete_participant'] = delete_participant
    env.globals['add_participant'] = add_participant
    env.globals['change_permissions'] = change_permissions
    env.globals['validate_research'] = validate_research
    env.globals['validate_user'] = validate_user
    env.globals['delete_user'] = delete_user
    env.globals['delete_research'] = delete_research

    return render_template("dashboard.html", table_headers=table_headers, table=table, table_name=table_name)


@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    # TODO: add delete option
    if current_user.is_authenticated:
        form = UpdateAccountForm()
        if form.validate_on_submit():
            current_user.first_name = form.firstname.data
            current_user.second_name = form.name.data
            current_user.email = form.email.data
            current_user.birth_date = form.birthdate.data
            g = db.session.query(Gender).filter_by(gender=form.gender.data).first()
            g.users.append(current_user)
            if current_user.permission != form.permissions.data:
                if form.permissions.data == "נחקר":
                    current_user.permission_confirmation = True
                else:
                    current_user.permission_confirmation = False
                p = Permissions.query.filter_by(permission=form.permissions.data).first()
                p.users.append(current_user)
            db.session.commit()
            flash('שינויים נשמרו בהצלחה', 'success')
        elif request.method == 'GET':
            form.firstname.data = current_user.first_name
            form.name.data = current_user.second_name
            form.email.data = current_user.email
            form.birthdate.data = current_user.birth_date
            form.gender.data = current_user.gender
            form.permissions.data = current_user.permission
        return render_template("profile.html", user=current_user, form=form)
    else:
        flash('משתמש לא מחובר', 'error')
        return redirect(url_for('auth.login'))


@views.route('/research', methods=['GET', 'POST'])
@login_required
def research():
    form = ResearchForm()
    if form.validate_on_submit():
        r = Research(title=form.title.data, content=form.content.data)
        if form.publish.validate(form):
            if str(current_user.permission) != 'חוקר':
                r.waiting_to_approval = True
            elif current_user.permission_confirmation and str(current_user.permission) == 'חוקר':
                r.approved = True
        db.session.add(r)
        db.session.commit()
        role = Role.query.filter_by(role='מחבר').first()
        p = Participants(research_id=r.id, participant_id=current_user.id, role_id=role.id)
        db.session.add(p)
        db.session.commit()
        role.participant.append(p)
        db.session.add(role)
        db.session.commit()
        if form.new_questioner.validate(form):
            return redirect(url_for("views.builder"))
    return render_template("new_research.html", form=form)
