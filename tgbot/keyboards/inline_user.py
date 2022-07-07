# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.services.api_sqlite import get_paymentx


# Выбор способов пополнения
def refill_choice_finl():
    keyboard = InlineKeyboardMarkup()

    get_payments = get_paymentx()
    active_kb = []

    if get_payments['way_form'] == "True":
        active_kb.append(InlineKeyboardButton("📋 QIWI форма", callback_data="refill_choice:Form"))
    if get_payments['way_number'] == "True":
        active_kb.append(InlineKeyboardButton("📞 QIWI номер", callback_data="refill_choice:Number"))
    if get_payments['way_nickname'] == "True":
        active_kb.append(InlineKeyboardButton("Ⓜ QIWI никнейм", callback_data="refill_choice:Nickname"))

    if len(active_kb) == 3:
        keyboard.add(active_kb[0], active_kb[1])
        keyboard.add(active_kb[2])
    elif len(active_kb) == 2:
        keyboard.add(active_kb[0], active_kb[1])
    elif len(active_kb) == 1:
        keyboard.add(active_kb[0])
    else:
        keyboard = None

    if len(active_kb) >= 1:
        keyboard.add(InlineKeyboardButton("⬅ Вернуться ↩", callback_data="user_profile"))

    return keyboard


# Проверка киви платежа
def refill_bill_finl(send_requests, get_receipt, get_way):
    keyboard = InlineKeyboardMarkup(
    ).add(
        InlineKeyboardButton("🌀 Перейти к оплате", url=send_requests)
    ).add(
        InlineKeyboardButton("🔄 Проверить оплату", callback_data=f"Pay:{get_way}:{get_receipt}")
    )

    return keyboard


# Кнопки при открытии самого товара
def products_open_finl(position_id, remover, category_id, town_id):
    keyboard = InlineKeyboardMarkup(
    ).add(
        InlineKeyboardButton("💰 Купить товар", callback_data=f"buy_item_select:{position_id}:None:{town_id}")
    ).add(
        InlineKeyboardButton("🈹 Ввести промокод", callback_data=f"enter_promo_code:{position_id}:{town_id}")
    ).add(
        InlineKeyboardButton("⬅ Вернуться ↩", callback_data=f"buy_position_return:{remover}:{category_id}:{town_id}")
    )

    return keyboard


def buy_item_select_promo_code(position_id, discount, town_id):
    keyboard = InlineKeyboardMarkup(
    ).add(
        InlineKeyboardButton(f"💰 Купить товар со скидкой {discount}%",
                             callback_data=f"buy_item_select:{position_id}:{discount}:{town_id}")
    )

    return keyboard


# Подтверждение покупки товара
def products_confirm_finl(position_id, get_count, town_id, price):
    keyboard = InlineKeyboardMarkup(
    ).add(
        InlineKeyboardButton("✅ Подтвердить", callback_data=f"xbuy_item:yes:{position_id}:{get_count}:{town_id}:{price}"),
        InlineKeyboardButton("❌ Отменить", callback_data=f"xbuy_item:not:{position_id}:{get_count}:{town_id}:{price}")
    )

    return keyboard


# Ссылка на поддержку
def user_support_finl(user_name):
    keyboard = InlineKeyboardMarkup(
    ).add(
        InlineKeyboardButton("💌 Написать в поддержку", url=f"https://t.me/{user_name}"),
    )

    return keyboard
