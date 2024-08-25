from extensions import db



class Open_Account(db.Model):
    __tablename__ = 'pms_request_account'

    id = db.Column(db.Integer, primary_key=True)
    mobile_no = db.Column(db.String(10), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=True, unique=True)
    fname = db.Column(db.String(80), nullable=True, unique=False)
    lname = db.Column(db.String(80), nullable=True, unique=False)
    fullname = db.Column(db.String(100), nullable=True, unique=False)
    gender = db.Column(db.String(80), nullable=True, unique=False)
    dob = db.Column(db.String(80), nullable=True, unique=False)
    income = db.Column(db.String(80), db.ForeignKey('income_master.id'), nullable=True, unique=False)
    occupation = db.Column(db.Integer, db.ForeignKey('occupation_Master.id'), nullable=True, unique=False)
    address = db.Column(db.String(200), nullable=True, unique=False)
    nfull_name = db.Column(db.String(80), nullable=True, unique=False)
    naddress = db.Column(db.String(200), nullable=True, unique=False)
    ndob = db.Column(db.String(80), nullable=True, unique=False)
    nmobile_no = db.Column(db.String(10), nullable=True, unique=False)
    relation = db.Column(db.Integer, db.ForeignKey('relation_Master.id'), nullable=True, unique=False)
    step = db.Column(db.Integer, nullable=False, unique=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())
    usersoc = db.relationship('Occupation_Master', backref='pms_request_account')
    usersrs = db.relationship('Relation_Master', backref='pms_request_account')
    usersim = db.relationship('Income_Master', backref='pms_request_account')

    @property
    def data(self):
        return {
            'id': self.id,
            'mobile_no': self.mobile_no,
            'email': self.email,
            'fname': self.fname,
            'lname': self.lname,
            'fullname': self.fullname,
            'gender': self.gender,
            'dob': self.dob,
            'income': self.income,
            'occupation': self.occupation,
            'address': self.address,
            'nfull_name': self.nfull_name,
            'naddress': self.naddress,
            'ndob': self.ndob,
            'nmobile_no': self.nmobile_no,
            'relation': self.relation,
            'step': self.step

        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        r = cls.query.all()
        result = []
        for i in r:
            result.append(i.data)
        return result

    @classmethod
    def get_user_data(cls, mobile_no):
        return cls.query.filter(cls.mobile_no == mobile_no).all()

    @classmethod
    def get_all_accont_data(cls, mobile_no):
        results = db.session.query(cls, Occupation_Master, Relation_Master, Income_Master).join(Occupation_Master,cls.occupation == Occupation_Master.id).join(Relation_Master, cls.relation == Relation_Master.id).join(Income_Master, cls.income == Income_Master.id).filter(cls.mobile_no == mobile_no).distinct().all()
        return results



    @classmethod
    def filter_by_condition(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()


# class Gender_Master(db.Model):
#     __tablename__ = 'gender_master'
#
#     id = db.Column(db.Integer, primary_key=True)
#     gender_name = db.Column(db.String(100), nullable=False, unique=True)
#
#     @property
#     def data(self):
#         return {
#             'id': self.id,
#             'gender_name': self.gender_name,
#         }
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#     @classmethod
#     def get_all(cls):
#         r = cls.query.all()
#         result = []
#         for i in r:
#             result.append(i.data)
#         return result
#
#     @classmethod
#     def filter_by_condition(cls, **kwargs):
#         return cls.query.filter_by(**kwargs).all()


class Occupation_Master(db.Model):
    __tablename__ = 'occupation_Master'

    id = db.Column(db.Integer, primary_key=True)
    occupation_name = db.Column(db.String(100), nullable=False, unique=True)

    @property
    def data(self):
        return {
            'id': self.id,
            'occupation_name': self.occupation_name,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        r = cls.query.all()
        result = []
        for i in r:
            result.append(i.data)
        return result

    @classmethod
    def filter_by_condition(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()


class Relation_Master(db.Model):
    __tablename__ = 'relation_Master'

    id = db.Column(db.Integer, primary_key=True)
    relation_name = db.Column(db.String(100), nullable=False, unique=True)

    @property
    def data(self):
        return {
            'id': self.id,
            'relation_name': self.relation_name,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        r = cls.query.all()
        result = []
        for i in r:
            result.append(i.data)
        return result

    @classmethod
    def filter_by_condition(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()


class Income_Master(db.Model):
    __tablename__ = 'income_master'

    id = db.Column(db.Integer, primary_key=True)
    income_rang = db.Column(db.String(100), nullable=False, unique=True)

    @property
    def data(self):
        return {
            'id': self.id,
            'income_rang': self.occupation_name,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        r = cls.query.all()
        result = []
        for i in r:
            result.append(i.data)
        return result

    @classmethod
    def filter_by_condition(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()