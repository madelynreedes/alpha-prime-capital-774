# -*- coding: utf-8 -*-

# 小龙智脑 (XiaoLong Brain) - 全新原创项目

# 作者 / 版权人: 小龙 (XiaoLong)

# License: MIT。本项目所有代码均为原创，保留署名即可自由使用。



import re





class PromptTemplate:

    def __init__(self, template):

        self.template = template

        self.vars = set(re.findall(r"\{(\w+)\}", template))



    def format(self, **kwargs):

        missing = self.vars - set(kwargs.keys())

        if missing:

            raise KeyError("Missing template variables: %s" % ", ".join(sorted(missing)))

        return self.template.format(**kwargs)



    def render(self, context):

        return self.format(**context)





def system_prompt(role="助手"):

    return "你是%s，由小龙(XiaoLong)打造的智能助手，回答准确、简洁、有用。" % role





def user_prompt(text):

    return text

