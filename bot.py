import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env (для локальной разработки)
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

# Инициализация диспетчера
dp = Dispatcher()


# --- Клавиатуры ---
def get_main_keyboard() -> ReplyKeyboardMarkup:
    """Создает главную Reply-клавиатуру бота."""
    kb = [
        [KeyboardButton(text="О нас")],
        [KeyboardButton(text="Направления"), KeyboardButton(text="Контакты")],
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите раздел...",
    )


# --- Обработчики команд и сообщений ---


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    """Обработчик команды /start."""
    welcome_text = (
        f"Здравствуйте, {message.from_user.full_name}!\n\n"
        "Добро пожаловать в бот **Молодежного ресурсного центра**! 👋\n\n"
        "Мы помогаем молодежи развиваться, реализовывать проекты и находить единомышленников. "
        "Используйте кнопки меню ниже, чтобы узнать больше о нашей деятельности."
    )
    await message.answer(
        text=welcome_text,
        reply_markup=get_main_keyboard(),
        parse_mode="Markdown",
    )


@dp.message(F.text == "О нас")
async def about_us_handler(message: types.Message) -> None:
    """Обработчик кнопки 'О нас'."""
    text = (
        "🏛 **О Молодежном ресурсном центре**\n\n"
        "МРЦ — это единая площадка для поддержки молодежных инициатив, "
        "личностного и профессионального роста.\n\n"
        "**Наша миссия:**\n"
        "Создание благоприятных условий для всестороннего развития молодежи, "
        "поддержка социальных проектов и вовлечение юношей и девушек в общественную жизнь.\n\n"
        "**Чем мы занимаемся:**\n"
        "• Консультирование молодежи по социальным и правовым вопросам;\n"
        "• Организация обучающих тренингов, мастер-классов и семинаров;\n"
        "• Поддержка волонтёрских и экологических движений;\n"
        "• Помощь в профориентации и трудоустройстве."
    )
    await message.answer(text=text, parse_mode="Markdown")


@dp.message(F.text == "Направления")
async def directions_handler(message: types.Message) -> None:
    """Обработчик кнопки 'Направления'."""
    text = (
        "🎯 **Основные направления деятельности**\n\n"
        "1️⃣ **Волонтёрство и благотворительность**\n"
        "Развитие добровольческого движения, участие в социальных и экологических акциях.\n\n"
        "2️⃣ **Трудоустройство и профориентация**\n"
        "Ярмарки вакансий, помощь в составлении резюме, консультации по карьерному старту.\n\n"
        "3️⃣ **Творчество и досуг**\n"
        "Организация фестивалей, творческих вечеров, спортивных турниров и киберспортивных соревнований.\n\n"
        "4️⃣ **Молодежное предпринимательство**\n"
        "Обучение основам бизнеса, помощь в подготовке стартапов и участие в грантовых программах.\n\n"
        "5️⃣ **Правовая и психологическая поддержка**\n"
        "Бесплатные консультации для молодежи, оказавшейся в трудной жизненной ситуации."
    )
    await message.answer(text=text, parse_mode="Markdown")


@dp.message(F.text == "Контакты")
async def contacts_handler(message: types.Message) -> None:
    """Обработчик кнопки 'Контакты'."""
    text = (
        "📍 **Контакты и режим работы**\n\n"
        "🏢 **Адрес:** ул. Молодежная, д. 10, кабинет 101\n"
        "📞 **Телефон:** +7 (700) 000-00-00\n"
        "✉️ **E-mail:** info@mrc.kz\n\n"
        "⏰ **Режим работы:**\n"
        "Понедельник — Пятница: 09:00 - 18:30\n"
        "Перерыв: 13:00 - 14:30\n"
        "Суббота, Воскресенье: Выходной\n\n"
        "🌐 **Мы в соцсетях:**\n"
        "• Instagram: @mrc_official\n"
        "• Telegram: @mrc_channel"
    )
    await message.answer(text=text, parse_mode="Markdown")


# --- Запуск бота ---
async def main() -> None:
    if not TOKEN:
        sys.exit("Ошибка: Переменная окружения BOT_TOKEN не задана!")

    bot = Bot(token=TOKEN)

    # Запуск процесса поллинга (получения обновлений)
    print("Бот успешно запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())