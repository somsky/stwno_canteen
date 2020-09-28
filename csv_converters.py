import datetime
from stwno_constants import CSV_MEAL_TYPE_MAP,\
    CSV_NUTRITION_TYPE_MAP,\
    NutritionType,\
    CSV_DATE_FORMAT,\
    MealType,\
    NutritionType


class NoValidDateStringException(Exception):
    pass


class UnknownMealTypeException(Exception):
    pass


class UnknownNutritionTypeException(Exception):
    pass


def convertCSVDishName(name: str) -> str:
    name = name.strip()
    indexBracket = name.find('(')
    if indexBracket == -1:
        return name
    return name[0:indexBracket].strip()


def convertCSVMealType(mealType: str) -> MealType:
    mealTypeID = ''.join(filter(str.isalpha, mealType))
    mType = CSV_MEAL_TYPE_MAP.get(mealTypeID)
    if mType != None:
        return mType
    else:
        raise UnknownMealTypeException(
            'MealType {} is not in the list of known meal types'.format(mType))


def convertCSVNutritionType(nutritionType: str) -> NutritionType:
    nutType = CSV_NUTRITION_TYPE_MAP.get(nutritionType)
    if nutType != None:
        return nutType
    else:
        return NutritionType.meat


def convertCSVDate(dateStr: str) -> datetime.date:
    try:
        return datetime.datetime.strptime(dateStr, CSV_DATE_FORMAT).date()
    except ValueError:
        raise NoValidDateStringException

