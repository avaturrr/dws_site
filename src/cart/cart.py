from _decimal import Decimal

from src.settings import CART_SESSION_ID

from dws_site.models import Product


class Cart: #словарь где ключ - айди продукта, значение- словарь из цены и количества
    def __init__(self, request):
        self.session = request.session #создаем атрибут сессию
        cart = self.session.get(CART_SESSION_ID) #получаем из сессии словарь
        if not cart: #если там нет данных
            cart = self.session[CART_SESSION_ID] = {} #добавляем пустые ключ значение
        self.cart = cart #сохраняем в атрибут словарь

    def __iter__(self): #
        products_id = self.cart.keys()
        products = Product.objects.filter(id__in=products_id)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        quantity_item = 0
        for _ in self.cart:
            quantity_item += 1
        return quantity_item

    def add(self, product, quantity=1, update_quantity=False):
        product_id = product.id #получаем айдишник товара
        if product_id not in self.cart: #проверяем есть ли этот товар в корзине
            self.cart[product_id] = {'quantity': 0,
                                 'price': str(product.price)} #добавляем словарь
        if update_quantity: #
            self.cart[product_id]['quantity'] = quantity #
        else:
            self.cart[product_id]['quantity'] += quantity #
        self.save()

    def save(self):
        self.session[CART_SESSION_ID] = self.cart #
        self.session.modified = True

    def delete(self, product_id):
        del self.cart[product_id]
        self.save()

    def clean_cart(self):
        del self.session[CART_SESSION_ID] #
        self.session.modified = True #

