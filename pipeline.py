from kfp import dsl, compiler


@dsl.component(base_image="python:3.10-slim")
def prepare_data() -> list:
    data = [2, 4, 6, 8, 10, 12]
    print("Данные подготовлены:", data)
    return data


@dsl.component(base_image="python:3.10-slim")
def train_model(data: list) -> float:
    coefficient = sum(data) / len(data)
    print("Модель обучена. Среднее значение:", coefficient)
    return coefficient


@dsl.component(base_image="python:3.10-slim")
def evaluate_model(coefficient: float) -> str:
    result = "успешно" if coefficient == 7 else "ошибка"
    print("Оценка модели:", result)
    print("Полученный коэффициент:", coefficient)
    return result


@dsl.pipeline(
    name="simple-ml-pipeline",
    description="Простой ML-процесс: подготовка данных, обучение и оценка модели."
)
def ml_pipeline():
    data_task = prepare_data()
    train_task = train_model(data=data_task.output)
    evaluate_model(coefficient=train_task.output)


if __name__ == "__main__":
    compiler.Compiler().compile(
        pipeline_func=ml_pipeline,
        package_path="pipeline.yaml"
    )
    print("Pipeline успешно скомпилирован: pipeline.yaml")
