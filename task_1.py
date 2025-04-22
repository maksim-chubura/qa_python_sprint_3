import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    # 1. Напиши геттеры
    # Геттер для получения списка товаров в чеке
    @property
    def name_items(self):
        return self.__name_items
    
    # Геттер для получения количества товаров в чеке
    @property
    def number_items(self):
        return self.__number_items
    
    # 2. Добавь товар в чек
    # метод добавляет товар в чек
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        
        # добавляем товар в чек
        self.__name_items.append(name)
        self.__number_items += 1

    # 3. Удали товар из чека
    # метод удаляет товар из чек
    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        
        # удаляем товар из чека
        self.__name_items.remove(name)
        self.__number_items -= 1

    # 4. Посчитай общую стоимость товаров
    # метод считает общую стоимость товаров
    def check_amount(self):
        total = 0

        # считаем общую стоимость товаров
        for item in self.__name_items:
            total += self.__item_price[item]

        # применяем скидку, если товаров больше 10
        if self.__number_items > 10:
            total *= 0.9
        
        return total
    
    # 5. Вычисли НДС для товаров со ставкой 20%
    # метод вычисляет НДС для товаров со ставкой 20%
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = 0

        # добавляем товары с налоговой ставкой 20% в список
        for item in self.__name_items: 
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)

        # считаем общую стоимость товаров с НДС 20%
        for item in twenty_percent_tax:
            total += self.__item_price[item] * 0.2

        # применяем скидку, если товаров больше 10
        if self.__number_items > 10:
            total *= 0.9

        return total
    
    # 6. Вычисли НДС для товаров со ставкой 10%
    # метод вычисляет НДС для товаров со ставкой 10%

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = 0

        # добавляем товары с налоговой ставкой 10% в список
        for item in self.__name_items: 
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)

        # считаем общую стоимость товаров с НДС 10%
        for item in ten_percent_tax:
            total += self.__item_price[item] * 0.1

        # применяем скидку, если товаров больше 10
        if self.__number_items > 10:
            total *= 0.9

        return total
    
    # 7. Посчитай общую сумму налогов
    # метод считает общую сумму налогов
    def total_tax(self):
        total = self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()
        return total
    
    # 8. Верни номер телефона покупателя
    # метод возвращает номер телефона
    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        
        str_number = str(telephone_number)

        if len(str_number) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        
        return f'+7{str_number}'
    
    
    # Дополнительное задание

    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()

        # список временных интервалов и соответствующих лямбда-функций
        date = [
            ['часы', lambda x: x.hour],
            ['минуты', lambda x: x.minute],
            ['день', lambda x: x.day],
            ['месяц', lambda x: x.month],
            ['год', lambda x: x.year]
        ]

        # цикл для заполнения date_and_time
        for interval in date:
            date_and_time.append(f'{interval[0]}: {interval[1](now)}')
        
        return date_and_time