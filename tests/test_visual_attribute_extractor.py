import unittest
from src.visual_attribute_extractor.extractor import VisualAttributeExtractor

class TestVisualAttributeExtractor(unittest.TestCase):

    def setUp(self):
        self.extractor = VisualAttributeExtractor()

    def test_extract_attributes(self):
        image_path = 'data/samples/sample_image.jpg'
        attributes = self.extractor.extract(image_path)
        self.assertIsInstance(attributes, list)
        self.assertGreater(len(attributes), 0)

    def test_invalid_image(self):
        image_path = 'data/samples/invalid_image.txt'
        with self.assertRaises(ValueError):
            self.extractor.extract(image_path)

    def test_attribute_format(self):
        image_path = 'data/samples/sample_image.jpg'
        attributes = self.extractor.extract(image_path)
        for attribute in attributes:
            self.assertIsInstance(attribute, str)

if __name__ == '__main__':
    unittest.main()