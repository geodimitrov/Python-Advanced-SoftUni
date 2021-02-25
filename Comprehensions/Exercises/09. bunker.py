def get_quantity_and_quality(item_data):
    result = [el.split(":") for el in item_data.split(";")] # split quantity&quality data into different cells
    return result

def get_item_quantity(quantity_data):
    return int(quantity_data[1])  # the number of items is the 2nd el in the quantity list, turn to int

def get_item_quality(quality_data):
    return int(quality_data[1])  # the quality is the 2nd el in the quality list, turn to int

def create_food_collection(food_categories, lines):
    food_dict = {category: {} for category in food_categories} #create dict with food categories
    items_count = 0  # create variable to count all items in the collection
    quality_sum = 0  # create variable to sum all qualities in the collection
    for line in range(lines):
        category, item, item_data = input().split(" - ")
        quantity, quality = get_quantity_and_quality(item_data)
        items_count += get_item_quantity(quantity)
        quality_sum += get_item_quality(quality)
        food_dict[category][item] = quantity, quality
    return food_dict, items_count, quality_sum

def get_average_quality(collection, sum_quality):
    result = sum_quality/len(collection)
    return result

def print_result(food_collection, items_count, sum_quality):
    average_quality = get_average_quality(food_collection, sum_quality)
    print(f"Count of items: {items_count}")
    print(f"Average quality: {average_quality:.2f}")
    for category, items in food_collection.items():
        result = []
        for item in items:
            result.append(item)
        result = ", ".join(result)
        print(f"{category} -> {result}")


categories = input().split(", ") #the initial food categories
lines = int(input())  #num of lines to read

#create function to fill in collection with data
food_collection, items_count, sum_quality = create_food_collection(categories, lines)
print_result(food_collection, items_count, sum_quality)