
import requests

def fetch_random_meal_freeapi():
    url = "https://api.freeapi.app/api/v1/public/meals/meal/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        mealname = user_data["strMeal"]
        instructions = user_data["strInstructions"]
        return mealname, instructions

    else:
        raise Exception("Failed to fetch data")

def main():
    try:
        mealname, intructions = fetch_random_meal_freeapi()
        print(f"mealname: {mealname}  \ninstructions: {intructions}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()    