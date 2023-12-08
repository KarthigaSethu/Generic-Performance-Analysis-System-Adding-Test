import unittest
from entity import Entity
from entity import EntityCollection

class TestEntity(unittest.TestCase):

    def setUp(self):
        # Code to set up resources or initialize variables for each test in this class
        self.entity = Entity("1", {"field1": 10})

    def tearDown(self):
        # Code to clean up resources after each test in this class, ensuring a clean state for each test.
        del self.entity

    def test_entity_creation(self):
        # Test to check whether the attributes a new Entity instance match the expected values
        self.assertEqual(self.entity.entity_id, "1")
        self.assertEqual(self.entity.field_value_pairs, {"field1": 10})

    def test_add_field(self):
        # Test to add key-value pairs to the attributes from an entity
        self.entity.add("field1", 20)
        self.assertEqual(self.entity.field_value_pairs, {"field1": 20})

    def test_add_non_numeric_field(self):
        # Test to skip adding non-numeric values in a field
        self.entity.add("field1", "abc")
        # After adding a non-numeric value, field_value_pairs should remain unchanged
        self.assertEqual(self.entity.field_value_pairs, {"field1": 10})
        
class TestEntityCollection(unittest.TestCase):

    def setUp(self):
        # Code to set up resources or initialize variables for each test in this class
        self.collection = EntityCollection()

    def tearDown(self):
        # Code to clean up resources after each test in this class
        del self.collection

    def test_add_entity(self):
        # Test to check that an entity is added to the collection and the returned entity refer to the same underlying object.
        entity = self.collection.add_entity("1")
        self.assertEqual(len(self.collection.items), 1)
        self.assertIs(self.collection.items[0], entity)

    def test_compute_mean(self):
        # Test to check the average from a computable field within a collection
        self.collection.add("1", {"score": 10})
        self.collection.add("2", {"score": 20})
        self.assertEqual(self.collection.compute_mean("score"), 15.0)

    def test_compute_mode(self):
        # Test to check the mode from a computable field within a collection
        self.collection.add("1", {"score": 10})
        self.collection.add("2", {"score": 20})
        self.assertEqual(self.collection.compute_mode("score"), 10)

    def test_compute_median(self):
        # Test to check median from a computable field within a collection
        self.collection.add("1", {"score": 10})
        self.collection.add("2", {"score": 20})
        self.assertEqual(self.collection.compute_median("score"), 15.0)

    def test_compute_min(self):
        # Test to check minimum from a computable field within a collection
        self.collection.add("1", {"score": 10})
        self.collection.add("2", {"score": 20})
        self.assertEqual(self.collection.compute_min("score"), 10)

    def test_compute_max(self):
        # Test to check the maximum from a computable field within a collection
        self.collection.add("1", {"score": 10})
        self.collection.add("2", {"score": 20})
        self.assertEqual(self.collection.compute_max("score"), 20)

    def test_compute_count(self):
        # Test to check the number of entities within a collection
        self.collection.add("1", {"score": 10})
        self.collection.add("2", {"score": 20})
        self.assertEqual(self.collection.compute_count("score"), 2)

unittest.main(argv=[''], verbosity=2, exit=False)