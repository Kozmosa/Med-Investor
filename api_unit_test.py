import analysers

def general_test() -> str:
    analyser = analysers.Analyser()
    result = analyser.general(prompt="你是一个人工智能语言模型", 
                     req="请你做一个自我介绍")
    return str(result)

if __name__ == "__main__":
    # test
    result = general_test()
    print("General test result is " + result)