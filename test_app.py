import pytest

from app import calculate_transaction_risk


def test_calculate_transaction_risk():
    """Normal akis testi."""
    data = [{"user_id": 1, "amount": 100}]
    result = calculate_transaction_risk(data)
    assert result == 5.0  # nosec


def test_empty_transactions():
    """Bos liste testi."""
    assert calculate_transaction_risk([]) == 0.0  # nosec


def test_max_risk_limit():
    """Sinir deger testi (Risk 500'u gecmemeli)."""
    data = [{"user_id": 2, "amount": 100000}]
    result = calculate_transaction_risk(data)
    assert result == 500.0  # nosec
    