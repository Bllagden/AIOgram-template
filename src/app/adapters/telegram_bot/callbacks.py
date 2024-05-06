from aiogram.filters.callback_data import CallbackData


class RandomCallback(CallbackData, prefix="random_value"):
    pass
