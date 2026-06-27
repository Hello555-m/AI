import unittest

from office_assistant import OfficeAssistant


class OfficeAssistantTests(unittest.TestCase):
    def setUp(self):
        self.assistant = OfficeAssistant("BluePeak Consulting")

    def test_email_draft_generation(self):
        response = self.assistant.handle_request(
            "Schreibe eine E-Mail an einen Kunden über die verspätete Lieferung"
        )
        self.assertIn("Betreff", response)
        self.assertIn("Hallo", response)

    def test_meeting_scheduling(self):
        response = self.assistant.handle_request(
            "Plane einen Termin für morgen um 14 Uhr"
        )
        self.assertIn("Termin geplant", response)
        self.assertIn("14:00", response)

    def test_task_creation(self):
        response = self.assistant.handle_request(
            "Erstelle eine Aufgabe für die Rechnungsprüfung"
        )
        self.assertIn("Aufgabe", response)
        self.assertIn("Rechnungsprüfung", response)


if __name__ == "__main__":
    unittest.main()
