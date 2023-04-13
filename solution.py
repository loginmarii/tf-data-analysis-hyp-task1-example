import pandas as pd
import numpy as np


chat_id = 1676035524  # Ваш chat ID, не меняйте название переменной

def solution(x_success: int,
             x_cnt: int,
             y_success: int,
             y_cnt: int) -> bool:
    h0 = float(x_success) / x_cnt
    h1 = float(y_success) / y_cnt
    if h1 > h0:
        b = True
    else:
        b = False
    return b  # Ваш ответ, True или False
