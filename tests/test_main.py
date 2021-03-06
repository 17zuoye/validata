# -*- coding: utf-8 -*-

import os, sys
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)

import unittest


from validata import *
import arrow


class TestMain(unittest.TestCase):

    def test_main(self):

        def current_ek_validation(v1):
            is_valid = True
            if ("id" in v1) and (not isinstance(v1['id'], int)):
                is_valid = False
            if ("name" not in v1) or (not isinstance(v1['name'], basestring)):
                is_valid = False
            return is_valid


        class TeacherAssignHomeworkLogValidator(Validator):
            # v1 is original raw data
            cids            = ListField(IntField(validation=lambda v1: v1 > 0),                  required=True)
            client          = StringField(choices=["web"],                                       required=True)
            create_time     = DateTimeField(validation=lambda v1: arrow.get(v1) < arrow.now(),   required=True)
            current_eid     = ObjectIdField(                                                     required=True)
            current_ek      = DictField(validation=current_ek_validation,                        required=True)
            current_page    = IntField(validation=lambda v1: 0 < v1 < 10000,                     required=True)
            exam_type       = StringField(choices=["homework", "quiz"],                          required=True)
            op_type         = StringField(choices=[
                                            "modify_time",
                                            "ek_click", "eid_page", "eid_add", "eid_del", "confirm_assign",
                                            "check_main",
                                           ],                                                    required=True)
            session         = StringField(validation=lambda v1: True,                            required=True)
            subject         = StringField(choices=["ENGLISH", "MATH"],                           required=True)
            tid             = IntField(validation=lambda v1: v1 > 0,                             required=True)



            example_data = {"cids": [263531], "client": "web", "create_time": "2015-03-01T15:57:37", "current_eid": "51da5a17a3107ec3c2109984", "current_ek": {"id": 1032000082, "name": "[eɪ]ai"}, "current_page": 1, "exam_type": "homework", "op_type": "eid_del", "session": "1491415english1425225216344", "subject": "ENGLISH", "tid": 1491415}
            error_data   = {"cids": [263531], "client": "web", "create_time": "2015-03-01T15:57:37", "current_eid": "__51da5a17a3107ec3c2109984", "current_ek": {"id": 1032000082, "name": None}, "current_page": -3, "exam_type": "homework1", "op_type": "eid_del", "session": "1491415english1425225216344", "subject": "ENGLISH", "_tid": 1491415}



        result1 = TeacherAssignHomeworkLogValidator.do( TeacherAssignHomeworkLogValidator.example_data )
        self.assertTrue(result1.success)
        self.assertEqual(result1.errors, dict())


        result2 = TeacherAssignHomeworkLogValidator.do( TeacherAssignHomeworkLogValidator.error_data   )
        self.assertFalse(result2.success)
        self.assertEqual(result2.json()['errors'], {
                                                    "current_eid": "Invalid Object ID",
                                                    "current_ek": "Value does not match custom validation method",
                                                    "tid": "Field is required",
                                                    "current_page": "Value does not match custom validation method",
                                                    "exam_type": "Value must be one of ['homework', 'quiz']"
                                                  })


if __name__ == '__main__': unittest.main()
