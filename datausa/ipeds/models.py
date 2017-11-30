from datausa.database import db
from datausa.ipeds.abstract_models import Enrollment, CipId, UniversityId
from datausa.ipeds.abstract_models import Tuition, GeoId, SectorId, BaseIpeds
from datausa.ipeds.abstract_models import Grads, DegreeId, GradsPct, Admissions
from datausa.ipeds.abstract_models import EnrollmentEfa, LStudyId, EnrollmentStatusId
from datausa.attrs.consts import STATE, COUNTY, MSA, GEO
from datausa.attrs.consts import PLACE, ALL


class EnrollmentYcu(Enrollment, CipId, UniversityId):
    __tablename__ = "enrollment_ycu"
    median_moe = 2.1

    year = db.Column(db.Integer(), primary_key=True)
    grads_total = db.Column(db.Integer())

    @classmethod
    def get_supported_levels(cls):
        return {"cip": CipId.LEVELS, "university": [ALL]}


class TuitionYgs(Tuition, GeoId, SectorId):
    __tablename__ = "tuition_ygs"
    median_moe = 2

    year = db.Column(db.Integer(), primary_key=True)

    @classmethod
    def get_supported_levels(cls):
        return {"geo": GeoId.LEVELS, "sector": [ALL]}


class TuitionYc(Tuition, CipId):
    __tablename__ = "tuition_yc"
    median_moe = 1

    year = db.Column(db.Integer(), primary_key=True)
    oos_tuition_rank = db.Column(db.Integer())
    state_tuition_rank = db.Column(db.Integer())


class TuitionYu(Tuition, UniversityId):
    __tablename__ = "tuition_yu"
    median_moe = 1

    year = db.Column(db.Integer(), primary_key=True)

    @classmethod
    def get_supported_levels(cls):
        return {"university": [ALL]}


class TuitionYcu(Tuition, CipId, UniversityId):
    __tablename__ = "tuition_ycu"
    median_moe = 2

    year = db.Column(db.Integer(), primary_key=True)
    grads_total = db.Column(db.Integer())

    @classmethod
    def get_supported_levels(cls):
        return {"cip": CipId.LEVELS, "university": [ALL]}


class TuitionYcs(Tuition, CipId, SectorId):
    __tablename__ = "tuition_ycs"
    median_moe = 1

    year = db.Column(db.Integer(), primary_key=True)
    num_universities = db.Column(db.Integer())

    @classmethod
    def get_supported_levels(cls):
        return {"cip": CipId.LEVELS, "sector": [ALL]}


class GradsYc(Grads, CipId):
    __tablename__ = "grads_yc"
    median_moe = 0

    year = db.Column(db.Integer(), primary_key=True)
    grads_rank = db.Column(db.Integer)

    @classmethod
    def get_supported_levels(cls):
        return {"cip": CipId.LEVELS}


class GradsYcd(Grads, CipId, DegreeId):
    __tablename__ = "grads_ycd"
    median_moe = 2

    year = db.Column(db.Integer(), primary_key=True)

    @classmethod
    def get_supported_levels(cls):
        return {"cip": CipId.LEVELS, "degree": [ALL]}


class GradsYu(Grads, UniversityId):
    __tablename__ = "grads_yu"
    median_moe = 1

    year = db.Column(db.Integer(), primary_key=True)

    @classmethod
    def get_supported_levels(cls):
        return {"university": [ALL]}


class GradsYcu(Grads, CipId, UniversityId):
    __tablename__ = "grads_ycu"
    median_moe = 2

    year = db.Column(db.Integer(), primary_key=True)

    # parent = relationship('Geo', foreign_keys='GeoContainment.parent_geoid')

    @classmethod
    def get_supported_levels(cls):
        return {"cip": CipId.LEVELS, "university": [ALL],
                GEO: [STATE, COUNTY, MSA, PLACE, ALL]}


class GradsYg(Grads, GeoId):
    __tablename__ = "grads_yg"
    median_moe = 1

    year = db.Column(db.Integer, primary_key=True)
    grads_total_growth = db.Column(db.Float)

    @classmethod
    def get_supported_levels(cls):
        return {GEO: GeoId.LEVELS}


class GradsYgc(Grads, GeoId, CipId):
    __tablename__ = "grads_ygc"
    median_moe = 2

    year = db.Column(db.Integer(), primary_key=True)
    grads_total_growth = db.Column(db.Float)
    grads_total_rca = db.Column(db.Float)

    @classmethod
    def get_supported_levels(cls):
        return {"cip": CipId.LEVELS, GEO: GeoId.LEVELS}


class GradsYgu(Grads, GeoId, UniversityId):
    __tablename__ = "grads_ygu"
    median_moe = 2

    year = db.Column(db.Integer(), primary_key=True)
    grads_total_growth = db.Column(db.Float)

    @classmethod
    def get_supported_levels(cls):
        return {"university": [ALL], GEO: GeoId.LEVELS}


class GradsYgs(Grads, GeoId, SectorId):
    __tablename__ = "grads_ygs"
    median_moe = 2

    year = db.Column(db.Integer(), primary_key=True)
    grads_total_growth = db.Column(db.Float)

    @classmethod
    def get_supported_levels(cls):
        return {"sector": [ALL], GEO: GeoId.LEVELS}


class GradsYud(Grads, UniversityId, DegreeId):
    __tablename__ = "grads_yud"
    median_moe = 2

    year = db.Column(db.Integer(), primary_key=True)
    grads_total = db.Column(db.Integer())

    @classmethod
    def get_supported_levels(cls):
        return {"university": [ALL], "degree": [ALL]}


class GradsYucd(Grads, UniversityId, CipId, DegreeId):
    __tablename__ = "grads_yucd"
    median_moe = 3

    year = db.Column(db.Integer(), primary_key=True)
    grads_total = db.Column(db.Integer())

    @classmethod
    def get_supported_levels(cls):
        return {"university": [ALL], "degree": [ALL], "cip": CipId.LEVELS}


class GradsYgd(Grads, GeoId, DegreeId):
    __tablename__ = "grads_ygd"
    median_moe = 2

    year = db.Column(db.Integer(), primary_key=True)
    grads_total_growth = db.Column(db.Float)
    grads_total_rca = db.Column(db.Float)

    @classmethod
    def get_supported_levels(cls):
        return {GEO: GeoId.LEVELS, "degree": [ALL]}


class GradsYgcd(Grads, GeoId, CipId, DegreeId):
    __tablename__ = "grads_ygcd"
    median_moe = 3

    year = db.Column(db.Integer(), primary_key=True)
    grads_total_growth = db.Column(db.Float)
    grads_total_rca = db.Column(db.Float)

    @classmethod
    def get_supported_levels(cls):
        return {"cip": CipId.LEVELS, GEO: GeoId.LEVELS, "degree": [ALL]}


class GradsPctYcu(GradsPct, CipId, UniversityId):
    __tablename__ = "gradspct_ycu"
    median_moe = 2

    year = db.Column(db.Integer(), primary_key=True)
    grads_total = db.Column(db.Integer)

    @classmethod
    def get_supported_levels(cls):
        return {"cip": CipId.LEVELS, "university": [ALL]}


class UnivGeo(BaseIpeds, UniversityId, GeoId):
    __tablename__ = "university_geo"
    median_moe = 0

    @classmethod
    def get_supported_levels(cls):
        return {"university": [ALL],
                GEO: [STATE, COUNTY, MSA, PLACE, ALL]}


class AdmissionsYu(Admissions, UniversityId):
    __tablename__ = "adm_undergrad_yu"
    median_moe = 1

    year = db.Column(db.Integer(), primary_key=True)

    @classmethod
    def get_supported_levels(cls):
        return {"university": UniversityId.LEVELS}


class AdmissionsY(Admissions):
    __tablename__ = "adm_undergrad_y"
    year = db.Column(db.Integer(), primary_key=True)
    median_moe = 0

    @classmethod
    def get_supported_levels(cls):
        return {"year": [ALL]}


class EnrollmentEfaYule(EnrollmentEfa, UniversityId, LStudyId, EnrollmentStatusId):
    __tablename__ = "enrollment_efa_yule"
    year = db.Column(db.Integer(), primary_key=True)
    median_moe = 3

    @classmethod
    def get_supported_levels(cls):
        return {"year": [ALL], "university": UniversityId.LEVELS, "enrollment_status": [ALL], "lstudy": [ALL]}


class EnrollmentEfaYul(EnrollmentEfa, UniversityId, LStudyId):
    __tablename__ = "enrollment_efa_yul"
    year = db.Column(db.Integer(), primary_key=True)
    median_moe = 2

    @classmethod
    def get_supported_levels(cls):
        return {"year": [ALL], "university": UniversityId.LEVELS, "lstudy": [ALL]}


class EnrollmentEfaYue(EnrollmentEfa, UniversityId, EnrollmentStatusId):
    __tablename__ = "enrollment_efa_yue"
    year = db.Column(db.Integer(), primary_key=True)
    median_moe = 2

    @classmethod
    def get_supported_levels(cls):
        return {"year": [ALL], "university": UniversityId.LEVELS, "enrollment_status": [ALL]}


class EnrollmentEfaYu(EnrollmentEfa, UniversityId):
    __tablename__ = "enrollment_efa_yu"
    year = db.Column(db.Integer(), primary_key=True)
    median_moe = 1

    @classmethod
    def get_supported_levels(cls):
        return {"year": [ALL], "university": UniversityId.LEVELS}
