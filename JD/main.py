import sys

from maotai.jd_spider_requests import ProdectPurchase


if __name__ == '__main__':
    tip = """                                            
功能列表：                                                                                
 1.预约商品
 2.秒杀抢购商品
    """
    print(tip)

    product = ProdectPurchase()
    choice_function = input('请选择:')
    if choice_function == '1':
        product.reserve()
    elif choice_function == '2':
        product.seckill_by_proc_pool()
    else:
        print('没有此功能')
        sys.exit(1)

