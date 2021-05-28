import os
import pickle
from unittest import TestCase


class TestSave_training_object(TestCase):
    def test_save_first(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        if os.path.isfile("data/db.pickle"):
            os.remove("data/db.pickle")
        # create demo object
        from main import save_training_object
        save_training_object("Name", "referent", "duration", "content")
        with open("data/db.pickle", "rb") as pickleFile:
            list_of_trainings = pickle.load(pickleFile)
        assert len(list_of_trainings) == 1

    def test_2_saves(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        if os.path.isfile("data/db.pickle"):
            os.remove("data/db.pickle")
        # create demo object
        from main import save_training_object
        save_training_object("Name", "referent", "duration", "content")
        save_training_object("Name2", "referent2", "duration2", "content2")
        with open("data/db.pickle", "rb") as pickleFile:
            list_of_trainings = pickle.load(pickleFile)
        assert len(list_of_trainings) == 2
