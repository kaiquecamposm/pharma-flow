from dataclasses import dataclass


@dataclass
class CourseParticipation:
    course_id: str
    professional_id: str
    attendance_percent: float = 0.0
    grade_percent: float = 0.0