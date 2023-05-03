from aiogram.dispatcher.filters.state import State,StatesGroup

class tests(StatesGroup):
    test_states=State()
    photo_states=State()
    answer_states=State()
    check_states=State()
    delete_states=State()

class home(StatesGroup):
    home_states=State()