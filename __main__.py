from Containers.DF_Pandas import Pandas_Container
from Containers.List2JSON import Save2JSON_Container
import os

if __name__ == "__main__" :
   

    df_boundary = Pandas_Container().boundary()
    reviews = df_boundary.get_reviews('message')  # Получил все отзывы  
    entire_df = df_boundary.get_all_dataframe()   # Получил весь датафрейм
    print('Импотированный датасет сохранен и приведен к нужному формату - ', type(entire_df))
    
    entire_df=entire_df.to_dict(orient='records')
    json_saver = Save2JSON_Container()
    json_saver.config.nested_list.from_value(entire_df)
    
    # Создаю путь для сохранения файла
    current_dir = os.path.dirname(__file__)
    relative_path = os.path.join(current_dir, 'Results_In_JSON')
    
    json_saver.init_convert().save_to_json(relative_path,'entire_df.json')



    '''
  
    for entry in list_of_df:
        filename, groups = next(iter(entry.items()))
        json_saver.config.nested_list.from_value(groups)
        json_saver.init_convert().save_to_json('Results_in_JSON',f'{filename}.json')
    print ('Таблицы DataFrame сохранены в JSON формате. Модуль завершает работу')
    '''
