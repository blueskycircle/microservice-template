# Create a test that adds my numbers
from library.methods import add, subtract


def test_add():
    """Test the add function."""
    assert add(2, 3) == 5, "Should be 5"
    assert add(-1, 1) == 0, "Should be 0"
    assert add(0, 0) == 0, "Should be 0"
    assert add(2.5, 3.5) == 6.0, "Should be 6.0"
    assert add(-2.5, -3.5) == -6.0, "Should be -6.0"
    assert add(2, -3) == -1, "Should be -1"


def test_subtract():
    """Test the subtract function."""
    assert subtract(5, 3) == 2, "Should be 2"
    assert subtract(0, 0) == 0, "Should be 0"
    assert subtract(-1, -1) == 0, "Should be 0"
    assert subtract(2.5, 1.5) == 1.0, "Should be 1.0"
    assert subtract(-2.5, -3.5) == 1.0, "Should be 1.0"
    assert subtract(2, -3) == 5, "Should be 5"


def test_add_floating_point_precision():
    """Test that add function handles floating point precision correctly."""
    # This would normally result in precision issues without Decimal
    assert add(-1, 2.3) == 1.3, "Should be exactly 1.3"
    assert add(0.1, 0.2) == 0.3, "Should be exactly 0.3"
    assert add(0.1, 0.7) == 0.8, "Should be exactly 0.8"
    assert add(1.5, -0.5) == 1.0, "Should be exactly 1.0"


def test_subtract_floating_point_precision():
    """Test that subtract function handles floating point precision correctly."""
    # This would normally result in precision issues without Decimal
    assert subtract(1.3, 1) == 0.3, "Should be exactly 0.3"
    assert subtract(0.3, 0.1) == 0.2, "Should be exactly 0.2"
    assert subtract(0.5, 0.4) == 0.1, "Should be exactly 0.1"
    assert subtract(1, 0.7) == 0.3, "Should be exactly 0.3"
