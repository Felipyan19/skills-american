from __future__ import annotations

import unittest

from server.bootstrap import extract_between_markers


class BootstrapTests(unittest.TestCase):
    def test_extract_between_markers_returns_block(self) -> None:
        source = "before\n<!-- START -->\nhello\n<!-- END -->\nafter"
        extracted = extract_between_markers(source, "<!-- START -->", "<!-- END -->")
        self.assertEqual(extracted, "<!-- START -->\nhello\n<!-- END -->\n")

    def test_extract_between_markers_raises_for_missing_markers(self) -> None:
        with self.assertRaises(ValueError):
            extract_between_markers("hello", "START", "END")
