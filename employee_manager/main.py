from models import Employee


def main():
    emp = Employee.from_dict(
        {
            "name": "Ahmed",
            "age": 30,
            "role": "manager",
            "email": "ahmed@gmail.com",
            "id": 1,
        }
    )

    data = emp.to_dict()
    print(f"Serialized: {data}")

    new_emp = Employee.from_dict(data)
    print(f"Object: {new_emp.name}")


if __name__ == "__main__":
    main()
