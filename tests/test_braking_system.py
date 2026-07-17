import pytest
from controller.braking_system import aeb


@pytest.mark.parametrize(
    "speed, distance, expected",
     [
         (50, 8, True),
         (50, 20, False),
         (15, 8, False),
         (30, 10, False),
         (30, 9.9, True),
     ]
 )
def test_brake_decision_for_valid_scenarios(speed, distance, expected):
    assert aeb(speed,distance) == expected


@pytest.mark.parametrize(
    "speed, distance, expected",
    [
        (21, 10.0, False),   # exactly at distance threshold
        (21, 9.99, True),    # just below threshold
        (21, 10.01, False),  # just above threshold
        (20, 9.99, False),   # exactly at speed threshold
        (20.01, 9.99, True), # just above speed threshold
        (19.99, 9.99, False) # just below speed threshold
    ]
)
def test_brake_decision_at_threshold_boundaries(speed, distance, expected):
    assert aeb(speed, distance) == expected


@pytest.mark.parametrize(
    "speed, distance, expected",
    [
        (-21.0, 10.0, False),   # exactly at distance threshold
        (None, -9.99, True),    # just below threshold
        (21, 10.01, False),  # just above threshold
        (0, -9.99, False),   # exactly at speed threshold
        ("2", 9.99, True), # just above speed threshold
        (19.99, None, False) # just below speed threshold
    ]
)
def test_brake_decision_at_invalid_inputs(speed, distance, expected):
    with pytest.raises((ValueError, TypeError)):
        assert aeb(speed, distance) == expected
