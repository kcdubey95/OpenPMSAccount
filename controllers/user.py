from flask import request
from models.user import Open_Account, Relation_Master,Occupation_Master
from extensions import db


def add_user_mobile(mobile_no):
    if request.method == "POST":
        user = Open_Account(mobile_no=mobile_no, step=1)
        user.save()
        data = {
            'id': user.id,
            'mobile_no': user.mobile_no,
        }
        return data


def update_user_stepone(user, fname, lname, email):
    if user:
        user.fname = fname
        user.lname = lname
        user.email = email
        user.step = 2
        db.session.commit()
        return user

def update_user_steptwo(user, fullname, gender, dob, address, income, occupation):
    if user:
        user.fullname = fullname
        user.gender = gender
        user.dob = dob
        user.address = address
        user.income = income
        user.occupation = occupation
        user.step = 3
        db.session.commit()
        return user



def update_user_stepthree(user, nfull_name, dob, address, phone, relation):
    if user:
        user.nfull_name = nfull_name
        user.ndob = dob
        user.naddress = address
        user.nmobile_no = phone
        user.relation = relation
        user.step = 4
        db.session.commit()
        return user



def get_user_data(mobile_no):
    results = Open_Account.get_user_data(mobile_no=mobile_no)

    if isinstance(results, list):
        data = []
        for open_account in results:
            data.append({
                'id': open_account.id,
                'mobile_no': open_account.mobile_no,
                'email': open_account.email,
                'fname': open_account.fname,
                'lname': open_account.lname,
                'fullname': open_account.fullname,
                'gender': open_account.gender,
                'dob': open_account.dob,
                'income': open_account.income,
                'occupation': open_account.occupation,
                'address': open_account.address,
                'nfull_name': open_account.nfull_name,
                'naddress': open_account.naddress,
                'ndob': open_account.ndob,
                'nmobile_no': open_account.nmobile_no,
                'step': open_account.step,
                'relation': open_account.relation,
            })
        return data
    else:
        if results:
            return [{
                'id': results.id,
                'mobile_no': results.mobile_no,
                'email': results.email,
                'fname': results.fname,
                'lname': results.lname,
                'fullname': results.fullname,
                'gender': results.gender,
                'dob': results.dob,
                'income': results.income,
                'occupation': results.occupation,
                'address': results.address,
                'nfull_name': results.nfull_name,
                'naddress': results.naddress,
                'ndob': results.ndob,
                'nmobile_no': results.nmobile_no,
                'step': results.step,
                'relation': results.relation,
            }]
        else:
            return []


def get_all_accont_data(mobile_no):
    results = Open_Account.get_all_accont_data(mobile_no=mobile_no)
    data = []
    for open_account, occupation, relation, income in results:
        data.append({
            'id': open_account.id,
            'mobile_no': open_account.mobile_no,
            'email': open_account.email,
            'fname': open_account.fname,
            'lname': open_account.lname,
            'fullname': open_account.fullname,
            'gender': open_account.gender,
            'dob': open_account.dob,
            'income': open_account.income,
            'occupation': open_account.occupation,
            'address': open_account.address,
            'nfull_name': open_account.nfull_name,
            'naddress': open_account.naddress,
            'ndob': open_account.ndob,
            'nmobile_no': open_account.nmobile_no,
            'step': open_account.step,
            'occupation_name': occupation.occupation_name,
            'relation_name': relation.relation_name,
            'relation': open_account.relation,
            'income_rang': income.income_rang
        })
    return data
