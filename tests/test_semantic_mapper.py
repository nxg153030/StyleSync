import unittest
from src.semantic_mapper.mapper import SemanticMapper

class TestSemanticMapper(unittest.TestCase):

    def setUp(self):
        self.mapper = SemanticMapper()

    def test_translate_technical_to_emotional(self):
        technical_input = "100% cotton, casual fit, short sleeves"
        expected_output = "Soft and breathable cotton for a relaxed summer vibe"
        self.assertEqual(self.mapper.translate(technical_input), expected_output)

    def test_invalid_input(self):
        invalid_input = ""
        with self.assertRaises(ValueError):
            self.mapper.translate(invalid_input)

    def test_edge_case_input(self):
        edge_case_input = "polyester blend, tailored fit"
        expected_output = "Sleek and polished look with a comfortable feel"
        self.assertEqual(self.mapper.translate(edge_case_input), expected_output)

if __name__ == '__main__':
    unittest.main()