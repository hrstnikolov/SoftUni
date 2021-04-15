from unittest import TestCase


def my_sum(*args):
    return sum(args)


class SampleTests(TestCase):
    def test_my_sum__when_numbers__expect_to_be_equal(self):
        numbers = [1, 2, 3, 4]
        expected_result = sum(numbers)
        actual_result = my_sum(numbers)

        self.assertEqual(expected_result, actual_result)