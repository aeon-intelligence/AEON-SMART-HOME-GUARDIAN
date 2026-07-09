import json
from pathlib import Path


class ThaiContextEngine:
    """
    ระบบวิเคราะห์บริบทภาษาไทยสำหรับ AEON MATRIX
    """

    def __init__(self):
        file_path = Path(__file__).parent / "idioms" / "thai_idioms.json"

        with open(file_path, "r", encoding="utf-8") as file:
            self.data = json.load(file)

    def analyze(self, message: str):
        results = []

        for item in self.data["สำนวน"]:
            if item["ข้อความ"] in message:
                results.append(item)

        return results
