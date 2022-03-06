#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unit Tests
----------

This module performs unit tests for each helper scripts.
"""

import unittest
import os

from environment_helper import Environment


__author__ = "Lucas Hohmann"
__email__ = "lfhohmann@gmail.com"
__user__ = "@lfhohmann"

__status__ = "Production"
__date__ = "2022/03/06"
__version__ = "1.0"
__license__ = "MIT"


class TestEnvironmentHelper(unittest.TestCase):
    """
    Environment Helper Test
    -----------------------

    Tests the Environment Helper variables class

    Note: Only the current environment mode ("kaggle" or "local") will be
    tested
    """

    # Check current environment mode
    current_mode = "kaggle" if "kaggle" in os.getcwd() else "local"

    def test_mode(self):
        """Test if the current environment mode is "kaggle" or "local"."""

        # Instantiate the environment variables class
        env = Environment()

        # Check if the current environment is "kaggle" or "local"
        self.assertEqual(env.mode, self.current_mode)

    def test_readonly_attributes(self):
        """Test if the readonly attributes ("mode", "dirpath") can't be set"""

        # Instantiate the environment variables class
        env = Environment()

        # Check if the readonly attributes can't be set
        for attribute in ["mode", "dirpath"]:
            with self.assertRaises(AttributeError):
                setattr(env, attribute, "value")

    def test_variables(self):
        """Test if the custom variables are set correctly"""

        data = {
            "kaggle": {
                "train_path": "/kaggle/train.csv",
                "test_path": "/kaggle/test.csv",
            },
            "local": {
                "train_path": "/local/train.csv",
                "test_path": "/local/test.csv",
            },
        }

        # Instantiate the environment variables class with custom data
        env = Environment(data)

        # Check if the custom variables are set correctly
        for attribute in data[env.mode].keys():
            self.assertEqual(data[env.mode][attribute], getattr(env, attribute))


if __name__ == "__main__":
    unittest.main(verbosity=2)
