import json
from datetime import datetime

from instruction_prompt.sql_extraction_prompt import SQL_EXTRACTION

def get_sql_extraction_prompt(user_query, verbose=True):

    current_date = datetime.now().strftime('%Y-%m-%d')
    sql_extraction = SQL_EXTRACTION.format(
        current_date=current_date, user_query=user_query
    )

    if verbose:
        print(f'- SQL extraction: {sql_extraction}')
    
    prompt = [
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
        {"role": "user", "content": sql_extraction}
    ]
    
    return prompt
