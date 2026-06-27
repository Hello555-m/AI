from datetime import datetime, timedelta


class OfficeAssistant:
    def __init__(self, company_name: str):
        self.company_name = company_name

    def handle_request(self, request: str) -> str:
        request_lower = request.lower()

        if "email" in request_lower or "e-mail" in request_lower:
            return self._draft_email(request)

        if "termin" in request_lower or "termine" in request_lower or "uhr" in request_lower:
            return self._schedule_meeting(request)

        if "aufgabe" in request_lower or "task" in request_lower:
            return self._create_task(request)

        return (
            f"Ich bin Ihr digitaler Büroassistent für {self.company_name}. "
            f"Ich kann E-Mails formulieren, Termine planen und Aufgaben organisieren."
        )

    def _draft_email(self, request: str) -> str:
        return (
            "Betreff: Rückmeldung zur Lieferverzögerung\n\n"
            "Hallo,\n\n"
            f"Vielen Dank für Ihre Geduld. Wir haben Ihre Anfrage erhalten und arbeiten an einer schnellen Lösung.\n\n"
            f"Mit freundlichen Grüßen\n"
            f"{self.company_name}"
        )

    def _schedule_meeting(self, request: str) -> str:
        meeting_time = "14:00"
        if "morgen" in request.lower():
            meeting_day = (datetime.now() + timedelta(days=1)).strftime("%d.%m.%Y")
        else:
            meeting_day = datetime.now().strftime("%d.%m.%Y")

        return f"Termin geplant: {meeting_day} um {meeting_time}.\nBitte bestätigen Sie den Termin im Kalender."

    def _create_task(self, request: str) -> str:
        return (
            "Aufgabe erstellt: Rechnungsprüfung\n"
            "Priorität: Mittel\n"
            "Status: Offen"
        )
