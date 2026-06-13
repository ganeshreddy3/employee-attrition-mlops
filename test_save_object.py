from src.utils.common import save_object

sample = {
    "name": "Ganesh",
    "project": "Employee Attrition"
}

save_object(
    "artifacts/test/sample.pkl",
    sample
)

print("Object saved successfully")

