from airflow.sdk import dag, task
import pendulum

@dag(
    dag_id="simple_ml_pipeline",
    schedule=None,
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    catchup=False,
    tags=["mlops"],
)
def simple_ml_pipeline():

    @task
    def load_data():
        print("STEP 1: Loading data")
        return [10, 20, 30, 40]

    @task
    def preprocess_data(data):
        print("STEP 2: Preprocessing data")
        return [x / 10 for x in data]

    @task
    def train_model(data):
        print("STEP 3: Training model")
        print("Training data:", data)
        return "trained_model"

    @task
    def evaluate_model(model):
        print("STEP 4: Evaluating model")
        print("Model:", model)
        print("Accuracy = 0.90")
        return 0.90

    data = load_data()
    processed_data = preprocess_data(data)
    model = train_model(processed_data)
    evaluate_model(model)


simple_ml_pipeline()
