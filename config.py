class MedInvestorConfig:
    api_key = "cfd77bb0b41247eb0ffcffdc39c7bc51.6AADA3IxXikTek54"
    prompts = {
        "ctd_analyser": "现在你是一位临床药理学家，你的工作是分析临床研究报告并找出该文章提供的有效的临床试验数据，例如常见的药代动力学参数与安全性参数。你应该以纯粹的json格式输出你所找到的数据，在输出中只需要给出json，不需要给出其他的提示信息，也不需要以markdown包裹json代码，请你直接给出纯文本的json格式输出。你需要分析下面这份报告：<DATAHOLDER>",
        "stock_analyser": "",
        "general_analyser": ""
    }
    dataholder="<DATAHOLDER>"