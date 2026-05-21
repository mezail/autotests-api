from pydantic import BaseModel

class CourseSchema(BaseModel):
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str

# Инициализируем модель CourseSchema через передачу аргументов
course_default_model = CourseSchema(
        id="course-id",
        title="Playwright",
        maxScore=100,
        minScore=10,
        description="Playwright",
        estimatedTime="1 week"
)
print('Course default model:', course_default_model)

# Инициализируем модель CourseSchema через распаковку словаря
course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}
course_dict_model = CourseSchema(**course_dict)
print('Course dict model:', course_dict_model)

# Инициализируем модель CourseSchema через JSON
course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print('Course JSON model:', course_json_model)