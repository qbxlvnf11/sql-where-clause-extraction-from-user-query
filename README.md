SQL Extraction with LLM
=============

### - SQL Extraction Example (GPT4o)

   <details>
   <summary>Output Example 1</summary>

   - Query: Please recommend an industrial public works program that can be supported until 2018.

   '''json
   {
      "sql_where_clause": "end_date >= '2018-01-01'",
      "explanation": "Filtering for programs that were available for support until at least the year 2018."
   }
   '''
   </details>

   <details>
   <summary>Output Example 2</summary>

   - Query: Youth Support Programs Available in 2022.

   '''json
   {
      "sql_where_clause": "target_audience = 'youth' AND start_date <= '2022-12-31' AND end_date >= '2022-01-01'",
      "explanation": "The filter condition searches for programs targeted at 'youth' that were available at any time during the year 2022."
   }
   '''
   </details>

### - SQL Extraction Example (GPT-OSS 20b)

   <details>
   <summary>Output Example 1</summary>

   - Query: ...

   '''json
   ...
   '''
   </details>


Docker Environment
=============

### - Docker Build

```
docker build -t sql_extraction_test .
```

### - Docker Run

```
docker run -it --gpus all --name sql_extraction_test_env --shm-size=64G -p {port}:{port} -e GRANT_SUDO=yes --user root -v {root_folder}:/workspace/sql_extraction_test -w /workspace/sql_extraction_test sql_extraction_test bash
```

### - Docker Exec

```
docker exec -it sql_extraction_test_env bash
```


SQL Extraction Test
=============

### - SQL Extraction (GPT4o)

   - When using the GPT API, enter the API KEY (token) in the '.env' file created after executing the initialization command
      
```
python sql_extraction.py --config_path config/llm_config.yaml --user_query "{user_query}" --llm gpt_api
```

### - SQL Extraction (GPT-OSS 20b)

```
python sql_extraction.py --config_path config/llm_config.yaml --user_query "{user_query}" --llm gpt_oss_20b
```


Author
=============

#### - LinkedIn: https://www.linkedin.com/in/taeyong-kong-016bb2154

#### - Blog URL: https://blog.naver.com/qbxlvnf11

#### - Email: qbxlvnf11@google.com, qbxlvnf11@naver.com

