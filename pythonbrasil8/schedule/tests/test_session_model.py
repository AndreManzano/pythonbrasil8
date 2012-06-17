# -*- coding: utf-8 -*-
from django.test import TestCase
from django.db.models import ForeignKey, ManyToManyField

from pythonbrasil8.schedule.models import Session, Track
from pythonbrasil8.schedule.forms import SessionForm


class SessionModelTestCase(TestCase):

    def test_should_have_title(self):
        self.assert_field_in("title", Session)

    def test_should_have_description(self):
        self.assert_field_in("description", Session)

    def test_should_have_tags(self):
        self.assert_field_in("tags", Session)

    def test_should_have_speakers(self):
        self.assert_field_in("speakers", Session)

    def test_should_have_type(self):
        self.assert_field_in("type", Session)

    def test_type_should_have_choices(self):
        type_field = Session._meta.get_field_by_name("type")[0]
        choices = [choice[0] for choice in type_field._choices]
        self.assertIn("talk", choices)
        self.assertIn("tutorial", choices)

    def test_speakers_shoudl_be_a_ManyToManyField(self):
        speakers_field = Session._meta.get_field_by_name("speakers")[0]
        self.assertIsInstance(speakers_field, ManyToManyField)

    def test_should_have_a_foreign_key_to_track(self):
        self.assert_field_in("track", Session)
        field = Session._meta.get_field_by_name("track")[0]
        self.assertIsInstance(field, ForeignKey)

    def test_track_fk_should_point_to_Track_model(self):
        field = Session._meta.get_field_by_name("track")[0]
        self.assertEqual(Track, field.related.parent_model)

    def assert_field_in(self, field_name, model):
        self.assertIn(field_name, model._meta.get_all_field_names())


class SessionFormTestCase(TestCase):

    def test_model_should_be_Session(self):
        self.assertEqual(Session, SessionForm._meta.model)
