import pandas as pd

# Загрузка данных
df = pd.read_excel('C:/Users/1/Documents/Python/Study/OriginTabl.xlsx')

# Группировка с несколькими агрегациями
summary = df.groupby('Артикул поставщика', as_index=False).agg({
    'Продажи': 'sum',           # Сумма продаж
    'Количество продаж': 'count', # количество продаж Артикула
    'Логистика': 'sum',           # Сумма за логистику
    # 'Цена': ['mean', 'max'],    # Средняя и максимальная цена
    'К перечислению': 'sum'             # Сумма к перечислению
})

# Переименование столбцов для удобства
summary.columns = [
    'Артикул поставщика',
    'Сумма продаж',
    'Количество продаж',
    'Сумма за логистику',
    'Сумма к перечислению',
    #'Максимальная цена',
    #'Количество записей'
]

# Сохранение результатов
summary.to_excel('C:/Users/1/Documents/Python/Study/ResultArtandSum.xlsx', 
                index=False,
                sheet_name='TotalData')