from Containers.DF_Pandas import Pandas_Container
from Containers.List2JSON import Save2JSON_Container


if __name__ == "__main__" :
   

    df_boundary = Pandas_Container().boundary()
    reviews = df_boundary.get_reviews('message')  # Получил все отзывы  
    entire_df = df_boundary.get_all_dataframe()   # Получил весь датафрейм
    print('Импотированный датасет сохранен и приведен к нужному формату - ', type(entire_df))
    
    entire_df=entire_df.to_dict(orient='records')
    json_saver = Save2JSON_Container()
    json_saver.config.nested_list.from_value(entire_df)
    
    json_saver.init_convert().save_to_json('Results_In_JSON','entire_df.json')



    '''
    
     ## Сохрание ключ. фраз в JSON 

    sentiment_boundary = SentimentModel_Container().boundary()
    result = sentiment_boundary.analyze_sentiments(list_by_groups, topics)
    print('Sentiment Analysis произведён. Число строк в таблице',len(result))
    sliced_df = pd.concat([result.head(5), result.tail(5)])
    print ('Результирующий DataFrame',sliced_df)

    postprocess = DataPostProcess_Container().boundary()
    new_dataframe = postprocess.validate_and_process(result, entire_df)
    sliced_df = pd.concat([new_dataframe.head(5), new_dataframe.tail(5)])
    print ('Постобработка DataFrame',sliced_df)

    weigths_norma = NormalizerWeight_Container().boundary()
    print('new_dataframe',new_dataframe.info()) 
    recalc_df = weigths_norma.process_grading(new_dataframe)
    print('recalc_df',recalc_df.info())    
    sliced_df = pd.concat([recalc_df.head(5), recalc_df.tail(5)])
    print ('Оценки пересчитаны',sliced_df)

    final_entries = Split_DF_Container().boundary()
    list_of_df = final_entries.process_data(recalc_df)    
    print ('DataFrame разделен по схеме нормализованной БД')
    print(len(list_of_df))
    for entry in list_of_df:
        filename, groups = next(iter(entry.items()))
        json_saver.config.nested_list.from_value(groups)
        json_saver.init_convert().save_to_json('Results_in_JSON',f'{filename}.json')
    print ('Таблицы DataFrame сохранены в JSON формате. Модуль завершает работу')
    '''
