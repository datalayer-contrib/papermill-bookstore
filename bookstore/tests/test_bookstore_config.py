"""Tests for bookstore config"""
import pytest

from bookstore.bookstore_config import BookstoreSettings, validate_bookstore


def test_validate_bookstore_defaults():
    """Tests that all bookstore validates with default values."""
    expected = {"bookstore_valid": False, "publish_valid": True, "archive_valid": True}
    settings = BookstoreSettings()
    assert validate_bookstore(settings) == expected


def test_validate_bookstore_published():
    """Tests that bookstore does not validate with an empty published_prefix."""
    expected = {"bookstore_valid": False, "publish_valid": False, "archive_valid": True}
    settings = BookstoreSettings(published_prefix="")
    assert validate_bookstore(settings) == expected


def test_validate_bookstore_workspace():
    """Tests that bookstore does not validate with an empty workspace_prefix."""
    expected = {"bookstore_valid": False, "publish_valid": True, "archive_valid": False}
    settings = BookstoreSettings(workspace_prefix="")
    assert validate_bookstore(settings) == expected


def test_validate_bookstore_endpoint():
    """Tests that bookstore does not validate with an empty s3_endpoint_url."""
    expected = {"bookstore_valid": False, "publish_valid": True, "archive_valid": True}
    settings = BookstoreSettings(s3_endpoint_url="")
    assert validate_bookstore(settings) == expected


def test_validate_bookstore_bucket():
    """Tests that bookstore does not validate with an empty s3_bucket."""
    expected = {"bookstore_valid": True, "publish_valid": True, "archive_valid": True}
    settings = BookstoreSettings(s3_bucket="A_bucket")
    assert validate_bookstore(settings) == expected
