from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Поступление: шаг за шагом'),
        ],
        [
            KeyboardButton(text='Факультет и программы обучения')
        ],
        [
            KeyboardButton(text='Оплата, скидки и гранты'),
        ],
        [
            KeyboardButton(text='Учёба, практика и студенческая жизнь'),
        ],
        [
            KeyboardButton(text='Контакты и часто задаваемые вопросы'),
        ]
    ], resize_keyboard=True
)


facult_inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text='Реклама и связи с общественностью',
            callback_data='ad'
        )],
        [InlineKeyboardButton(
            text='Туризм',
            callback_data='tour'
        )],
        [InlineKeyboardButton(
            text='Гостиничное дело',
            callback_data='hotel'
        )],
        [InlineKeyboardButton(
            text='Сервис (гостинично-ресторанный)',
            callback_data='service'
        )],
        [InlineKeyboardButton(
            text='Реклама и СО(двойной диплом КНР)',
            callback_data='double_ad'
        )],
        [
            InlineKeyboardButton(
                text='В начало',
                callback_data='main_menu'
            )
        ]
    ]
)


inline_back_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Назад',
                callback_data='back'
            ),
        ]
    ]
)


inline_admission_first = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Далее',
                callback_data='first_step'
            ),
        ]
    ]
)


inline_admission_sec = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Далее',
                callback_data='second_step'
            ),
        ]
    ]
)


inline_admission_third = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Далее',
                callback_data='third_step'
            ),
        ]
    ]
)


back_to_main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='В начало',
                callback_data='main_menu'
            )
        ]
    ]
)


pay_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='График оплаты обучения',
                callback_data='graph'
            ),],
        [
            InlineKeyboardButton(
                text='Гранты и скидки на обучение',
                callback_data='grants',
            )
        ],
        [
            InlineKeyboardButton(
                text='В начало',
                callback_data='main_menu'
            )
        ]
    ]
)


practice_main_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Образовательный процесс',
                callback_data='edu'
            )
        ],
        [
            InlineKeyboardButton(
                text='Практика и стажировки',
                callback_data='practice'
            )
        ],
        [
            InlineKeyboardButton(
                text='Академическая мобильность и международные программы',
                callback_data='academ'
            )
        ],
        [
            InlineKeyboardButton(
                text='Общежитие и инфраструктура',
                callback_data='infra'
            )
        ],
        [
            InlineKeyboardButton(
                text='Академические задолженности',
                callback_data='debt')
        ],
        [
            InlineKeyboardButton(
                text='В начало',
                callback_data='main_menu'
            )
        ]
    ]
)

inline_debt_first = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Далее',
                callback_data='debt_one'
            ),
        ]
    ]
)


inline_debt_sec = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Далее',
                callback_data='debt_two'
            ),
        ]
    ]
)

inline_debt_three = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Далее',
                callback_data='debt_three'
            ),
        ]
    ]
)


inline_debt_four = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Далее',
                callback_data='debt_four'
            ),
        ]
    ]
)


inline_contacts = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Контакты и прием документов',
                callback_data='docs'
            ),],
        [
            InlineKeyboardButton(
                text='Часто задаваемые вопросы',
                callback_data='questions'
            )
        ],
        [
            InlineKeyboardButton(
                text='В начало',
                callback_data='main_menu'
            )
        ]
    ]
)