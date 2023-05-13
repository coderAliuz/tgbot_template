from aiogram.dispatcher.filters.state import State,StatesGroup


class home(StatesGroup):
    home_states=State()
    result_states=State()

#admin
class tests(StatesGroup):
    type_states=State()
    type_add_states=State()
    test_add_state=State()
    test_states=State()
    photo_states=State()
    answer_states=State()
    check_states=State()

class searches(StatesGroup):
    search=State()
    test_states=State()
    user_states=State()

#user
class users_tests(StatesGroup):
    start_states=State()
    check_states=State()

class users_register(StatesGroup):
    fullname=State()
    phone=State()
