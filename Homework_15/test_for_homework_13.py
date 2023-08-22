from Homework_13.drivers.base_class import Menu
from Homework_13.drivers.drinks import Drink
from Homework_13.drivers.dishes import Dish
from Homework_13.homework_13 import OrderPart
import pytest

@pytest.fixture
def dish_instance():
    return Dish()

@pytest.fixture
def drink_instance():
    return Drink()

@pytest.mark.dish
def test_dish_positions(dish_instance):
    assert len(dish_instance.positions) == 3
    assert 'Risotto' in dish_instance.positions
    assert 'Pasta' in dish_instance.positions
    assert 'Pizza' in dish_instance.positions

@pytest.mark.drink
def test_drink_positions(drink_instance):
    assert len(drink_instance.positions) == 3
    assert 'Water' in drink_instance.positions
    assert 'Juice' in drink_instance.positions
    assert 'Wine' in drink_instance.positions

@pytest.mark.parametrize("menu_type, position, expected_output", [
    ('dish', 'Risotto', 'Here is your risotto'),
    ('dish', 'Pasta', 'Here is your pasta'),
    ('dish', 'Pizza', 'Here is your pizza'),
    ('dish', 'Burger', 'We do not have this position in menu'),
    ('drink', 'Water', 'Here is your water'),
    ('drink', 'Juice', 'Here is your juice'),
    ('drink', 'Wine', 'Here is your wine'),
    ('drink', 'Cola', 'We do not have this position in menu')
])

@pytest.mark.regression
def test_order_menu_item(menu_type, position, expected_output):
    menu = OrderPart.get_menu(menu_type)
    result = menu.order(position)
    assert result == expected_output

@pytest.mark.xfail(reason="Here should be the error. (Negative test)")
def test_order_nonexistent_item():
    menu = OrderPart.get_menu('dish')
    result = menu.order('Sushi')
    assert result == 'Here is your sushi'



