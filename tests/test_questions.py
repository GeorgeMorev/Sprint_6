import allure
import pytest

QUESTIONS_ANSWERS = [
    (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
    (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
    (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
    (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
    (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
    (6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
    (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
]

@allure.feature('FAQ Section')
@allure.story('Проверка ответов на частые вопросы')
@pytest.mark.parametrize(
    "question_num,expected_answer",
    QUESTIONS_ANSWERS,
    ids=[f"Question {num}" for num, _ in QUESTIONS_ANSWERS]
)
def test_question_dropdown(home_page, question_num, expected_answer):
    with allure.step(f'Проверка вопроса №{question_num + 1}'):
        allure.dynamic.title(f'Проверка ответа на вопрос №{question_num + 1}')
        
        with allure.step(f'Кликнуть на вопрос №{question_num + 1}'):
            home_page.click_question(question_num)
            allure.attach(
                str(question_num),
                name="Question number",
                attachment_type=allure.attachment_type.TEXT
            )
        
        with allure.step('Получить текст ответа'):
            actual_answer = home_page.get_answer_text(question_num)
            allure.attach(
                actual_answer,
                name="Actual answer",
                attachment_type=allure.attachment_type.TEXT
            )
        
        with allure.step('Сравнить с ожидаемым ответом'):
            allure.attach(
                expected_answer,
                name="Expected answer",
                attachment_type=allure.attachment_type.TEXT
            )
            assert actual_answer == expected_answer, (
                f"\nОжидаемый ответ: {expected_answer}"
                f"\nФактический ответ: {actual_answer}"
            )