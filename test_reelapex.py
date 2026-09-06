# test_reelapex.py
"""
Tests for ReelApex module.
"""

import unittest
from reelapex import ReelApex

class TestReelApex(unittest.TestCase):
    """Test cases for ReelApex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ReelApex()
        self.assertIsInstance(instance, ReelApex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ReelApex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
