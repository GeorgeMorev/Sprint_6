import allure
import pytest

ORDER_DATA = [
    (
        'header',
        {
            'name': 'Иван',
            'last_name': 'Иванов', 
            'address': 'ул. Пушкина, 10',
            'metro': 'Сокольники',
            'phone': '+79991234567'
        },
        {
            'date': '2024-03-15',
            'period': 'сутки', 
            'color': 'black',
            'comment': 'Тестовый заказ'
        }
    )
]

@allure.feature('Оформление заказа')
@allure.story('Проверка полного цикла оформления заказа')
@pytest.mark.parametrize(
    "entry_point,personal_info,rent_info", 
    ORDER_DATA,
    ids=["Header order flow test"]
)
def test_order_flow(home_page, order_page, entry_point, personal_info, rent_info):
    with allure.step(f'Инициализировать тест с точкой входа "{entry_point}"'):
        allure.dynamic.title(f'Оформление заказа через {entry_point}')
        allure.dynamic.description(f'Проверка полного цикла оформления через {entry_point} кнопку')
        
    with allure.step('Нажать кнопку оформления заказа'):
        home_page.click_order_button(entry_point)
        allure.attach(
            home_page.driver.current_url,
            name="Current URL after click",
            attachment_type=allure.attachment_type.TEXT
        )
    
    with allure.step('Заполнить персональные данные'):
        order_page.fill_personal_info(**personal_info)
        allure.attach(
            str(personal_info),
            name="Personal info",
            attachment_type=allure.attachment_type.JSON
        )
    
    with allure.step('Заполнить данные аренды'):
        order_page.fill_rent_info(**rent_info)
        allure.attach(
            str(rent_info),
            name="Rent info",
            attachment_type=allure.attachment_type.JSON
        )
    
    with allure.step('Подтвердить заказ'):
        order_page.confirm_order()
    
    with allure.step('Проверить сообщение об успешном оформлении'):
        success_message = order_page.get_success_message()
        allure.attach(
            success_message,
            name="Success message",
            attachment_type=allure.attachment_type.TEXT
        )
        assert "Заказ оформлен" in success_message, (
            f'Ожидалось "Заказ оформлен" в сообщении, получено: {success_message}'
        )