import argparse
import os
from dotenv import load_dotenv

from config.config_file_loader import ConfigYamlLoader
# from utils import parse_json_file_cases
from llm.utils import get_gpt_api_llm, get_gpt_oss_llm, gpt_api_llm_generate, gpt_oss_llm_generate
from core.sql_extraction import get_sql_extraction_prompt

def get_parser():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path', type=str, \
        default='./config/llm_config.yaml')
    parser.add_argument('--user_query', type=str, \
        required=True)
    parser.add_argument('--llm', type=str, \
        choices=["gpt_api", "gpt_oss_20b"],
        required=True, default="gpt_api")
    
    return parser.parse_args()

if __name__ == '__main__':
    
    ## Args
    args = get_parser()
    
    ## Query
    user_query = args.user_query
    print(f'- User query: {user_query}')

    sql_extraction_prompt = get_sql_extraction_prompt(user_query=user_query)

    if args.llm == "gpt_api":
            
        ## Config
        config_loader = ConfigYamlLoader()
        config = config_loader.load_config(args.config_path)
        # print('config:', config)
    
        ## API
        load_dotenv()
        config['llm']['api_key'] = os.getenv('token')
        gpt_api_llm = get_gpt_api_llm(config)

        ## Generate
        sql_result = gpt_api_llm_generate(config, gpt_api_llm, sql_extraction_prompt, streaming=False, callbacks=None)
    
    elif args.llm == "gpt_oss_20b":

        messages = [
            {"role": "user", "content": sql_extraction_prompt},
        ]

        gpt_oss_llm_pipe = get_gpt_oss_llm()

        sql_result = gpt_oss_llm_generate(gpt_oss_llm_pipe, messages)

    print('- SQL Result:', sql_result)
    